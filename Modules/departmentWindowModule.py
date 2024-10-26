import pymysql
from PyQt5 import QtWidgets
from WindowFiles.departmentWindow import Ui_Department

class DepartmentWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Department()
        self.ui.setupUi(self)

