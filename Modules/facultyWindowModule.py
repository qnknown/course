import pymysql
from PyQt5 import QtWidgets
from WindowFiles.facultyWindow import Ui_FacultyWindow
from PyQt5.QtWidgets import QTableWidgetItem

class FacultyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FacultyWindow()
        self.ui.setupUi(self)



