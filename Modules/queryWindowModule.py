import pymysql
from PyQt5 import QtWidgets
from WindowFiles.queryWindow import Ui_Query
from PyQt5.QtWidgets import QTableWidgetItem

class QueryWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Query()
        self.ui.setupUi(self)
