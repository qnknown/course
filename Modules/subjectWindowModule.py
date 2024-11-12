import pymysql
from PyQt5 import QtWidgets
from WindowFiles.subjectWindow import Ui_Subjects
from PyQt5.QtWidgets import QTableWidgetItem

class SubjectsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Subjects()
        self.ui.setupUi(self)
