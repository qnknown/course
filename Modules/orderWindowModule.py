# orderWindowModule.py
import pymysql
from PyQt5 import QtWidgets
from WindowFiles.orderWindow import Ui_orderWindow

class orderWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_orderWindow()
        self.ui.setupUi(self)

        # Connect to the database
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            port=3306,
            database="course",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.Cursor
        )

        # Передача з'єднання до Ui_orderWindow
        self.ui.set_connection(self.connection)

        # Load data into the combo boxes
        self.ui.load_combobox_data(self.connection)


    def closeEvent(self, event):
        # Close the database connection when the application is closed
        self.connection.close()
        event.accept()


