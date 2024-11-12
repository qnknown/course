import sys
from PyQt5 import QtWidgets

from WindowFiles.MainWindow import Ui_MainWindow
from Modules.orderWindowModule import orderWindow
from Modules.loginWindowModule import LoginWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_order_window)
        self.ui.pushButton_2.clicked.connect(self.open_login_window)

    def open_order_window(self):
        self.order_window = orderWindow()
        self.order_window.show()

    def open_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
