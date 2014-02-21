# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'typechange.ui'
#
# Created: Fri Feb 21 16:40:33 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_TypeChange(object):
    def setupUi(self, TypeChange):
        TypeChange.setObjectName(_fromUtf8("TypeChange"))
        TypeChange.resize(683, 475)
        self.horizontalLayout = QtGui.QHBoxLayout(TypeChange)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(TypeChange)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.typeview = QtGui.QTreeWidget(self.widget)
        self.typeview.setObjectName(_fromUtf8("typeview"))
        self.typeview.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout.addWidget(self.typeview)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(TypeChange)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TypeChange.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TypeChange.reject)
        QtCore.QMetaObject.connectSlotsByName(TypeChange)

    def retranslateUi(self, TypeChange):
        TypeChange.setWindowTitle(_translate("TypeChange", "Выбор модификаторов", None))

