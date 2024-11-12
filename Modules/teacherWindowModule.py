import pymysql
from PyQt5 import QtWidgets
from WindowFiles.teacherWindow import Ui_Teachers
from PyQt5.QtWidgets import QTableWidgetItem

class TeachersWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Teachers()
        self.ui.setupUi(self)
