import pymysql
from PyQt5 import QtWidgets
from WindowFiles.specWindow import Ui_Specialties
from PyQt5.QtWidgets import QTableWidgetItem

class SpecWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Specialties()
        self.ui.setupUi(self)
