from functools import wraps
from PyQt5.QtWidgets import QMessageBox
import globals

class Validation:
    @staticmethod
    def check_access(user_access, required_access=("root", "Admin", "Operator")):
        return user_access in required_access

    @staticmethod
    def access_control(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            user_access = globals.user_access
            if not Validation.check_access(user_access):
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Access Denied")
                msg_box.setText("You do not have permission to perform this action.")
                msg_box.exec_()
                return
            return method(self, *args, **kwargs)
        return wrapper
