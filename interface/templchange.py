# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templchange.ui'
#
# Created: Thu Feb 20 13:26:58 2014
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

class Ui_TemplateChange(object):
    def setupUi(self, TemplateChange):
        TemplateChange.setObjectName(_fromUtf8("TemplateChange"))
        TemplateChange.resize(484, 119)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(TemplateChange)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.widget = QtGui.QWidget(TemplateChange)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.templlist = QtGui.QComboBox(self.widget)
        self.templlist.setObjectName(_fromUtf8("templlist"))
        self.verticalLayout.addWidget(self.templlist)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(TemplateChange)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TemplateChange.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TemplateChange.reject)
        QtCore.QMetaObject.connectSlotsByName(TemplateChange)

    def retranslateUi(self, TemplateChange):
        TemplateChange.setWindowTitle(_translate("TemplateChange", "Выбор шаблона", None))
        self.label.setText(_translate("TemplateChange", "TextLabel", None))

