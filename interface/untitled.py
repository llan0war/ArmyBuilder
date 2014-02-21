# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Feb 21 17:58:19 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(840, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setBaseSize(QtCore.QSize(350, 350))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 0))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(18, 12, 811, 471))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 811, 417))
        self.page.setObjectName(_fromUtf8("page"))
        self.list = QtGui.QTreeWidget(self.page)
        self.list.setGeometry(QtCore.QRect(0, 0, 811, 411))
        self.list.setAnimated(True)
        self.list.setWordWrap(True)
        self.list.setObjectName(_fromUtf8("list"))
        self.list.headerItem().setText(0, _fromUtf8("Name"))
        font = QtGui.QFont()
        font.setKerning(False)
        self.list.headerItem().setFont(0, font)
        self.list.header().setCascadingSectionResizes(True)
        self.list.header().setHighlightSections(True)
        self.list.header().setSortIndicatorShown(True)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.table = QtGui.QTableWidget(self.page_3)
        self.table.setGeometry(QtCore.QRect(0, 10, 811, 361))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(8)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.list.headerItem().setText(1, _translate("MainWindow", "TS", None))
        self.list.headerItem().setText(2, _translate("MainWindow", "Raise", None))
        self.list.headerItem().setText(3, _translate("MainWindow", "Supply", None))
        self.list.headerItem().setText(4, _translate("MainWindow", "Weight", None))
        self.list.headerItem().setText(5, _translate("MainWindow", "TL", None))
        self.list.headerItem().setText(6, _translate("MainWindow", "Type", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TS", None))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Raise", None))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Supply", None))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Weight", None))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "TL", None))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Type", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Страница", None))

