# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'squadmod.ui'
#
# Created: Fri Feb 21 17:10:24 2014
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

class Ui_SquadMod(object):
    def setupUi(self, SquadMod):
        SquadMod.setObjectName(_fromUtf8("SquadMod"))
        SquadMod.resize(611, 202)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(SquadMod)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.widget = QtGui.QWidget(SquadMod)
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
        self.formLayout = QtGui.QFormLayout(self.frame_2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.transportlist = QtGui.QComboBox(self.frame_2)
        self.transportlist.setObjectName(_fromUtf8("transportlist"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.transportlist)
        self.casualities = QtGui.QSpinBox(self.frame_2)
        self.casualities.setMaximum(100)
        self.casualities.setObjectName(_fromUtf8("casualities"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.casualities)
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
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

        self.retranslateUi(SquadMod)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SquadMod.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SquadMod.reject)
        QtCore.QMetaObject.connectSlotsByName(SquadMod)

    def retranslateUi(self, SquadMod):
        SquadMod.setWindowTitle(_translate("SquadMod", "Редактирование отряда", None))
        self.label.setText(_translate("SquadMod", "TextLabel", None))
        self.label_2.setText(_translate("SquadMod", "Транспорт", None))
        self.label_3.setText(_translate("SquadMod", "Потери", None))

