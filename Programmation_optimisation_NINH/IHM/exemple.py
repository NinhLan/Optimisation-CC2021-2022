# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exemple.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import question1
import question2
import question3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1227, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 40, 341, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 451, 31))
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 180, 1161, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(120, 40, 911, 221))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(280, 40, 591, 211))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(100, 30, 971, 251))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 550, 161, 51))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.question1)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 550, 161, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_2.clicked.connect(self.question2)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(960, 550, 161, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_3.clicked.connect(self.question3)
        
        # self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_4.setGeometry(QtCore.QRect(30, 10, 93, 28))
        # self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1227, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bienvenue!"))
        self.label_2.setText(_translate("MainWindow", "Veuillez voir les sujets ci-dessous et choisissez un exemple que vous voulez"))
        self.label_3.setText(_translate("MainWindow", "Question 1 :\n"
"Un fabricant produit trois types d\'accessoires en plastique. Le temps nécessaire au moulage, à la découpe et à l\'emballage est indiqué dans le Tableau 1. \n"
"(Les temps sont indiqués en heures par douzaine d\'accessoires).\n"
"\n"
"Tableau 1: Coûts et profits associés à la production de produits en plastique.\n"
"\n"
"Procédure / Produit    Type A    Type B    Type C    Temps total disponible\n"
"Moulage    1    2    3/2    12.000,00\n"
"Découpage    2/3    2/3    1    4.600,00\n"
"Emballage    1/2    1/3    1/2    2.400,00\n"
"Profit    11 €    16 €    15 €    \n"
"\n"
"Combien de douzaines de chaque type d\'accessoire doivent être produites pour obtenir un profit maximal ?\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Question1"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Une petite compagnie pétrolière possède deux raffineries. La raffinerie 1 coûte 20 000 dollars par jour </p><p>et peut produire chaque jour 400 barils de pétrole de qualité supérieure, 300 barils de pétrole de</p><p>qualité moyenne et 200 barils de pétrole de qualité inférieure. La raffinerie 2 est plus récente et </p><p>plus moderne. Son coût d\'exploitation est de 25 000 dollars par jour et elle peut produire chaque</p><p>jour 300 barils de pétrole de qualité supérieure, 400 barils de pétrole de qualité moyenne et 500</p><p>barils de pétrole de qualité inférieure.</p><p/><p>L\'entreprise a des commandes totalisant 25000 barils de pétrole de qualité supérieure, 27000 barils</p><p>de pétrole de qualité moyenne et 30000 barils de pétrole de qualité inférieure. Combien de jours</p><p>doit-elle faire fonctionner chaque raffinerie pour minimiser ses coûts tout en raffinant suffisamment</p><p>de pétrole pour honorer ses commandes ? </p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Question2"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Une entreprise automobile possède deux usines. Une usine a 400 voitures (d\'un certain modèle) en stock et l\'autre usine a 300 voitures (du même modèle) en stock.</p><p> Deux clients commandent ce modèle de voiture. Le premier client a besoin de 200 voitures, et le second de 300 voitures. Le coût de l\'expédition des voitures</p><p>des deux usines aux clients est indiqué dans le Tableau 2. </p><p><span style=\" font-size:11.5pt;\"/></p><p align=\"center\"><span style=\" font-size:9pt; font-style:italic; color:#44546a;\">Tableau 2 : Coûts d\'expédition de véhicules.</span></p><p align=\"center\"><span style=\" font-style:italic;\"/></p><table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"0\"><tr><td width=\"121\" rowspan=\"2\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\"/></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Usine 1</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Usine 2</span></p></td><td width=\"134\" style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Client 1     Client 2</span></p></td></tr><tr><td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\"><p align=\"center\"><span style=\" font-size:12pt;\">30 €          25 €</span></p><p align=\"center\"><span style=\" font-size:12pt;\">36 €          30 €</span></p></td></tr></table><p align=\"center\"><span style=\" font-style:italic;\"/></p><p>Comment l\'entreprise doit-elle expédier les voitures afin de minimiser les frais d\'expédition ? </p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Question3"))
        self.pushButton.setText(_translate("MainWindow", "Question1"))
        self.pushButton_2.setText(_translate("MainWindow", "Question2"))
        self.pushButton_3.setText(_translate("MainWindow", "Question3"))
        # self.pushButton_4.setText(_translate("MainWindow", "Retourner"))
    def question1(self):
        q1.show()
    def question2(self):
        q2.show()
    def question3(self):
        q3.show()
        
            

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
q1=question1.MainWindow
q2=question2.MainWindow
q3=question3.MainWindow
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.quit())

