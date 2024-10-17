import pandas as pd
import re
from collections import Counter
from nltk.corpus import stopwords
import google.generativeai as genai
import json

# Path to your WhatsApp chat export file
file_path = 'C:/Users/aasla/PycharmProjects/Whatsapp_Analytics/WhatsApp-Chat_with_Jacqueline.txt'


# Function to prepare the DataFrame from the chat file
def prepare_dataframe(path):
    """
    Reads a WhatsApp chat export file, parses the messages, and returns a Pandas DataFrame.

    Args:
        path (str): The path to the WhatsApp chat export file.

    Returns:
        pandas.DataFrame: A DataFrame containing the chat data.
    """
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = []
    current_entry = None
    pattern = r'(\d{1,2}/\d{1,2}/\d{2}), (\d{1,2}:\d{2} ?[APM]{2}) - (.*?): (.*)'  # WhatsApp chat format

    for line in lines:
        match = re.match(pattern, line)
        if match:
            if current_entry:
                data.append(current_entry)
            current_entry = list(match.groups())
        else:
            if current_entry:
                current_entry[-1] += '\n' + line.strip()

    if current_entry:
        data.append(current_entry)

    df = pd.DataFrame(data, columns=['Date', 'Time', 'Sender', 'Message'])
    df['Datetime'] = pd.to_datetime(df['Date'] + ', ' + df['Time'], format='%m/%d/%y, %I:%M %p')
    df.drop(columns=['Date', 'Time'], inplace=True)
    df = df[['Datetime', 'Sender', 'Message']]
    return df


# Function to extract and count emojis from text
def extract_and_count_emojis(text):
    """
    Extracts emojis from a string and counts their occurrences.
    Groups heart-related emojis into a single "❤️" category.

    Args:
        text (str): The input text.

    Returns:
        collections.Counter: A Counter object containing emoji counts.
    """
    emoji_pattern = re.compile(
        '['
        u'\U0001F600-\U0001F64F'  # Emoticons
        u'\U0001F300-\U0001F5FF'  # Symbols & Pictographs
        u'\U0001F680-\U0001F6FF'  # Transport & Map Symbols
        u'\U0001F700-\U0001F77F'  # Alchemical Symbols
        u'\U0001F780-\U0001F7FF'  # Geometric Shapes Extended
        u'\U0001F800-\U0001F8FF'  # Supplemental Arrows-C
        u'\U0001F900-\U0001F9FF'  # Supplemental Symbols and Pictographs
        u'\U0001FA00-\U0001FA6F'  # Chess Symbols
        u'\U0001FA70-\U0001FAFF'  # Symbols and Pictographs Extended-A
        u'\U00002702-\U000027B0'  # Dingbats
        u'\U000024C2-\U0001F251'
        ']', flags=re.UNICODE)  # Removed the + that was causing the issue

    heart_emojis = {'❤', '💚', '💙', '💜', '💛', '💓', '💞', '💕', '♥️', '❤️', '🧡', '💗', '💖', '💘',
                    '💝', '🩵', '💟', '🩷', '♥', '❣'}

    all_emojis = emoji_pattern.findall(text)
    filtered_emojis = [emoji for emoji in all_emojis if emoji != '️']
    grouped_emojis = ['❤️' if emoji in heart_emojis else emoji for emoji in filtered_emojis]
    return Counter(grouped_emojis)


# Function to get the top 10 emojis in the chat
def show_top10_emoji(df):
    """
    Finds the top 10 most used emojis in the chat DataFrame.

    Args:
        df (pandas.DataFrame): The chat DataFrame.

    Returns:
        pandas.DataFrame: A DataFrame with the top 10 emojis and their counts.
    """
    all_emojis = ''
    for message in df['Message']:
        all_emojis += message

    emoji_counts = extract_and_count_emojis(all_emojis)
    top_10_emojis = emoji_counts.most_common(10)
    return pd.DataFrame(top_10_emojis, columns=['Emoji', 'Count'])


