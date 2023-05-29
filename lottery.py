# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QLineEdit, QFileDialog, QDockWidget, QListWidget, QComboBox, QCheckBox
from PyQt5.QtCore import QDir, Qt, QUrl, QObject
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
import random


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 150, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 110, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(280, 210, 111, 20))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 90, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 40, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 190, 55, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 210, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "產生中獎號碼"))
        self.pushButton_2.setText(_translate("Form", "對樂透"))
        self.checkBox.setText(_translate("Form", "顯示樂透號碼"))
        self.label.setText(_translate("Form", "樂透號碼"))
        self.label_2.setText(_translate("Form", "中獎號碼"))
        self.label_3.setText(_translate("Form", "獎金"))

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Click)
        self.ui.pushButton_2.clicked.connect(self.Click2)
        self.ui.checkBox.stateChanged.connect(self.Change)
        pIntvalidator=QIntValidator(self)
        pIntvalidator.setRange(100,999)
        self.ui.lineEdit.setValidator(pIntvalidator)
        self.ui.lineEdit_2.setReadOnly(True)
        self.ui.lineEdit_3.setReadOnly(True)
        self.ui.lineEdit_2.hide()
        self.ui.label_2.hide()

    def Click(self):
        global A, B, C, D
        A = random.randint(1,9)
        A = int(A)
        list = [0,1,2,3,4,5,6,7,8,9]
        list.remove(A)
        B = random.sample(list, 1)
        B = str(B)
        B = B[1:len(B)-1]
        B = int(B)
        list.remove(B)
        C = random.sample(list, 1)
        C = str(C)
        C = C[1:len(C)-1]
        A = str(A)
        B = str(B)
        C = str(C)
        D = A+B+C
        print(D)
        self.ui.lineEdit_2.setText(D)
        
        

        



    def Click2(self):
        num = self.ui.lineEdit.text()
        if (self.ui.lineEdit_2.text() == ""):
            
            reply = QMessageBox.warning(self,"警告","請先產生樂透號碼！")
            return
        
        if (num == ""):
            
            reply = QMessageBox.warning(self,"警告","不可為空，請輸入！")
            return
        if (len(num) < 3):
            
            reply = QMessageBox.warning(self,"警告","請輸入三個數字！")
            return
        array = [0, 0, 0]
        array[0] = int(num[0])
        array[1] = int(num[1])
        array[2] = int(num[2])
        duplicated_array = set(array)
        if len(duplicated_array) != len(array):
            reply = QMessageBox.warning(self,"警告","請勿輸入重複的數字")
            return
        
        E = str(num[0])
        F = str(num[1])
        G = str(num[2])
        print(E+F+G)
        m = 0
        n = 0
        if E == A:
            m += 1
            n += 1
        pass
        if F == A:
            m += 0
            n += 1
        pass
        if G == A:
            m += 0
            n += 1
        pass
        if F == B:
            m += 1
            n += 1
        pass
        if E == B:
            m += 0
            n += 1
        pass
        if G == B:
            m += 0
            n += 1
        pass
        if G == C:
            m += 1
            n += 1
        pass
        if E == C:
            m += 0
            n += 1
        pass
        if F == C:
            m += 0
            n += 1
        pass

        if (m == 3):
            self.ui.lineEdit_3.setText('12000')
        pass
        if (m != 3 and n == 3):
            self.ui.lineEdit_3.setText('3600')
        pass
        if (n <= 2):
            self.ui.lineEdit_3.setText('1500')
        pass
        if (n == 0):
            self.ui.lineEdit_3.setText('0')
        pass

            


    def Change(self):
        if not self.ui.checkBox.isChecked():
            self.ui.lineEdit_2.hide()
            self.ui.label_2.hide()

        if  self.ui.checkBox.isChecked():
            self.ui.lineEdit_2.show()
            self.ui.label_2.show()
            




app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
