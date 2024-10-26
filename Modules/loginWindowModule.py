import pymysql
from PyQt5 import QtWidgets
from WindowFiles.loginWindow import Ui_loginWindow

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginWindow()
        self.ui.setupUi(self)

