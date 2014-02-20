# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templchange.ui'
#
# Created: Thu Feb 20 16:11:11 2014
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
        TemplateChange.resize(611, 173)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(TemplateChange)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.widget = QtGui.QWidget(TemplateChange)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.widget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.widget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tllist = QtGui.QComboBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tllist.sizePolicy().hasHeightForWidth())
        self.tllist.setSizePolicy(sizePolicy)
        self.tllist.setMinimumSize(QtCore.QSize(50, 0))
        self.tllist.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tllist.setBaseSize(QtCore.QSize(50, 0))
        self.tllist.setObjectName(_fromUtf8("tllist"))
        self.horizontalLayout_3.addWidget(self.tllist)
        self.templlist = QtGui.QComboBox(self.frame_2)
        self.templlist.setObjectName(_fromUtf8("templlist"))
        self.horizontalLayout_3.addWidget(self.templlist)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(self.widget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.buttonBox = QtGui.QDialogButtonBox(self.frame_3)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(TemplateChange)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TemplateChange.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TemplateChange.reject)
        QtCore.QMetaObject.connectSlotsByName(TemplateChange)

    def retranslateUi(self, TemplateChange):
        TemplateChange.setWindowTitle(_translate("TemplateChange", "Выбор шаблона", None))
        self.label.setText(_translate("TemplateChange", "TextLabel", None))

