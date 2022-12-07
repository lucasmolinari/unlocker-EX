# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 303)
        MainWindow.setStyleSheet("background: rgb(85, 170, 127)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(530, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.buttonSave.setFont(font)
        self.buttonSave.setStyleSheet("background-color: white")
        self.buttonSave.setObjectName("buttonSave")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-2, 70, 611, 20))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 9, 92, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("center: true")
        self.label.setObjectName("label")
        self.inputOpenFile = QtWidgets.QLineEdit(self.centralwidget)
        self.inputOpenFile.setGeometry(QtCore.QRect(10, 40, 501, 23))
        self.inputOpenFile.setStyleSheet("background-color: white")
        self.inputOpenFile.setReadOnly(True)
        self.inputOpenFile.setObjectName("inputOpenFile")
        self.buttonChooseFile = QtWidgets.QPushButton(self.centralwidget)
        self.buttonChooseFile.setGeometry(QtCore.QRect(530, 40, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.buttonChooseFile.setFont(font)
        self.buttonChooseFile.setStyleSheet("background-color: white\n"
"")
        self.buttonChooseFile.setObjectName("buttonChooseFile")
        self.buttonUnlock = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUnlock.setGeometry(QtCore.QRect(440, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.buttonUnlock.setFont(font)
        self.buttonUnlock.setStyleSheet("background-color:rgb(108, 217, 161)")
        self.buttonUnlock.setObjectName("buttonUnlock")
        self.labelProcess = QtWidgets.QLabel(self.centralwidget)
        self.labelProcess.setGeometry(QtCore.QRect(9, 88, 590, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelProcess.setFont(font)
        self.labelProcess.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255)")
        self.labelProcess.setObjectName("labelProcess")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 260, 420, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UnlockerEX"))
        self.buttonSave.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "UnlockerEX "))
        self.buttonChooseFile.setText(_translate("MainWindow", "Open File"))
        self.buttonUnlock.setText(_translate("MainWindow", "Unlock"))
        self.labelProcess.setText(_translate("MainWindow", "                                                              --CONSOLE--"))
