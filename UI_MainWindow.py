# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 450)
        MainWindow.setMinimumSize(QtCore.QSize(900, 450))
        MainWindow.setMaximumSize(QtCore.QSize(900, 450))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.coffeeTable = QtWidgets.QTableView(parent=self.centralwidget)
        self.coffeeTable.setGeometry(QtCore.QRect(0, 0, 901, 351))
        self.coffeeTable.setObjectName("coffeeTable")
        self.editButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(730, 390, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.editButton.setFont(font)
        self.editButton.setObjectName("editButton")
        self.addButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(730, 360, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.editButton.setText(_translate("MainWindow", "Редактировать"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
