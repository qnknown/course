import pymysql
from PyQt5 import QtWidgets
from WindowFiles.relationWindow import Ui_Relations
from PyQt5.QtWidgets import QTableWidgetItem

class RelationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Relations()
        self.ui.setupUi(self)
