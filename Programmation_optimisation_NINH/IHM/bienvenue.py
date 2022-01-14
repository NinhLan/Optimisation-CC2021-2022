# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetre1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# import BigM_NINH_ITS2 as bigm
import exemple
import numpy as np
import subprocess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 20, 341, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 190, 361, 141))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 291, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(140, 80, 61, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(580, 190, 361, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(60, 30, 231, 16))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(30, 80, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 80, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(290, 80, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 370, 221, 51))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.commencer)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 440, 221, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_2.clicked.connect(self.exemple)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bienvenue!"))
        self.groupBox.setTitle(_translate("MainWindow", "Choisir type de problème"))
        self.label_2.setText(_translate("MainWindow", "Veuillez choisi le type de problème (max ou min) :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "max"))
        self.comboBox.setItemText(1, _translate("MainWindow", "min"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Choisir type de contraintes"))
        self.label_3.setText(_translate("MainWindow", "Veuillez choisir les types de contraintes"))
        self.checkBox.setText(_translate("MainWindow", "≥"))
        self.checkBox_2.setText(_translate("MainWindow", "≥"))
        self.checkBox_3.setText(_translate("MainWindow", "≥"))
        self.pushButton.setText(_translate("MainWindow", "Commencer"))
        self.pushButton_2.setText(_translate("MainWindow", "Exemple"))

    def commencer(self):
        # print('a')
        
        cmd = 'BigM_NINH_ITS2.py'
        
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate() 
        result = out.split('\n')
        for lin in result:
            if not lin.startswith('#'):
                print(lin)


        # execfile("BigM_NINH_ITS2.py")
    def exemple(self):
        ex.show()
                

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ex = exemple.MainWindow
# bigm=BingM_NINH_ITS2.show()
ui.setupUi(MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow.show()
    sys.exit(app.quit())

