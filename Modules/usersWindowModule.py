import pymysql
import globals
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from WindowFiles.usersWindow import Ui_usersWindow

class UsersWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        if self.check_root_access():
            self.setup_ui()
        else:
            self.show_access_denied_alert()

    def setup_ui(self):
        self.ui = Ui_usersWindow()
        self.ui.setupUi(self)

    def check_root_access(self):
        try:
            connection = pymysql.connect(
                host='127.0.0.1',
                user='root',
                password='root',
                port=3306,
                database='course'
            )
            with connection.cursor() as cursor:
                query = "SELECT access FROM `keys` WHERE username = %s"
                cursor.execute(query, (globals.username,))
                result = cursor.fetchone()
                return result and result[0] == "root"
        except pymysql.MySQLError as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        finally:
            if 'connection' in locals():
                connection.close()

    def show_access_denied_alert(self):
        alert = QMessageBox()
        alert.setWindowTitle("Access Denied")
        alert.setText("У вас немає прав доступу для відкриття цього вікна.")
        alert.setIcon(QMessageBox.Warning)
        alert.exec_()
