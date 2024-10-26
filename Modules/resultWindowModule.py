import pymysql
from PyQt5 import QtWidgets
from WindowFiles.resultWindow import Ui_resultWindow
from PyQt5.QtWidgets import QTableWidgetItem

class ResultWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_resultWindow()
        self.ui.setupUi(self)



