# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'syn_flood.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 531, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.runBotton = QtWidgets.QPushButton(self.frame)
        self.runBotton.setGeometry(QtCore.QRect(20, 340, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.runBotton.setFont(font)
        self.runBotton.setObjectName("runBotton")
        self.dstIP = QtWidgets.QLineEdit(self.frame)
        self.dstIP.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.dstIP.setObjectName("dstIP")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dstPort = QtWidgets.QLineEdit(self.frame)
        self.dstPort.setGeometry(QtCore.QRect(20, 120, 113, 20))
        self.dstPort.setObjectName("dstPort")
        self.treadsCount = QtWidgets.QLineEdit(self.frame)
        self.treadsCount.setGeometry(QtCore.QRect(20, 210, 113, 20))
        self.treadsCount.setObjectName("treadsCount")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.packetsCount = QtWidgets.QLabel(self.frame)
        self.packetsCount.setGeometry(QtCore.QRect(170, 250, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.packetsCount.setFont(font)
        self.packetsCount.setText("")
        self.packetsCount.setWordWrap(True)
        self.packetsCount.setObjectName("packetsCount")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
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
        self.runBotton.setText(_translate("MainWindow", "Начать атаку"))
        self.label.setText(_translate("MainWindow", "Введите IP"))
        self.label_2.setText(_translate("MainWindow", "Введите порт"))
        self.label_3.setText(_translate("MainWindow", "Введите количество потоков"))
        self.label_4.setText(_translate("MainWindow", "Количество пакетов отправлено"))
