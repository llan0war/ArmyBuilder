# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mobilitychanger.ui'
#
# Created: Thu Feb 20 18:08:06 2014
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

class Ui_MobilityChange(object):
    def setupUi(self, MobilityChange):
        MobilityChange.setObjectName(_fromUtf8("MobilityChange"))
        MobilityChange.resize(484, 119)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(MobilityChange)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.widget = QtGui.QWidget(MobilityChange)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.moblist = QtGui.QComboBox(self.widget)
        self.moblist.setObjectName(_fromUtf8("moblist"))
        self.verticalLayout.addWidget(self.moblist)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(MobilityChange)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MobilityChange.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MobilityChange.reject)
        QtCore.QMetaObject.connectSlotsByName(MobilityChange)

    def retranslateUi(self, MobilityChange):
        MobilityChange.setWindowTitle(_translate("MobilityChange", "Выбор типа передвижения", None))
        self.label.setText(_translate("MobilityChange", "Выбор тип перемещения", None))

