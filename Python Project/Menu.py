# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import dns
import pymongo
import Picture
import Login,Bread,Coffee,Coke,Donut,FishBurger,FrenchFries,HamSandwich,Hotdog,MeatBurger,ProkBurger,TunaSandwich,Water,Cart
from datetime import datetime

import datacollection


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 451)
        Dialog.setMaximumSize(QtCore.QSize(400, 451))
        self.lbl_Menu = QtWidgets.QLabel(Dialog)
        self.lbl_Menu.setGeometry(QtCore.QRect(170, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_Menu.setFont(font)
        self.lbl_Menu.setObjectName("lbl_Menu")
        self.but_Burger = QtWidgets.QPushButton(Dialog)
        self.but_Burger.setGeometry(QtCore.QRect(20, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Burger.setFont(font)
        self.but_Burger.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.but_Burger.setObjectName("but_Burger")
        self.but_PorkBurger = QtWidgets.QPushButton(Dialog)
        self.but_PorkBurger.setGeometry(QtCore.QRect(150, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_PorkBurger.setFont(font)
        self.but_PorkBurger.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.but_PorkBurger.setObjectName("but_PorkBurger")
        self.but_FishBurger = QtWidgets.QPushButton(Dialog)
        self.but_FishBurger.setGeometry(QtCore.QRect(280, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_FishBurger.setFont(font)
        self.but_FishBurger.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.but_FishBurger.setObjectName("but_FishBurger")
        self.but_French_fries = QtWidgets.QPushButton(Dialog)
        self.but_French_fries.setGeometry(QtCore.QRect(280, 140, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_French_fries.setFont(font)
        self.but_French_fries.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.but_French_fries.setObjectName("but_French_fries")
        self.but_Bread = QtWidgets.QPushButton(Dialog)
        self.but_Bread.setGeometry(QtCore.QRect(20, 140, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Bread.setFont(font)
        self.but_Bread.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.but_Bread.setObjectName("but_Bread")
        self.but_Hotdog = QtWidgets.QPushButton(Dialog)
        self.but_Hotdog.setGeometry(QtCore.QRect(150, 140, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Hotdog.setFont(font)
        self.but_Hotdog.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.but_Hotdog.setObjectName("but_Hotdog")
        self.but_Coffee = QtWidgets.QPushButton(Dialog)
        self.but_Coffee.setGeometry(QtCore.QRect(150, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Coffee.setFont(font)
        self.but_Coffee.setStyleSheet("background-color: rgb(164, 199, 255);")
        self.but_Coffee.setObjectName("but_Coffee")
        self.but_Sandwichham = QtWidgets.QPushButton(Dialog)
        self.but_Sandwichham.setGeometry(QtCore.QRect(20, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Sandwichham.setFont(font)
        self.but_Sandwichham.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.but_Sandwichham.setObjectName("but_Sandwichham")
        self.but_Water = QtWidgets.QPushButton(Dialog)
        self.but_Water.setGeometry(QtCore.QRect(20, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Water.setFont(font)
        self.but_Water.setStyleSheet("background-color: rgb(164, 199, 255);")
        self.but_Water.setObjectName("but_Water")
        self.but_Donut = QtWidgets.QPushButton(Dialog)
        self.but_Donut.setGeometry(QtCore.QRect(280, 210, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Donut.setFont(font)
        self.but_Donut.setStyleSheet("background-color: rgb(255, 181, 215);")
        self.but_Donut.setObjectName("but_Donut")
        self.but_TunaSanwich = QtWidgets.QPushButton(Dialog)
        self.but_TunaSanwich.setGeometry(QtCore.QRect(150, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_TunaSanwich.setFont(font)
        self.but_TunaSanwich.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.but_TunaSanwich.setObjectName("but_TunaSanwich")
        self.but_Coke = QtWidgets.QPushButton(Dialog)
        self.but_Coke.setGeometry(QtCore.QRect(280, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Coke.setFont(font)
        self.but_Coke.setStyleSheet("background-color: rgb(164, 199, 255);")
        self.but_Coke.setObjectName("but_Coke")
        self.but_Back = QtWidgets.QPushButton(Dialog)
        self.but_Back.setGeometry(QtCore.QRect(10, 400, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Back.setFont(font)
        self.but_Back.setObjectName("but_Back")
        self.but_Confirm = QtWidgets.QPushButton(Dialog)
        self.but_Confirm.setGeometry(QtCore.QRect(280, 400, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Confirm.setFont(font)
        self.but_Confirm.setStyleSheet("background-color: rgb(138, 255, 148);")
        self.but_Confirm.setObjectName("but_Confirm")
        self.lbl_Result = QtWidgets.QLabel(Dialog)
        self.lbl_Result.setGeometry(QtCore.QRect(140, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Result.setFont(font)
        self.lbl_Result.setText("{} Item in cart ".format(datacollection.countitem()))
        self.lbl_Result.setObjectName("lbl_Result")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, -150, 441, 701))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/—Pngtree—elemental background of fast food_981344.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.lbl_Menu.raise_()
        self.but_Burger.raise_()
        self.but_PorkBurger.raise_()
        self.but_FishBurger.raise_()
        self.but_French_fries.raise_()
        self.but_Bread.raise_()
        self.but_Hotdog.raise_()
        self.but_Coffee.raise_()
        self.but_Sandwichham.raise_()
        self.but_Water.raise_()
        self.but_Donut.raise_()
        self.but_TunaSanwich.raise_()
        self.but_Coke.raise_()
        self.but_Back.raise_()
        self.but_Confirm.raise_()
        self.lbl_Result.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.but_Back.clicked.connect(self.Back_Menu)
        self.but_Back.clicked.connect(Dialog.close)
        self.but_Confirm.clicked.connect(self.Cart)
        self.but_Confirm.clicked.connect(Dialog.close)

        self.but_Bread.clicked.connect(self.open_Bread)
        self.but_Bread.clicked.connect(Dialog.close)

        self.but_Coffee.clicked.connect(self.open_Coffee)
        self.but_Coffee.clicked.connect(Dialog.close)

        self.but_Coke.clicked.connect(self.open_Coke)
        self.but_Coke.clicked.connect(Dialog.close)

        self.but_Donut.clicked.connect(self.open_Donut)
        self.but_Donut.clicked.connect(Dialog.close)

        self.but_FishBurger.clicked.connect(self.open_FishBurger)
        self.but_FishBurger.clicked.connect(Dialog.close)

        self.but_French_fries.clicked.connect(self.open_FrenchFries)
        self.but_French_fries.clicked.connect(Dialog.close)

        self.but_Sandwichham.clicked.connect(self.open_HamSandwich)
        self.but_Sandwichham.clicked.connect(Dialog.close)

        self.but_Hotdog.clicked.connect(self.open_Hotdog)
        self.but_Hotdog.clicked.connect(Dialog.close)

        self.but_Burger.clicked.connect(self.open_MeatBurger)
        self.but_Burger.clicked.connect(Dialog.close)

        self.but_PorkBurger.clicked.connect(self.open_PorkBurger)
        self.but_PorkBurger.clicked.connect(Dialog.close)

        self.but_TunaSanwich.clicked.connect(self.open_TunaSandwich)
        self.but_TunaSanwich.clicked.connect(Dialog.close)

        self.but_Water.clicked.connect(self.open_Water)
        self.but_Water.clicked.connect(Dialog.close)

        #self.lbl_Result.setText(self.Count)

    def open_Bread(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Bread.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_Coffee(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Coffee.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_Coke(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Coke.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_Donut(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Donut.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_FishBurger(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = FishBurger.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_FrenchFries(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = FrenchFries.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_HamSandwich(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = HamSandwich.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_Hotdog(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Hotdog.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_MeatBurger(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MeatBurger.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_PorkBurger(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ProkBurger.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_TunaSandwich(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = TunaSandwich.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_Water(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Water.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def Back_Menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Login.Ui_OnlyFood()
        self.ui.setupUi(self.window)
        self.window.show()

    def Cart(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Cart.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "OnlyFood"))
        self.lbl_Menu.setText(_translate("Dialog", "MENU"))
        self.but_Burger.setText(_translate("Dialog", "MeatBurger"))
        self.but_PorkBurger.setText(_translate("Dialog", "PorkBurger"))
        self.but_FishBurger.setText(_translate("Dialog", "FishBurger"))
        self.but_French_fries.setText(_translate("Dialog", "FrenchFries"))
        self.but_Bread.setText(_translate("Dialog", "Bread"))
        self.but_Hotdog.setText(_translate("Dialog", "Hotdog"))
        self.but_Coffee.setText(_translate("Dialog", "Coffee"))
        self.but_Sandwichham.setText(_translate("Dialog", "HamSandwich"))
        self.but_Water.setText(_translate("Dialog", "Water"))
        self.but_Donut.setText(_translate("Dialog", "Donut"))
        self.but_TunaSanwich.setText(_translate("Dialog", "TunaSandwich"))
        self.but_Coke.setText(_translate("Dialog", "Coke"))
        self.but_Back.setText(_translate("Dialog", "Back"))
        self.but_Confirm.setText(_translate("Dialog", "Confirm"))



if __name__ == "__main__":
    import sys

    cloudDatabase = 'mongodb+srv://myAccount:peerapol1@cluster0.ws1ng.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
