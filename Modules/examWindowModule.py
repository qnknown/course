import pymysql
from PyQt5 import QtWidgets
from WindowFiles.examWindow import Ui_examWindow
from PyQt5.QtWidgets import QTableWidgetItem

class ExamWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_examWindow()
        self.ui.setupUi(self)