# Function to get the top 10 emojis used by each person
def show_top10_emoji_per_person(df):
    """
    Finds the top 10 most used emojis by each person in the chat DataFrame.

    Args:
        df (pandas.DataFrame): The chat DataFrame.

    Returns:
        dict: A dictionary where keys are sender names and values are DataFrames
              containing the top 10 emojis and their counts for that sender.
    """
    dataframes = {}
    for sender in df['Sender'].unique():
        sender_df = df[df['Sender'] == sender]
        all_messages = ''.join(sender_df['Message'])
        emoji_counts = extract_and_count_emojis(all_messages)
        top_10_emojis = emoji_counts.most_common(10)
        dataframes[sender] = pd.DataFrame(top_10_emojis, columns=['Emoji', 'Count'])
    return dataframes


# Function to analyze messaging time patterns
def analyze_messaging_time(df):
    """
    Analyzes messaging time patterns to find the most active day and part of the day.

    Args:
        df (pandas.DataFrame): The chat DataFrame.

    Returns:
        tuple: A tuple containing:
            - pandas.DataFrame: DataFrame with message counts by day and part of day
            - str: The most active day
            - str: The most active part of the day
    """
    df['DayOfWeek'] = df['Datetime'].dt.day_name()
    day_abbr = {'Monday': 'Mon', 'Tuesday': 'Tue', 'Wednesday': 'Wed',
                'Thursday': 'Thu', 'Friday': 'Fri', 'Saturday': 'Sat', 'Sunday': 'Sun'}
    df['DayOfWeek'] = df['DayOfWeek'].map(day_abbr)
    df['Hour'] = df['Datetime'].dt.hour

    def categorize_hour(hour):
        if 0 <= hour < 6:
            return 'Early Morn'
        elif 6 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 17:
            return 'Afternoon'
        elif 17 <= hour < 22:
            return 'Evening'
        else:
            return 'Late Night'

    df['PartOfDay'] = df['Hour'].apply(categorize_hour)
    message_counts = df.groupby(['DayOfWeek', 'PartOfDay']).size().unstack(fill_value=0)
    desired_day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    desired_part_order = ['Early Morn', 'Morning', 'Afternoon', 'Evening', 'Late Night']
    message_counts = message_counts[desired_part_order].reindex(desired_day_order)
    most_active_day, most_active_part = message_counts.stack().idxmax()
    return message_counts, most_active_day, most_active_part


# Function to analyze text statistics for each person
def analyze_text_stats_per_person(df):
    """
    Analyzes various text statistics (word count, unique words, etc.) for each person in the chat.

    Args:
        df (pandas.DataFrame): The chat DataFrame.

    Returns:
        pandas.DataFrame: DataFrame with text statistics transposed (persons as columns).
    """
    stop_words = set(stopwords.words('english'))
    result_df = df.groupby('Sender').agg({
        'Message': ['count', lambda x: ' '.join(x).split()]
    }).rename(columns={'count': 'Message Count', '<lambda_0>': 'All Words'})

    result_df.columns = ['Message Count', 'All Words']
    result_df['Words'] = result_df['All Words'].apply(lambda x: [word for word in x if word.lower() not in stop_words])
    result_df['Word Count'] = result_df['Words'].apply(len)
    result_df['Unique Word Count'] = result_df['Words'].apply(lambda x: len(set(x)))
    result_df['Characters'] = result_df['Words'].apply(lambda x: len(' '.join(x)))
    result_df = result_df[['Message Count', 'Word Count', 'Unique Word Count', 'Characters']]
    return result_df.T


# Function to get the date range of the chat
def get_chat_date_range(df):
    """
    Determines the start and end dates of the chat.

    Args:
        df (pandas.DataFrame): The chat DataFrame.

    Returns:
        tuple: Start date and end date of the chat (formatted as 'YYYY-MM-DD').
    """
    start_date = df['Datetime'].min().strftime('%Y-%m-%d')
    end_date = df['Datetime'].max().strftime('%Y-%m-%d')
    return start_date, end_date


