# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'examWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Services.login_logic import DatabaseConnection
from Services.examService import Exams

class Ui_examWindow(object):
    def setupUi(self, resultWindow):
        resultWindow.setObjectName("resultWindow")
        resultWindow.resize(1920, 1080)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/symvolika-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        resultWindow.setWindowIcon(icon)
        resultWindow.setStyleSheet("background: #5472DE;\n"
"background-image: url(:/newPrefix/649eb8ca76c20 (1).png);")
        self.centralwidget = QtWidgets.QWidget(resultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 50, 741, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background: transparent;")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(1290, 690, 251, 51))
        self.pushButton_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(1290, 450, 251, 51))
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 240, 271, 51))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(1290, 310, 251, 51))
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(1580, 310, 251, 51))
        self.pushButton_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1270, 210, 281, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("background: transparent;")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.comboBox_8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_8.setGeometry(QtCore.QRect(1290, 380, 251, 51))
        self.comboBox_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_8.setObjectName("comboBox_8")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(90, 310, 1161, 691))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setWordWrap(False)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(980, 240, 271, 51))
        self.pushButton_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1290, 430, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1290, 360, 61, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(1290, 520, 251, 51))
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1290, 500, 61, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(1290, 590, 251, 51))
        self.comboBox_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1290, 570, 141, 16))
        self.label_5.setObjectName("label_5")
        resultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(resultWindow)
        QtCore.QMetaObject.connectSlotsByName(resultWindow)

        self.connection = DatabaseConnection.get_connection()

        self.exams = Exams(self.connection)
        self.exams.load_data_to_tablewidget(self.tableWidget_2)

        self.lineEdit_6.textChanged.connect(self.search)

        self.pushButton_16.clicked.connect(self.save_data)
        self.pushButton_17.clicked.connect(self.delete_record)
        self.pushButton_18.clicked.connect(self.update_data)
        self.exams.load_combobox_data(self.comboBox_5, self.comboBox_8, self.comboBox_4, self.comboBox_6)

    def search(self):
        keyword = self.lineEdit_6.text()
        self.exams.search_data(keyword, self.tableWidget_2)

    def delete_record(self):
        self.exams.delete_selected_record(self.tableWidget_2)

    def save_data(self):
        if self.connection is None:
            print("З'єднання з базою даних не встановлене.")
            return

        name = self.lineEdit_16.text()
        subject_1 = self.comboBox_8.currentData()
        subject_2 = self.comboBox_4.currentData()
        subject_3 = self.comboBox_5.currentData()
        is_creative = self.comboBox_6.currentData()

        if not name:
            QtWidgets.QMessageBox.warning(None, "Помилка", "Всі поля мають бути заповнені.")
            return

        self.exams.save_data(name, subject_1, subject_2, subject_3, is_creative)
        self.exams.load_data_to_tablewidget(self.tableWidget_2)

    def update_data(self):
        self.exams.update_data(self.tableWidget_2)

    def retranslateUi(self, resultWindow):
        _translate = QtCore.QCoreApplication.translate
        resultWindow.setWindowTitle(_translate("resultWindow", "Керування БД"))
        self.label_3.setText(_translate("resultWindow", "Набори екзаменів"))
        self.pushButton_16.setText(_translate("resultWindow", "Додати"))
        self.lineEdit_6.setPlaceholderText(_translate("resultWindow", "Пошук по ключовому слову"))
        self.lineEdit_16.setPlaceholderText(_translate("resultWindow", "Назва"))
        self.pushButton_17.setText(_translate("resultWindow", "Видалити вибраний запис"))
        self.label_9.setText(_translate("resultWindow", "Додати набір"))
        self.tableWidget_2.setSortingEnabled(True)
        self.pushButton_18.setText(_translate("resultWindow", "Зберегти зміни"))
        self.label.setText(_translate("resultWindow", "Предмет 2"))
        self.label_2.setText(_translate("resultWindow", "Предмет 1"))
        self.label_4.setText(_translate("resultWindow", "Предмет 3"))
        self.label_5.setText(_translate("resultWindow", "Чи є творчим конкурсом"))
import WindowFiles.img.image_rc
