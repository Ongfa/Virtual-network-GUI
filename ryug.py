#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
def myfunc():
        os.system("gnome-terminal -e 'sudo mn --controller=remote'")
def myfunc1():
        os.system("gnome-terminal -e 'python  /home/ongfa/ryu/bin/ryu-manager ryu/app/simple_switch.py'")
def myfunc2():
        os.system("gnome-terminal -e 'bash -c \"python /home/ongfa/ryu/bin/ryu-manager --verbose --observe-links ryu.topology.dumper ryu.controller.controller;exec bash\"'")
def myfunc3():
        os.system("gnome-terminal -e 'bash -c  \"python /home/ongfa/ryu/rm.py;exec bash\"'")
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 541, 211))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/LogoSet02.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label  self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(135, 280, 495, 95))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.widget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.widget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.widget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.widget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.widget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.widget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL(_fromUtf8("clicked()")),myfunc)
"))   QtCore.QObject.connect(self.pushButton_4,QtCore.SIGNAL(_fromUtf8("clicked()")),myfunc1)
        QtCore.QObject.connect(self.pushButton_7,QtCore.SIGNAL(_fromUtf8("clicked()")),myfunc2)
        QtCore.QObject.connect(self.pushButton_6,QtCore.SIGNAL(_fromUtf8("clicked()")),myfunc3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Run Mininet Topology", None))
        self.pushButton_4.setText(_translate("MainWindow", "Run Simple Switch", None))
        self.pushButton_7.setText(_translate("MainWindow", "Run Dumper File", None))
        self.pushButton_2.setText(_translate("MainWindow", "Run Best Path File", None))
        self.pushButton_5.setText(_translate("MainWindow", "Push Flows", None))
        self.pushButton_8.setText(_translate("MainWindow", "Run Topology Viewer", None))
        self.pushButton_3.setText(_translate("MainWindow", "View Topology Details", None))
        self.pushButton_6.setText(_translate("MainWindow", "Delete Dumper Files", None))
        self.pushButton_9.setText(_translate("MainWindow", "Exit", None))
import test_rc
import mn

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

