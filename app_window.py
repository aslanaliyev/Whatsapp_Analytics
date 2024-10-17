import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QFileDialog, QGraphicsDropShadowEffect, QMessageBox
from PySide6.QtGui import QFont
from PySide6 import QtCore
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread, Signal)
from PySide6.QtUiTools import QUiLoader
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from time import sleep
import seaborn as sns
import matplotlib.pyplot as plt
from ui_splash_screen import Ui_SplashScreen
from data_analysis import *  # Import all functions from data_analysis.py
from ui_main import Ui_MainWindow
from opening import Ui_MainWindow_opening

counter = 0


# Main Window Class (Initial Window)
class MainWindow(QMainWindow, Ui_MainWindow_opening):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Whatsapp Analytics')

        self.file_path = None
        self.pushButton.clicked.connect(self.open_file)

    def open_file(self):
        """Opens file dialog, loads data, and starts the splash screen."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open WhatsApp Chat Export", "", "Text Files (*.txt)"
        )

        if file_path:
            try:
                self.file_path = file_path
                df = prepare_dataframe(file_path)
                self.hide()
                self.splash_screen = SplashScreen(df)

            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to load file:\n{str(e)}")
        else:
            pass  # Handle file dialog cancel

# Main Application Window Class
class MainWindowApp(QMainWindow, Ui_MainWindow):
    def __init__(self, df):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Whatsapp Analytics')
        self.df = df

        # Call functions to populate tables and setup UI
        self.populate_tables()
        self.showMaximized()

        # Set up Matplotlib figures and canvases
        self.figure_m_time = Figure()
        self.canvas_m_time = FigureCanvas(self.figure_m_time)
        self.figure_m_message_volume = Figure()
        self.canvas_m_message_volume = FigureCanvas(self.figure_m_message_volume)

        # Get layouts and add canvases
        layout = self.verticalLayout_15
        layout_2 = self.horizontalLayout_3
        layout.addWidget(self.canvas_m_time)
        layout_2.addWidget(self.canvas_m_message_volume)

        # Display visualizations
        self.display_messaging_time_heatmap()
        self.display_conversation_stats()
        self.display_monthly_message_volume()


        # Displays the result from the Gemini
        self.Gemini_Text.setText(gemini_chat_analysis(df))


    def populate_tables(self):
        """Populates all tables with data from the analysis."""
        top_emojis_dataframes = show_top10_emoji_per_person(self.df)
        senders = list(top_emojis_dataframes.keys())

        self.populate_table(self.tableWidget, show_top10_emoji(self.df))

        self.populate_table(self.tableWidget_2, top_emojis_dataframes[senders[0]])
        self.label_3.setText(f"{senders[0]}:")

        self.populate_table(self.tableWidget_3, top_emojis_dataframes[senders[1]])
        self.label_4.setText(f"{senders[1]}:")

        text_stats_df = analyze_text_stats_per_person(self.df)
        self.populate_table_text_stats(self.tableWidget_4, text_stats_df)

        start_date, end_date = get_chat_date_range(self.df)
        self.label_title.setText(f"Whatsapp Analytics from {start_date} to {end_date}")

    def populate_table(self, table_widget, df_emoji):
        """Populates a QTableWidget with emoji data."""
        table_widget.setRowCount(len(df_emoji))
        for row, (emoji, count) in enumerate(df_emoji.itertuples(index=False)):
            emoji_item = QTableWidgetItem(emoji)
            count_item = QTableWidgetItem(str(count))
            emoji_item.setFont(QFont("Arial", 11))
            count_item.setFont(QFont("Arial", 11))
            table_widget.setItem(row, 0, emoji_item)
            table_widget.setItem(row, 1, count_item)
        table_widget.resizeColumnsToContents()
        table_widget.verticalHeader().setDefaultSectionSize(10)

    def populate_table_text_stats(self, table_widget, df_stats):
        """Populates a QTableWidget with text stats data."""
        table_widget.setRowCount(len(df_stats))
        table_widget.setColumnCount(len(df_stats.columns))
        table_widget.setHorizontalHeaderLabels(df_stats.columns)
        for row, stat_name in enumerate(df_stats.index):
            stat_item = QTableWidgetItem(stat_name)
            stat_item.setFont(QFont("Arial", 11))
            table_widget.setItem(row, 0, stat_item)
            for col, sender in enumerate(df_stats.columns):
                value = df_stats.loc[stat_name, sender]
                value_item = QTableWidgetItem(str(value))
                table_widget.setItem(row, col, value_item)
        table_widget.resizeColumnsToContents()
        table_widget.verticalHeader().setDefaultSectionSize(10)

    def display_conversation_stats(self):
        """Analyzes and displays conversation statistics."""
        conversation_stats_df = analyze_conversation_and_double_messages(self.df)
        self.populate_table_text_stats(self.tableWidget_5, conversation_stats_df)
        self.tableWidget_5.setHorizontalHeaderLabels(conversation_stats_df.columns)

    def display_messaging_time_heatmap(self):
        """Creates and displays the messaging time heatmap."""
        message_counts, most_active_day, most_active_part = analyze_messaging_time(self.df)
        self.label_6.setText(
            f"The majority of the conversation was happening:<br> {most_active_day} - {most_active_part}")

        plt.figure(figsize=(1, 1))
        ax = self.figure_m_time.add_subplot(111)

        self.figure_m_time.patch.set_facecolor((42 / 255, 47 / 255, 108 / 255))
        ax.set_facecolor((42 / 255, 47 / 255, 108 / 255))
        sns.heatmap(message_counts.transpose(), annot=True, fmt="d", cmap="Oranges", cbar=False,
                    annot_kws={"size": 7}, ax=ax)

        ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=7)
        ax.set_xticklabels(ax.get_xticklabels(), fontsize=7)
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        pos = ax.get_position()
        ax.set_position([pos.x0 + 0.09, pos.y0, pos.width, pos.height])

        plt.tight_layout()
        self.canvas_m_time.draw()

    def display_monthly_message_volume(self):
        """Creates and displays the monthly message volume area chart."""
        message_counts_by_month = monthly_message_chart(self.df)
        ax = self.figure_m_message_volume.add_subplot(111)
        message_counts_by_month.plot.area(stacked=True, ax=ax)

        self.figure_m_message_volume.patch.set_facecolor((42 / 255, 47 / 255, 108 / 255))
        ax.set_facecolor((42 / 255, 47 / 255, 108 / 255))

        ax.set_title('Monthly Message Volume', fontsize=7)
        ax.set_ylabel('Message Count', fontsize=7)
        ax.tick_params(axis='x', colors='white', labelsize=7)
        ax.tick_params(axis='y', colors='white', labelsize=7)
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        pos = ax.get_position()
        ax.set_position([pos.x0 + 0.00, pos.y0 + 0.00, pos.width, pos.height])

        legend = ax.get_legend()
        if legend:
            frame = legend.get_frame()
            frame.set_facecolor((42 / 255, 47 / 255, 108 / 255))
            for text in legend.get_texts():
                text.set_color('white')
                text.set_fontsize(7)
            legend.set_title("")
            frame.set_linewidth(0)

        self.canvas_m_message_volume.draw()


class SplashScreen(QMainWindow):
    def __init__(self, df):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.df = df

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # CLOSE SPLASH SCREEN
            self.close()

            # SHOW MAIN WINDOW
            self.main = MainWindowApp(self.df)
            self.main.show()



        # INCREASE COUNTER
        counter += 1




# Main Application Execution
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())