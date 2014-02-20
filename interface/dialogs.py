__author__ = 'a.libkind'

from src import SquadMobility, SquadTemplate, SquadTypes, SquadMods, ArmySquad, Army, SquadEquip
from PyQt4 import QtGui, QtCore
from typechange import Ui_TypeChange
from templchange import Ui_TemplateChange
from mobilitychanger import Ui_MobilityChange
from equipchange import Ui_EquipChange
from src import core


class TypeChange(QtGui.QDialog):
    def __init__(self, parent=None, types=None, item=None):
        QtGui.QDialog.__init__(self, parent)
        self.typedialog = Ui_TypeChange()
        self.typedialog.setupUi(self)
        self.fill_types(types)
        self.res = 0
        self.item = item

    def fill_types(self, types):
        self.typedialog.typeview.clear()
        self.typedialog.typeview.setHeaderItem(QtGui.QTreeWidgetItem(['ID', 'Name']))
        self.typedialog.typeview.setColumnHidden(0, True)
        quer = SquadTypes.SquadTypes.query.all()
        for cur, templ in enumerate(quer):
            fields = [str(templ.id), templ.name]
            root = QtGui.QTreeWidgetItem(self.typedialog.typeview, fields)
            if templ.id in types:
                root.setCheckState(1, QtCore.Qt.Checked)
            else:
                root.setCheckState(1, QtCore.Qt.Unchecked)

    def accept(self):
        root = self.typedialog.typeview.invisibleRootItem()
        child_count = root.childCount()
        self.item.type = []
        for i in range(child_count):
            item = root.child(i)
            if item.checkState(1):
                print 'Found', item.text(1)
                self.item.type.append(SquadTypes.SquadTypes.get_by(id=int(item.text(0))))
        print self.item.type
        core.saveData()
        super(TypeChange, self).accept()

    def reject(self):
        super(TypeChange, self).reject()


class ModsChange(QtGui.QDialog):
    def __init__(self, parent=None, mods=None, item=None):
        QtGui.QDialog.__init__(self, parent)
        self.typedialog = Ui_TypeChange()
        self.typedialog.setupUi(self)
        self.fill_types(mods)
        self.res = 0
        self.item = item

    def fill_types(self, types):
        self.typedialog.typeview.clear()
        self.typedialog.typeview.setHeaderItem(QtGui.QTreeWidgetItem(['ID', 'Name', 'TS', 'Raise', 'Supply', 'Weight', 'TL']))
        self.typedialog.typeview.setColumnHidden(0, True)
        quer = SquadMods.SquadMods.query.all()
        for cur, templ in enumerate(quer):
            fields = [str(templ.id), templ.name, str(templ.ts), str(templ.raise_cost), str(templ.supply), str(templ.weight), str(templ.tl)]
            root = QtGui.QTreeWidgetItem(self.typedialog.typeview, fields)
            if templ.id in types:
                root.setCheckState(1, QtCore.Qt.Checked)
            else:
                root.setCheckState(1, QtCore.Qt.Unchecked)

    def accept(self):
        root = self.typedialog.typeview.invisibleRootItem()
        child_count = root.childCount()
        self.item.mods = []
        for i in range(child_count):
            item = root.child(i)
            if item.checkState(1):
                self.item.mods.append(SquadMods.SquadMods.get_by(id=int(item.text(0))))
        core.saveData()
        super(ModsChange, self).accept()

    def reject(self):
        super(ModsChange, self).reject()


class TemplChange(QtGui.QDialog):
    def __init__(self, parent=None, templ=None, item=None):
        QtGui.QDialog.__init__(self, parent)
        self.typedialog = Ui_TemplateChange()
        self.typedialog.setupUi(self)
        self.fill_types(templ)
        self.res = 0
        self.item = item

    def fill_types(self, types):
        self.typedialog.templlist.clear()
        quer = SquadTemplate.SquadTemplate.query.all()
        items = ['%s: %s' % (str(templ.id), templ.name) for templ in quer]
        self.typedialog.templlist.addItems(items)
        self.typedialog.templlist.setCurrentIndex(items.index('%s: %s' % (str(types.id), types.name)))

    def accept(self):
        item = self.typedialog.templlist.currentText()
        self.item.templ = SquadTemplate.SquadTemplate.get_by(id=int(item.split(':')[0]))
        core.saveData()
        super(TemplChange, self).accept()

    def reject(self):
        super(TemplChange, self).reject()

    def on_templlist_currentIndexChanged(self, ite):
        if type(ite) == type(1):
            item = self.typedialog.templlist.currentText()
            res = SquadTemplate.SquadTemplate.get_by(id=int(item.split(':')[0]))
            self.typedialog.label.setText(res.printer())


class MobilityChanger(QtGui.QDialog):
    def __init__(self, parent=None, mob=None, tl=None, item=None):
        QtGui.QDialog.__init__(self, parent)
        self.typedialog = Ui_MobilityChange()
        self.typedialog.setupUi(self)
        self.tl = tl
        self.res = 0
        self.item = item
        self.fill_types(mob)

    def fill_types(self, types):
        self.typedialog.moblist.clear()
        quer = SquadMobility.SquadMobility.query.all()
        items = ['%s: %s' % (str(templ.id), templ.name) for templ in quer]
        self.typedialog.moblist.addItems(items)
        self.typedialog.moblist.setCurrentIndex(items.index('%s: %s' % (str(types.id), types.name)))

    def accept(self):
        item = self.typedialog.moblist.currentText()
        self.item.mobility = SquadMobility.SquadMobility.get_by(id=int(item.split(':')[0]))
        core.saveData()
        super(MobilityChanger, self).accept()

    def reject(self):
        super(MobilityChanger, self).reject()

    def on_moblist_currentIndexChanged(self, ite):
        if type(ite) == type(1):
            item = self.typedialog.moblist.currentText()
            res = SquadMobility.SquadMobility.get_by(id=int(item.split(':')[0]))
            self.typedialog.label.setText(core.speed_calcer(res, self.tl))

class EquipChanger(QtGui.QDialog):
    def __init__(self, parent=None, eq=None, item=None):
        QtGui.QDialog.__init__(self, parent)
        self.typedialog = Ui_EquipChange()
        self.typedialog.setupUi(self)
        self.res = 0
        self.item = item
        self.fill_types(eq)

    def fill_types(self, types):
        self.typedialog.equiplist.clear()
        quer = SquadEquip.SquadEquip.query.all()
        items = ['%s: %s' % (str(templ.id), templ.name) for templ in quer]
        self.typedialog.equiplist.addItems(items)
        self.typedialog.equiplist.setCurrentIndex(items.index('%s: %s' % (str(types.id), types.name)))

    def accept(self):
        item = self.typedialog.equiplist.currentText()
        self.item.equip = SquadEquip.SquadEquip.get_by(id=int(item.split(':')[0]))
        core.saveData()
        super(EquipChanger, self).accept()

    def reject(self):
        super(EquipChanger, self).reject()

    def on_moblist_currentIndexChanged(self, ite):
        if type(ite) == type(1):
            item = self.typedialog.equiplist.currentText()
            res = SquadEquip.SquadEquip.get_by(id=int(item.split(':')[0]))
            self.typedialog.label.setText(res.name)