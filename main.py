#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'a.libkind'

from PyQt4 import QtGui, QtCore
import sys, os
from interface.interface import Ui_MainWindow
from interface.dialogs import *
from src import core, SquadTemplate, ArmySquad, SquadTypes, SquadMods, Army, SquadMobility
from elixir import *

reload(sys)
sys.setdefaultencoding('utf-8')

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.loaded = False
        self.trigger_lock = False
        self.mainwindow = Ui_MainWindow()
        self.mainwindow.setupUi(self)
        self.load_data()
        self.loaded = True

    def load_data(self):
        core.calc_all()
        self.fill_templatetable()
        self.fill_modstable()
        self.fill_armytree()
        self.fill_squadtable()
        self.fill_typetable()

    def fill_armytree(self):
        self.loaded = False
        self.mainwindow.armylist.clear()
        self.mainwindow.armylist.setHeaderItem(QtGui.QTreeWidgetItem(['Name', 'ID', 'TS', 'Raise', 'Supply', 'Weight', 'TL', 'Type', 'Mods', 'Casualities']))
        self.mainwindow.armylist.setColumnHidden(1, True)
        quer = Army.Army.query.all()
        for cur, templ in enumerate(quer):
            arm = templ.calcer2()
            root = QtGui.QTreeWidgetItem(self.mainwindow.armylist, arm['army'])
            for squad in arm['squads']:
                adding = QtGui.QTreeWidgetItem(root, squad)
        self.loaded = True

    def combotempl_constructor(self):
        box = QtGui.QComboBox()
        quer = SquadTypes.SquadTypes.query.all()
        for q in quer:
            box.addItem(q.name)
        return box

    def fill_squadtable(self):
        self.loaded = False
        self.mainwindow.squadtable.clear()
        self.mainwindow.squadtable.setColumnCount(9)
        for num, dat in enumerate(['ID', 'Name', 'Type', 'Mods', 'Casualities', 'Template', 'Mobility', 'Equip', 'Expirience']):
            self.mainwindow.squadtable.setHorizontalHeaderItem(num, QtGui.QTableWidgetItem(dat))
        self.mainwindow.squadtable.setColumnHidden(0, True)
        quer = ArmySquad.ArmySquad.query.all()
        self.mainwindow.squadtable.setRowCount(len(quer))

        for cur, templ in enumerate(quer):
            fields = templ.calcer()
            item = QtGui.QTreeWidgetItem(fields)
            item.templ = templ
            for num, dat in enumerate(fields):
                res = QtGui.QTableWidgetItem(dat)
                if not num in [1, 4]: res.setFlags(QtCore.Qt.ItemIsEnabled)
                self.mainwindow.squadtable.setItem(cur, num, res)
        self.loaded = True

    def fill_modstable(self):
        self.loaded = False
        self.mainwindow.modstable.clear()
        for num, dat in enumerate(['ID', 'Name', 'TS', 'Raise', 'Supply', 'Weight', 'TL']):
            self.mainwindow.modstable.setHorizontalHeaderItem(num, QtGui.QTableWidgetItem(dat))
        self.mainwindow.modstable.setColumnHidden(0, True)
        quer = SquadMods.SquadMods.query.all()
        self.mainwindow.modstable.setRowCount(len(quer))
        for cur, templ in enumerate(quer):
            fields = [str(templ.id), templ.name, str(templ.ts), str(templ.raise_cost), str(templ.supply), str(templ.weight), str(templ.tl)]
            item = QtGui.QTreeWidgetItem(fields)
            item.templ = templ
            for num, dat in enumerate(fields):
                self.mainwindow.modstable.setItem(cur, num, QtGui.QTableWidgetItem(dat))
        self.loaded = True

    def fill_typetable(self):
        self.loaded = False
        self.mainwindow.typetable.clear()
        for num, dat in enumerate(['ID', 'Type']):
            self.mainwindow.typetable.setHorizontalHeaderItem(num, QtGui.QTableWidgetItem(dat))
        self.mainwindow.typetable.setColumnHidden(0, True)
        quer = SquadTypes.SquadTypes.query.all()
        self.mainwindow.typetable.setRowCount(len(quer))

        for cur, templ in enumerate(quer):
            fields = [str(templ.id), templ.name]
            item = QtGui.QTreeWidgetItem(fields)
            for num, dat in enumerate(fields):
                self.mainwindow.typetable.setItem(cur, num, QtGui.QTableWidgetItem(dat))

        self.mainwindow.mobilitytable.clear()
        for num, dat in enumerate(['ID', 'Mobility']):
            self.mainwindow.mobilitytable.setHorizontalHeaderItem(num, QtGui.QTableWidgetItem(dat))
        self.mainwindow.mobilitytable.setColumnHidden(0, True)
        quer = SquadMobility.SquadMobility.query.all()
        self.mainwindow.mobilitytable.setRowCount(len(quer))

        for cur, templ in enumerate(quer):
            fields = [str(templ.id), templ.name]
            item = QtGui.QTreeWidgetItem(fields)
            for num, dat in enumerate(fields):
                self.mainwindow.mobilitytable.setItem(cur, num, QtGui.QTableWidgetItem(dat))

        self.loaded = True

    def fill_templatetable(self):
        self.loaded = False
        self.mainwindow.templatetable.clear()
        self.mainwindow.templatetable.setColumnCount(10)
        for num, dat in enumerate(['ID', 'Name', 'TS', 'Raise', 'Supply', 'Weight', 'TL', 'Type', 'Mobility', u'Скорость']):
            self.mainwindow.templatetable.setHorizontalHeaderItem(num, QtGui.QTableWidgetItem(dat))
        self.mainwindow.templatetable.setColumnHidden(0, True)
        quer = SquadTemplate.SquadTemplate.query.all()
        self.mainwindow.templatetable.setRowCount(len(quer))
        for cur, templ in enumerate(quer):
            fields = templ.calcer()
            for num, dat in enumerate(fields):
                res = QtGui.QTableWidgetItem(dat)
                if num in [7, 8, 9]: res.setFlags(QtCore.Qt.ItemIsEnabled)
                self.mainwindow.templatetable.setItem(cur, num, res)
        self.loaded = True

    def on_squadtable_cellClicked(self, row, col):
        target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.templatetable.item(row, 0).text()))
        self.mainwindow.squadopts.setText(target.typelist())

    def on_templatetable_cellDoubleClicked(self, row, col):
        if col == 7:
            target = SquadTemplate.SquadTemplate.get_by(id=int(self.mainwindow.templatetable.item(row, 0).text()))
            dlg = TypeChange(self, types=[t.id for t in target.type], item=target)
            dlg.exec_()
        if col == 8:
            target = SquadTemplate.SquadTemplate.get_by(id=int(self.mainwindow.templatetable.item(row, 0).text()))
            dlg = MobilityChanger(self, mob=target.mobility, tl=target.tl, item=target)
            dlg.exec_()

    def on_squadtable_cellDoubleClicked(self, row, col):
        '''if col == 2:
            target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = TypeChange(self, types=[t.id for t in target.type], item=target)
            dlg.exec_()'''
        if col == 3:
            target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = ModsChange(self, mods=[t.id for t in target.mods], item=target)
            dlg.exec_()
        if col == 5:
            target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = TemplChange(self, templ=target.templ, item=target)
            dlg.exec_()
        if col == 7:
            target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = EquipChanger(self, eq=target.equip, item=target)
            dlg.exec_()
        if col == 8:
            target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = ExpChanger(self, exp=target.exp, item=target)
            dlg.exec_()

        '''if col == 6:
            target = SquadTemplate.SquadTemplate.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = MobilityChanger(self, mob=target.mobility, tl=target.tl, item=target)
            dlg.exec_()'''

    def on_templatetable_itemChanged(self, item):
        if self.loaded and not item.column() == 7:
            changed_item = SquadTemplate.SquadTemplate.get_by(id=int(self.mainwindow.templatetable.item(item.row(), 0).text()))
            setattr(changed_item, changed_item.fields[item.column()].name, str(item.text()))
            core.saveData()

    def on_armylist_itemClicked(self, item):
        if not item.parent():
            index = item.text(1)
        else:
            index = item.parent().text(1)
        changed_item = Army.Army.get_by(id=int(index))
        self.mainwindow.armyopts.setText(changed_item.typelist())

    def on_squadtable_itemChanged(self, item):
        if self.loaded:
            changed_item = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(item.row(), 0).text()))
            setattr(changed_item, changed_item.fields[item.column()].name, str(item.text()))
            core.saveData()

    def on_modstable_itemChanged(self, item):
        if self.loaded:
            changed_item = SquadMods.SquadMods.get_by(id=int(self.mainwindow.modstable.item(item.row(), 0).text()))
            setattr(changed_item, changed_item.fields[item.column()].name, str(item.text()))
            core.saveData()

    def on_typetable_itemChanged(self, item):
        if self.loaded:
            changed_item = SquadTypes.SquadTypes.get_by(id=int(self.mainwindow.typetable.item(item.row(), 0).text()))
            setattr(changed_item, changed_item.fields[item.column()].name, str(item.text()))
            core.saveData()

    def on_updateaction_triggered(self, foo=True):
        if not foo:
            self.load_data()

    def on_addaction_triggered(self, foo=True):
        if not foo:
            curr_view = self.mainwindow.toolBox.currentIndex()
            print curr_view
            if curr_view == 1:
                #print SquadTemplate.SquadTemplate.query.first()
                newsquad = ArmySquad.ArmySquad(name=u'new', templ=SquadTemplate.SquadTemplate.query.first(), equip=SquadEquip.SquadEquip.query.first(), mobility=SquadMobility.SquadMobility.query.first())
                core.saveData()
                self.load_data()
            if curr_view == 2:
                newmod = SquadMods.SquadMods(name=u'new')
                core.saveData()
                self.load_data()
            if curr_view == 3:
                newtempl = SquadTemplate.SquadTemplate(name=u'new', mobility=SquadMobility.SquadMobility.query.first())
                core.saveData()
                self.load_data()
            if curr_view == 4:
                newtype = SquadTypes.SquadTypes(name=u'new')
                core.saveData()
                self.load_data()

    def on_removeaction_triggered(self, foo=True):
        if not foo:
            curr_view = self.mainwindow.toolBox.currentIndex()
            if curr_view == 1:
                rows = list(set([t.row() for t in self.mainwindow.squadtable.selectedItems()]))
                for rr in rows:
                    changed_item = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(rr, 0).text()))
                    changed_item.delete()
                core.saveData()
                self.load_data()
            if curr_view == 2:
                rows = list(set([t.row() for t in self.mainwindow.modstable.selectedItems()]))
                for rr in rows:
                    changed_item = SquadMods.SquadMods.get_by(id=int(self.mainwindow.modstable.item(rr, 0).text()))
                    changed_item.delete()
                core.saveData()
                self.load_data()
            if curr_view == 3:
                rows = list(set([t.row() for t in self.mainwindow.templatetable.selectedItems()]))
                for rr in rows:
                    changed_item = SquadTemplate.SquadTemplate.get_by(id=int(self.mainwindow.templatetable.item(rr, 0).text()))
                    changed_item.delete()
                core.saveData()
                self.load_data()
            if curr_view == 4:
                rows = list(set([t.row() for t in self.mainwindow.typetable.selectedItems()]))
                for rr in rows:
                    changed_item = SquadTypes.SquadTypes.get_by(id=int(self.mainwindow.typetable.item(rr, 0).text()))
                    changed_item.delete()
                core.saveData()
                self.load_data()

if __name__ == '__main__':

    core.initDB()
    #core.sampleArmy()
    core.calc_all()
    #print [(t.name, t.param) for t in ArmyTemplate.ArmyTemplate.query.all()]

    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())