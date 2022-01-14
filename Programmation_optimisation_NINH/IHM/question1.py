# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Simplexe_NINH_ITS2 as spl
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 70, 711, 381))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(130, 440, 501, 71))
        self.textBrowser.setObjectName("textBrowser")
        
        m = spl.gen_matrix(3,3)
        spl.constrain(m,'1,2,1.5,<=,12000')
        spl.constrain(m,'1.5,1.5,1,<=,4600')
        spl.constrain(m,'1.5,1.5,0.5,<=,2400')
        spl.obj(m,'11,16,15')
        a=str(spl.maxz(m))
        self.textBrowser.setText(a)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 26))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Question 1</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">A partir du sujet on a donc la résolution suivent </span></p><p><span style=\" font-weight:600;\">On a :</span></p><p>x<span style=\" vertical-align:sub;\">1 </span>est le produit type A</p><p>x<span style=\" vertical-align:sub;\">2 </span>est le produit type B</p><p><span style=\" font-weight:600;\">On a un problème maximisation à la forme : </span></p><p><span style=\" font-weight:600;\">Z = 11x</span><span style=\" font-weight:600; vertical-align:sub;\">1</span><span style=\" font-weight:600;\"> + 16x</span><span style=\" font-weight:600; vertical-align:sub;\">2</span><span style=\" font-weight:600;\"> + 15x</span><span style=\" font-weight:600; vertical-align:sub;\">3</span></p><p><span style=\" font-weight:600;\">Avec les sous contraintes : </span></p><p><img src=\"file:///C:/Users/ninht/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png\" width=\"184\" height=\"106\"/></p><p><span style=\" font-weight:600; text-decoration: underline;\">On obtient la solution suivent:</span></p></body></html>"))

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.quit())

