import pymysql
from PyQt5 import QtWidgets
from WindowFiles.groupWindow import Ui_groupWindow
from PyQt5.QtWidgets import QTableWidgetItem

class GroupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_groupWindow()
        self.ui.setupUi(self)



