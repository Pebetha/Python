# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HamSandwich.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import pymongo
from PyQt5 import QtCore, QtGui, QtWidgets
import Menu
import datacollection


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.lbl_HamSandwich = QtWidgets.QLabel(Dialog)
        self.lbl_HamSandwich.setGeometry(QtCore.QRect(150, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_HamSandwich.setFont(font)
        self.lbl_HamSandwich.setObjectName("lbl_HamSandwich")
        self.but_AddtoCart = QtWidgets.QPushButton(Dialog)
        self.but_AddtoCart.setGeometry(QtCore.QRect(290, 250, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_AddtoCart.setFont(font)
        self.but_AddtoCart.setStyleSheet("background-color: rgb(138, 255, 148);")
        self.but_AddtoCart.setObjectName("but_AddtoCart")
        self.but_Back = QtWidgets.QPushButton(Dialog)
        self.but_Back.setGeometry(QtCore.QRect(10, 250, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.but_Back.setFont(font)
        self.but_Back.setObjectName("but_Back")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 80, 201, 141))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/hamasandwich.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_HamSandwich_de = QtWidgets.QLabel(Dialog)
        self.lbl_HamSandwich_de.setGeometry(QtCore.QRect(260, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_HamSandwich_de.setFont(font)
        self.lbl_HamSandwich_de.setObjectName("lbl_HamSandwich_de")
        self.lbl_Price = QtWidgets.QLabel(Dialog)
        self.lbl_Price.setGeometry(QtCore.QRect(250, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Price.setFont(font)
        self.lbl_Price.setObjectName("lbl_Price")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(-50, -80, 461, 441))
        self.frame_2.setMaximumSize(QtCore.QSize(461, 441))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/—Pngtree—elemental background of fast food_981344.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.lbl_HamSandwich.raise_()
        self.but_AddtoCart.raise_()
        self.but_Back.raise_()
        self.frame.raise_()
        self.lbl_HamSandwich_de.raise_()
        self.lbl_Price.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.but_Back.clicked.connect(self.Back_Menu)
        self.but_Back.clicked.connect(Dialog.close)

        self.but_AddtoCart.clicked.connect(self.Add_Cart)
        self.but_AddtoCart.clicked.connect(self.Back_Menu)
        self.but_AddtoCart.clicked.connect(Dialog.close)

    def Back_Menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Menu.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def Add_Cart(self):
        cloudDatabase = 'mongodb+srv://myAccount:peerapol1@cluster0.ws1ng.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
        with pymongo.MongoClient(cloudDatabase) as conn:
            db = conn.get_database('myFirstDatabase')
            foodname = 'HamSandwich'
            cursor = {'menuname': foodname }
            findfood = db.Menu.find(cursor)
            check = True
            for i in findfood:
                name = i['menuname']
                price = i['price']

            if len(datacollection.cart) == 0:
                datacollection.cart.append([name, price,1])

            else:
                for i in range(len(datacollection.cart)):
                    if datacollection.cart[i][0] == name:
                        check = False
                        datacollection.cart[i][2] = datacollection.cart[i][2] + 1
                        break
                if check == True:
                    datacollection.cart.append([name, price,1])

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "OnlyFood"))
        self.lbl_HamSandwich.setText(_translate("Dialog", "HamSandwich"))
        self.but_AddtoCart.setText(_translate("Dialog", "Add to Cart"))
        self.but_Back.setText(_translate("Dialog", "Back"))
        self.lbl_HamSandwich_de.setText(_translate("Dialog", "HamSandwich"))
        self.lbl_Price.setText(_translate("Dialog", "Price : 35 Bath"))
import Picture


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
