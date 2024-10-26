import pymysql
from PyQt5 import QtWidgets
from WindowFiles.applicantsWindow import Ui_Applicants
from PyQt5.QtWidgets import QTableWidgetItem

class ApplicantsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Applicants()
        self.ui.setupUi(self)



