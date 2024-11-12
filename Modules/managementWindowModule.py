import pymysql
from PyQt5 import QtWidgets
from WindowFiles.ManagementWindow import Ui_Management

class ManagementWindow(QtWidgets.QMainWindow):
    def __init__(self, username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = username
        self.ui = Ui_Management()
        self.ui.setupUi(self)
        self.set_user_info()

    def set_user_info(self):
        self.ui.label_4.setText(f"Ви увійшли як {self.username}")

    def has_root_access(self):
        connection = pymysql.connect(
            host="localhost",
            user="your_user",
            password="your_password",
            database="course"
        )
        try:
            with connection.cursor() as cursor:
                query = "SELECT access FROM keys WHERE username = %s"
                cursor.execute(query, (self.username,))
                result = cursor.fetchone()
                if result and result[0] == "root":
                    return True
                else:
                    return False
        finally:
            connection.close()