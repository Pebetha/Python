# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import dns
import pymongo
import Register
import Menu
from datetime import datetime


class Ui_OnlyFood(object):
    def setupUi(self, OnlyFood):
        OnlyFood.setObjectName("OnlyFood")
        OnlyFood.resize(400, 300)
        OnlyFood.setMaximumSize(QtCore.QSize(400, 300))
        self.but_Register = QtWidgets.QPushButton(OnlyFood)
        self.but_Register.setGeometry(QtCore.QRect(30, 240, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Register.setFont(font)
        self.but_Register.setObjectName("but_Register")
        self.but_Login = QtWidgets.QPushButton(OnlyFood)
        self.but_Login.setGeometry(QtCore.QRect(150, 240, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Login.setFont(font)
        self.but_Login.setObjectName("but_Login")
        self.lbl_Result = QtWidgets.QLabel(OnlyFood)
        self.lbl_Result.setGeometry(QtCore.QRect(270, 240, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Result.setFont(font)
        self.lbl_Result.setText("")
        self.lbl_Result.setObjectName("lbl_Result")
        self.lbl_OnlyFood = QtWidgets.QLabel(OnlyFood)
        self.lbl_OnlyFood.setGeometry(QtCore.QRect(140, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lbl_OnlyFood.setFont(font)
        self.lbl_OnlyFood.setStyleSheet("")
        self.lbl_OnlyFood.setObjectName("lbl_OnlyFood")
        self.lbl_Username = QtWidgets.QLabel(OnlyFood)
        self.lbl_Username.setGeometry(QtCore.QRect(50, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Username.setFont(font)
        self.lbl_Username.setObjectName("lbl_Username")
        self.lbl_Password = QtWidgets.QLabel(OnlyFood)
        self.lbl_Password.setGeometry(QtCore.QRect(50, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Password.setFont(font)
        self.lbl_Password.setObjectName("lbl_Password")
        self.txt_Username = QtWidgets.QTextEdit(OnlyFood)
        self.txt_Username.setGeometry(QtCore.QRect(180, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_Username.setFont(font)
        self.txt_Username.setObjectName("txt_Username")
        self.txt_Password = QtWidgets.QLineEdit(OnlyFood)
        self.txt_Password.setGeometry(QtCore.QRect(180, 140, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_Password.setFont(font)
        self.txt_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_Password.setObjectName("txt_Password")
        self.Background = QtWidgets.QFrame(OnlyFood)
        self.Background.setGeometry(QtCore.QRect(-10, -20, 411, 351))
        self.Background.setAutoFillBackground(False)
        self.Background.setStyleSheet(
            "border-image: url(:/newPrefix/???Pngtree???elemental background of fast food_981344.png);")
        self.Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background.setObjectName("Background")
        self.Background.raise_()
        self.but_Register.raise_()
        self.but_Login.raise_()
        self.lbl_Result.raise_()
        self.lbl_OnlyFood.raise_()
        self.lbl_Username.raise_()
        self.lbl_Password.raise_()
        self.txt_Username.raise_()
        self.txt_Password.raise_()

        self.retranslateUi(OnlyFood)
        QtCore.QMetaObject.connectSlotsByName(OnlyFood)
        # Event Driven
        self.but_Login.clicked.connect(self.show)
        self.but_Register.clicked.connect(self.open_Register)
        self.but_Register.clicked.connect(OnlyFood.close)

    def open_Register(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Register.Ui_Form_Register()
        self.ui.setupUi(self.window)
        self.window.show()

    def show(self):
        with pymongo.MongoClient(cloudDatabase) as conn:
            db = conn.get_database('myFirstDatabase')
            inputuname = self.txt_Username.toPlainText()
            inputpass = self.txt_Password.text()
            condition1 = {'username': inputuname}
            condition2 = {'password': inputpass}
            where = {'$and': [condition1, condition2]}
            found = db.users.count_documents(where)
            if found == 1:
                self.window = QtWidgets.QMainWindow()
                self.ui = Menu.Ui_Dialog()
                self.ui.setupUi(self.window)
                self.window.show()
                self.lbl_Result.setText(" ")
                OnlyFood.close()
            else:
                self.lbl_Result.setText("Not found")

    def retranslateUi(self, OnlyFood):
        _translate = QtCore.QCoreApplication.translate
        OnlyFood.setWindowTitle(_translate("OnlyFood", "OnlyFood"))
        self.but_Register.setText(_translate("OnlyFood", "Register"))
        self.but_Login.setText(_translate("OnlyFood", "Login"))
        self.lbl_OnlyFood.setText(_translate("OnlyFood", "OnlyFood"))
        self.lbl_Username.setText(_translate("OnlyFood", "Username"))
        self.lbl_Password.setText(_translate("OnlyFood", "Password"))


if __name__ == "__main__":
    import Picture
    import sys

    cloudDatabase = 'mongodb+srv://myAccount:peerapol1@cluster0.ws1ng.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    app = QtWidgets.QApplication(sys.argv)
    OnlyFood = QtWidgets.QDialog()
    ui = Ui_OnlyFood()
    ui.setupUi(OnlyFood)
    OnlyFood.show()
    sys.exit(app.exec_())
