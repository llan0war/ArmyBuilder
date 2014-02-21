#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'a.libkind'

from PyQt4 import QtGui, QtCore
import sys
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
        curtab = self.mainwindow.toolBox.currentIndex()
        core.calc_all()
        self.fill_templatetable()
        self.fill_modstable()
        self.fill_armytree()
        self.fill_squadtable()
        self.fill_typetable()
        self.mainwindow.toolBox.setCurrentIndex(curtab)

    def fill_armytree(self):
        self.loaded = False
        self.mainwindow.armylist.clear()
        self.mainwindow.armylist.setHeaderItem(QtGui.QTreeWidgetItem(['Name', 'ID', 'SType', 'TS', 'Raise', 'Supply', 'Weight', 'TL', 'Type', 'Mods', 'Casualities', 'Count']))
        self.mainwindow.armylist.setColumnHidden(1, True)
        self.mainwindow.armylist.setColumnHidden(2, True)
        self.mainwindow.armylist.header().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        #.setResizeMode(QtGui.QHeaderView.Stretch)
        quer = Army.Army.query.all()
        for cur, templ in enumerate(quer):
            arm = templ.calcer2()
            root = QtGui.QTreeWidgetItem(self.mainwindow.armylist, arm['army'])
            for squad in arm['squads']:
                adding = QtGui.QTreeWidgetItem(root, squad['data'])
                if len(squad['transporting']) > 0:
                    for sqt in squad['transporting']:
                        lv2 = QtGui.QTreeWidgetItem(adding, sqt['data'])
        self.loaded = True

    def fill_squadtable(self):
        self.loaded = False
        self.mainwindow.squadtable.clear()
        self.mainwindow.squadtable.setColumnCount(10)
        for num, dat in enumerate(['ID', 'Name', 'Type', 'Mods', 'Casualities', 'Template', 'Mobility', 'Equip', 'Expirience', u'Количество']):
            self.mainwindow.squadtable.setHorizontalHeaderItem(num, QtGui.QTableWidgetItem(dat))
        self.mainwindow.squadtable.setColumnHidden(0, True)
        self.mainwindow.squadtable.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        quer = ArmySquad.ArmySquad.query.all()
        self.mainwindow.squadtable.setRowCount(len(quer))

        for cur, templ in enumerate(quer):
            fields = templ.calcer()
            item = QtGui.QTreeWidgetItem(fields)
            item.templ = templ
            for num, dat in enumerate(fields):
                res = QtGui.QTableWidgetItem(dat)
                if not num in [1, 4, 9]: res.setFlags(QtCore.Qt.ItemIsEnabled)
                self.mainwindow.squadtable.setItem(cur, num, res)
        self.loaded = True

    def fill_modstable(self):
        self.loaded = False
        self.mainwindow.modstable.clear()
        for num, dat in enumerate(['ID', 'Name', 'TS', 'Raise', 'Supply', 'Weight', 'TL']):
            self.mainwindow.modstable.setHorizontalHeaderItem(num, QtGui.QTableWidgetItem(dat))
        self.mainwindow.modstable.setColumnHidden(0, True)
        self.mainwindow.modstable.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
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
        self.mainwindow.typetable.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
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
        self.mainwindow.templatetable.setColumnCount(12)
        for num, dat in enumerate(['ID', 'Name', 'TS', 'Raise', 'Supply', 'Weight', 'TL', 'Type', 'Mobility', u'Скорость', u'Грузоподьемность', 'Support']):
            self.mainwindow.templatetable.setHorizontalHeaderItem(num, QtGui.QTableWidgetItem(dat))
        self.mainwindow.templatetable.setColumnHidden(0, True)
        self.mainwindow.templatetable.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        quer = SquadTemplate.SquadTemplate.query.all()
        self.mainwindow.templatetable.setRowCount(len(quer))
        for cur, templ in enumerate(quer):
            fields = templ.calcer()
            for num, dat in enumerate(fields):
                res = QtGui.QTableWidgetItem(dat)
                if num in [7, 8, 9, 11]: res.setFlags(QtCore.Qt.ItemIsEnabled)
                self.mainwindow.templatetable.setItem(cur, num, res)
        self.loaded = True

    def on_squadtable_cellClicked(self, row, col):
        target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.templatetable.item(row, 0).text()))
        self.mainwindow.squadopts.setText(target.typelist())

    def on_templatetable_cellDoubleClicked(self, row, col):
        if col == 7:
            target = SquadTemplate.SquadTemplate.get_by(id=int(self.mainwindow.templatetable.item(row, 0).text()))
            dlg = TypeChange(self, types=[t.id for t in target.type], item=target)
            if dlg.exec_():
                self.load_data()
        if col == 8:
            target = SquadTemplate.SquadTemplate.get_by(id=int(self.mainwindow.templatetable.item(row, 0).text()))
            dlg = MobilityChanger(self, mob=target.mobility, tl=target.tl, item=target)
            if dlg.exec_():
                self.load_data()
        if col == 11:
            target = SquadTemplate.SquadTemplate.get_by(id=int(self.mainwindow.templatetable.item(row, 0).text()))
            target.support = not target.support
            core.saveData()
            self.load_data()

    def on_squadtable_cellDoubleClicked(self, row, col):
        '''if col == 2:
            target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = TypeChange(self, types=[t.id for t in target.type], item=target)
            dlg.exec_()'''
        if col == 3:
            target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = ModsChange(self, mods=[t.id for t in target.mods], item=target)
            if dlg.exec_():
                self.load_data()
        if col == 5:
            target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = TemplChange(self, templ=target.templ, item=target)
            if dlg.exec_():
                self.load_data()
        if col == 7:
            target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = EquipChanger(self, eq=target.equip, item=target)
            if dlg.exec_():
                self.load_data()
        if col == 8:
            target = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = ExpChanger(self, exp=target.exp, item=target)
            if dlg.exec_():
                self.load_data()
        '''if col == 6:
            target = SquadTemplate.SquadTemplate.get_by(id=int(self.mainwindow.squadtable.item(row, 0).text()))
            dlg = MobilityChanger(self, mob=target.mobility, tl=target.tl, item=target)
            dlg.exec_()'''

    def on_templatetable_itemChanged(self, item):
        if self.loaded and not item.column() == 7:
            changed_item = SquadTemplate.SquadTemplate.get_by(id=int(self.mainwindow.templatetable.item(item.row(), 0).text()))
            setattr(changed_item, changed_item.fields[item.column()].name, str(item.text()).decode('utf-8'))
            core.saveData()
            self.load_data()


    def on_armylist_itemClicked(self, item):
        #while item.parent():
        #    item = item.parent()
        #index = item.text(1)
        if item.text(2) == 'Army':
            changed_item = Army.Army.get_by(id=int(item.text(1)))
            self.mainwindow.armyopts.setText(changed_item.typelist() + changed_item.impetous_fanatics_calcer())
        elif item.text(2) == 'Squad':
            changed_item = ArmySquad.ArmySquad.get_by(id=int(item.text(1)))
            self.mainwindow.armyopts.setText(changed_item.typelist())

    def on_armylist_itemDoubleClicked(self, item):
        if item.text(2) == 'Squad':
            changed_item = ArmySquad.ArmySquad.get_by(id=int(item.text(1)))
            dlg = SquadMod(self, arm=changed_item.army, item=changed_item)
            if dlg.exec_():
                self.load_data()
        elif item.text(2) == 'Army':
            changed_item = Army.Army.get_by(id=int(item.text(1)))
            newname, ok = QtGui.QInputDialog.getText(self, 'New name', 'Enter new army name')
            if ok:
                changed_item.name = str(newname).decode('utf-8')
                core.saveData()
                self.load_data()

    def on_squadtable_itemChanged(self, item):
        if self.loaded:
            changed_item = ArmySquad.ArmySquad.get_by(id=int(self.mainwindow.squadtable.item(item.row(), 0).text()))
            setattr(changed_item, changed_item.fields[item.column()].name, str(item.text()).decode('utf-8'))
            core.saveData()
            self.load_data()

    def on_modstable_itemChanged(self, item):
        if self.loaded:
            changed_item = SquadMods.SquadMods.get_by(id=int(self.mainwindow.modstable.item(item.row(), 0).text()))
            setattr(changed_item, changed_item.fields[item.column()].name, str(item.text()).decode('utf-8'))
            core.saveData()
            self.load_data()

    def on_typetable_itemChanged(self, item):
        if self.loaded:
            changed_item = SquadTypes.SquadTypes.get_by(id=int(self.mainwindow.typetable.item(item.row(), 0).text()))
            setattr(changed_item, changed_item.fields[item.column()].name, str(item.text()).decode('utf-8'))
            core.saveData()
            self.load_data()

    def on_updateaction_triggered(self, foo=True):
        if not foo:
            self.load_data()

    def on_addaction_triggered(self, foo=True):
        if not foo:
            curr_view = self.mainwindow.toolBox.currentIndex()
            if curr_view == 1:
                #print SquadTemplate.SquadTemplate.query.first()
                newsquad = ArmySquad.ArmySquad(name=u'new', templ=SquadTemplate.SquadTemplate.query.first(),
                                               equip=SquadEquip.SquadEquip.get_by(name=u'Basic'),
                                               mobility=SquadMobility.SquadMobility.query.first(),
                                               exp=SquadExp.SquadExp.get_by(name=u'Average'))
                dlg = TemplChange(self, templ=newsquad.templ, item=newsquad)
                dlg.exec_()
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
            if curr_view == 0:
                newarmy = Army.Army(name=u'new')
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
            if curr_view == 0:
                item = self.mainwindow.armylist.currentItem()
                while item.parent():
                    item = item.parent()
                if item.text(2) == 'Army':
                    changed_item = Army.Army.get_by(id=int(item.text(1)))
                    changed_item.delete()
                    core.saveData()
                self.load_data()

    def on_saveaction_triggered(self, foo=True):
        if not foo:
            curr_view = self.mainwindow.toolBox.currentIndex()
            if curr_view == 0:
                for i in range(self.mainwindow.armylist.topLevelItemCount()):
                    item = self.mainwindow.armylist.topLevelItem(i)
                    if item.text(2) == 'Army':
                        cur_army = Army.Army.get_by(id=int(item.text(1)))
                        #squads_num = item.childCount()
                        squads = []
                        for sq in range(item.childCount()):
                            if item.child(sq).childCount() > 0:
                                for j in range(item.child(sq).childCount()):
                                    squads.append(ArmySquad.ArmySquad.get_by(id=int(item.child(sq).child(j).text(1))))
                            squads.append(ArmySquad.ArmySquad.get_by(id=int(item.child(sq).text(1))))
                        cur_army.squads = squads
            core.saveData()
            self.load_data()

    '''def on_armylist_currentItemChanged(self, a, b):
        if b:
            item = b
            while item.parent():
                item = item.parent()
            print item.text(0), b.text(0)
            if item.text(2) != 'Army':
                print 'Unit %s change army to %s' % (b.text(0), item.text(0))

                new_army = Army.Army.get_by(id=int(item.text(1)))
                old_army = ArmySquad.ArmySquad.get_by(id=(int(b.text(1)))).army
                old_squads = old_army.squads
                old_squads.remove(b)
                new_army.squads.append(b)

                core.saveData()
                self.load_data()'''

if __name__ == '__main__':

    core.initDB()
    #core.sampleArmy()
    core.calc_all()
    #print [(t.name, t.param) for t in ArmyTemplate.ArmyTemplate.query.all()]

    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())