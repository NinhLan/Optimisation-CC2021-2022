# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import BigM_NINH_ITS2 as bigm
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 786)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 661, 391))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 61))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 490, 651, 181))
        self.textBrowser.setObjectName("textBrowser")
        (z, x) = bigm.simplex('min', np.array([[1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]),
                        np.array([[400], [300], [200], [300]]),
                        np.array([[30], [25], [36], [30]]),
                        np.array([[1], [1], [0], [0]]),
                  10000)
        Z=str(z)
        X=str(x)
        a=(str('point optimal actuel: ')+X+str('\nZ = ')+Z)
        
        self.textBrowser.setText(a)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 26))
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
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">A partir du sujet on a donc la résolution suivent </span></p><p><span style=\" font-weight:600;\">On a</span></p><p><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">x</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">1</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> est le nombre de voiture que l\'usine1 envoir à client1</span></p><p><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">x</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">1</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> est le nombre de voiture que l\'usine1 envoir à client2</span></p><p><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">x</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">1</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> est le nombre de voiture que l\'usine2 envoir à client1</span></p><p><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">x</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">1</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> est le nombre de voiture que l\'usine2 envoir à client2</span></p><p><span style=\" font-weight:600;\">On a un problème minimisation à la forme : </span></p><p>Z = 30x<span style=\" vertical-align:sub;\">1 </span>+ 25x<span style=\" vertical-align:sub;\">2</span> + 36x<span style=\" vertical-align:sub;\">3</span> +30x<span style=\" vertical-align:sub;\">4</span></p><p><span style=\" font-weight:600;\">Avec les sous contraintes : </span></p><p><img src=\"file:///C:/Users/ninht/AppData/Local/Temp/msohtmlclip1/01/clip_image012.png\" width=\"189\" height=\"70\"/></p><p/><p>Grâce au programme BigM on peut trouver la solution souvent : A partir du sujet on a donc la résolution suivent </p><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Question 3</span></p></body></html>"))

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow.show()
    sys.exit(app.quit())