# Function to create a monthly message chart
def monthly_message_chart(df):
    """
    Creates a DataFrame suitable for visualizing monthly message counts.

    Args:
        df (pandas.DataFrame): The chat DataFrame.

    Returns:
        pandas.DataFrame: DataFrame with monthly message counts, transposed
                          for easy plotting (Months as index, Senders as columns)
    """
    df['Month'] = df['Datetime'].dt.to_period('M')
    message_counts_by_month = df.groupby(['Sender', 'Month']).size().unstack(fill_value=0)
    return message_counts_by_month.sort_index().T


# Function to analyze conversations and double messages
def analyze_conversation_and_double_messages(df,
                                             conversation_time_threshold=pd.Timedelta(minutes=60),
                                             double_message_time_threshold=pd.Timedelta(minutes=15),
                                             immediate_response_threshold=pd.Timedelta(seconds=1)):
    """
    Analyzes conversation patterns, including starts/ends, double messages, and response times.

    Args:
        df (pandas.DataFrame): The chat DataFrame.
        conversation_time_threshold (pd.Timedelta): Time gap to define a new conversation.
        double_message_time_threshold (pd.Timedelta): Time gap between messages from the same person to be a "double message"
        immediate_response_threshold (pd.Timedelta):  Time within which a response is considered "immediate"

    Returns:
        pandas.DataFrame: DataFrame containing conversation statistics transposed
                          (statistics as index, senders as columns)
    """
    df_sorted = df.sort_values('Datetime')
    df_sorted['TimeDiff'] = df_sorted['Datetime'].diff()
    df_sorted['ConversationStart'] = df_sorted['TimeDiff'] > conversation_time_threshold
    df_sorted['ConversationEnd'] = df_sorted['TimeDiff'].shift(-1) > conversation_time_threshold
    conversation_starters = df_sorted[df_sorted['ConversationStart']]['Sender']
    conversation_enders = df_sorted[df_sorted['ConversationEnd']]['Sender']
    starter_counts = conversation_starters.value_counts()
    ender_counts = conversation_enders.value_counts()

    df_sorted['DoubleMessage'] = (
            (df_sorted['Sender'] == df_sorted['Sender'].shift(1)) &
            (df_sorted['TimeDiff'] > double_message_time_threshold) &
            (df_sorted['Sender'] == df_sorted['Sender'].shift(-1))
    )
    df_sorted.loc[df_sorted.index[-1], 'DoubleMessage'] = False
    double_message_counts = df_sorted[df_sorted['DoubleMessage']]['Sender'].value_counts()

    df_sorted = df_sorted.dropna(subset=['TimeDiff'])
    df_sorted['IsResponse'] = df_sorted['Sender'] != df_sorted['Sender'].shift(1)
    df_sorted['IsImmediate'] = df_sorted['TimeDiff'] <= immediate_response_threshold
    immediate_response_counts = df_sorted[df_sorted['IsResponse']].groupby('Sender')['IsImmediate'].sum()
    total_response_counts = df_sorted[df_sorted['IsResponse']].groupby('Sender')['IsImmediate'].count()
    immediate_response_percentage = (immediate_response_counts / total_response_counts) * 100
    formatted_percentage = immediate_response_percentage.apply(lambda x: f"{x:.0f}%")

    conversation_stats_df = pd.DataFrame({
        'Started': starter_counts.round(0),
        'Ended': ender_counts.round(0),
        'Double Messages': double_message_counts.round(0),
        'Immediate Response (%)': formatted_percentage.round(0)
    })
    conversation_stats_df.fillna(0, inplace=True)

    # Define the phrases we are looking for
    apology_phrases = {"sorry", "please", "entschuldigung", "apologize", "my bad", "forgive", "pardon", "excuse"}
    encouragement_phrases = {"good job", "congratulation", "you will make it", "believe you", "believe in you",
                             "don't worry", "dont worry", "do not worry", "gut gemacht", "be fine", "will pass",
                             "well done", "keep it up", "you can do it", "proud of you", "great work"}

    # Define question words
    question_words = r'\b(?:who|what|when|where|why|how|which|whose|whom|warum)\b'

    # Combine phrases into patterns for searching
    apology_pattern = '|'.join(apology_phrases)
    encouragement_pattern = '|'.join(encouragement_phrases)

    # Search for apologies, encouragements, and questions
    df['Apologies'] = df['Message'].str.contains(apology_pattern, case=False, regex=True)
    df['Encouragements'] = df['Message'].str.contains(encouragement_pattern, case=False, regex=True)

    # Search for messages starting with a question word OR ending with a ?
    df['Questions'] = df['Message'].str.contains(question_words, case=False, regex=True) | df['Message'].str.contains(
        r'\w\?$', regex=True)

    # Aggregate results for each sender
    speech_acts_df = df.groupby('Sender').agg({
        'Questions': 'sum',
        'Apologies': 'sum',
        'Encouragements': 'sum'
    })


    combined_df = pd.concat([conversation_stats_df, speech_acts_df], axis=1)

    return combined_df.T  # Return the transposed DataFrame


