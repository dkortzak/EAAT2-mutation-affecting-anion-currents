# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HEKATree.ui'
#
# Created: Thu Aug 14 10:37:22 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1098, 640)
        self.treeView = QtGui.QTreeView(Dialog)
        self.treeView.setGeometry(QtCore.QRect(10, 30, 256, 281))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.displayButton = QtGui.QPushButton(Dialog)
        self.displayButton.setGeometry(QtCore.QRect(150, 320, 111, 41))
        self.displayButton.setObjectName(_fromUtf8("displayButton"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(279, 9, 801, 621))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.openButton = QtGui.QPushButton(Dialog)
        self.openButton.setGeometry(QtCore.QRect(10, 320, 111, 41))
        self.openButton.setObjectName(_fromUtf8("openButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.displayButton.setText(_translate("Dialog", "Display", None))
        self.openButton.setText(_translate("Dialog", "Open File...", None))

