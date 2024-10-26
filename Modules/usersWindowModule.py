import pymysql
from PyQt5 import QtWidgets
from WindowFiles.usersWindow import Ui_usersWindow
from PyQt5.QtWidgets import QTableWidgetItem

class UsersWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_usersWindow()
        self.ui.setupUi(self)