def prepare_gemini_data(df):
    """Prepares the data dictionary for the Gemini API call, avoiding redundant calls."""

    data = {}

    # Store results of analysis functions to avoid redundant calls
    data["top_emoji"] = show_top10_emoji(df).to_json(orient="split")
    data["top_emoji_per_person"] = prepare_top_emoji_per_person_data(df)
    (
        data["messaging_time"],
        most_active_day,
        most_active_part,
    ) = analyze_messaging_time(df)
    data["messaging_time"] = data["messaging_time"].to_json(orient="split")
    data["text_stat_per_person"] = analyze_text_stats_per_person(df).to_json(
        orient="split"
    )
    data["monthly_message_chart"] = monthly_message_chart(df).T.to_json(
        orient="records"
    )
    data[
        "conversation_double_messages"
    ] = analyze_conversation_and_double_messages(df).to_json(orient="split")

    return data


def prepare_top_emoji_per_person_data(df):
    """Prepares the top emoji per person data for JSON serialization."""
    top_emoji_per_person_data = []
    for sender, df_emoji in show_top10_emoji_per_person(df).items():
        for _, row in df_emoji.iterrows():
            top_emoji_per_person_data.append(
                {"sender": sender, "emoji": row["Emoji"], "count": row["Count"]}
            )
    return json.dumps(top_emoji_per_person_data)


def gemini_chat_analysis(df):
    """Analyzes the WhatsApp chat data using the Gemini API."""
    """Performs the analysis and reports progress if callback is provided."""

    GOOGLE_API_KEY = "XXXXXXXXXXXXXXXXXXXX"  # Replace with your API key
    genai.configure(api_key=GOOGLE_API_KEY)

    # Prepare data for Gemini, only calling functions once
    data = prepare_gemini_data(df)

    # Construct the prompt for Gemini
    prompt = (
        "Can you do a relationship summary based on this JSON data?\n\n"
        "Here's a breakdown:\n\n"
        "**top_emoji:** {top_emoji}\n"
        "**top_emoji_per_person:** {top_emoji_per_person}\n"
        "**messaging_time:** {messaging_time}\n"
        "**text_stat_per_person:** {text_stat_per_person}\n"
        "**monthly_message_chart:** {monthly_message_chart}\n"
        "**conversation_double_messages:** {conversation_double_messages}\n\n"
        "Based on this information, provide insights into the relationship. Remember:\n"
        "* I don't need a 'Things to Consider' section.\n"
        "* Rate the relationship out of 10.\n"
        "* Carefully analyze which statistics belong to whom - don't mix them up.\n"
        "* Be gentle and avoid overly critical judgments."
    )

    # Format the prompt with the data
    formatted_prompt = prompt.format(**data)

    # Create and configure the Gemini model
    generation_config = {
        "temperature": 0.6,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="You are a relationship expert.",
    )

    # Start a chat and send the message to Gemini
    chat = model.start_chat(history=[])
    response = chat.send_message(formatted_prompt)

    return response.text


# # Example usage
# df = prepare_dataframe(file_path)
# analysis_result = gemini_chat_analysis(df)
# print(analysis_result)
