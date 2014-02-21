__author__ = 'a.libkind'

from src import SquadMobility, SquadTemplate, SquadTypes, SquadMods, ArmySquad, Army, SquadEquip, SquadExp
from PyQt4 import QtGui, QtCore
from typechange import Ui_TypeChange
from templchange import Ui_TemplateChange
from mobilitychanger import Ui_MobilityChange
from equipchange import Ui_EquipChange
from expchange import Ui_ExpChange
from squadmod import Ui_SquadMod
from src import core


class TypeChange(QtGui.QDialog):
    def __init__(self, parent=None, types=None, item=None):
        QtGui.QDialog.__init__(self, parent)
        self.typedialog = Ui_TypeChange()
        self.typedialog.setupUi(self)
        self.res = 0
        self.item = item
        self.fill_types(types)

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
                self.item.type.append(SquadTypes.SquadTypes.get_by(id=int(item.text(0))))
        core.saveData()
        super(TypeChange, self).accept()

    def reject(self):
        super(TypeChange, self).reject()


class ModsChange(QtGui.QDialog):
    def __init__(self, parent=None, mods=None, item=None):
        QtGui.QDialog.__init__(self, parent)
        self.typedialog = Ui_TypeChange()
        self.typedialog.setupUi(self)
        self.res = 0
        self.item = item
        self.fill_types(mods)

    def fill_types(self, types):
        self.typedialog.typeview.clear()
        self.typedialog.typeview.setHeaderItem(QtGui.QTreeWidgetItem(['ID', 'Name', 'TS', 'Raise', 'Supply', 'Weight', 'TL']))
        self.typedialog.typeview.setColumnHidden(0, True)
        quer = SquadMods.SquadMods.query.all()
        for cur, templ in enumerate(quer):
            fields = [str(templ.id), templ.name, str(templ.ts), str(templ.raise_cost), str(templ.supply), str(templ.weight), str(templ.tl)]
            if templ.name == 'Hovercraft':
                if self.item.mobility.name in [u'Motorized', u'Coast'] and self.item.tl > 7:
                    root = QtGui.QTreeWidgetItem(self.typedialog.typeview, fields)
                    if templ.id in types:
                        root.setCheckState(1, QtCore.Qt.Checked)
                    else:
                        root.setCheckState(1, QtCore.Qt.Unchecked)
            else:
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
        self.loaded = False
        self.item = item
        self.templ = templ
        self.fill_tl()
        self.loaded = True

    def fill_tl(self):
        self.typedialog.tllist.clear()
        quer = SquadTemplate.SquadTemplate.query.all()
        items = list(set(['TL: %s' % str(templ.tl) for templ in quer]))
        self.typedialog.tllist.addItems(items)
        self.typedialog.tllist.setCurrentIndex(items.index('TL: %s' % str(self.templ.tl)))

    def fill_types(self, tl):
        self.loaded = False
        self.typedialog.templlist.clear()
        quer = SquadTemplate.SquadTemplate.query.all()
        items = ['%s: %s' % (str(templ.id), templ.name) for templ in quer if templ.tl == tl]
        self.typedialog.templlist.addItems(items)
        self.loaded = True
        self.on_templlist_currentIndexChanged(self.typedialog.templlist.currentIndex())
        if not self.loaded: self.typedialog.templlist.setCurrentIndex(items.index('%s: %s' % (str(self.templ.id), self.templ.name)))

    def accept(self):
        item = self.typedialog.templlist.currentText()
        self.item.templ = SquadTemplate.SquadTemplate.get_by(id=int(item.split(':')[0]))
        core.saveData()
        super(TemplChange, self).accept()

    def reject(self):
        super(TemplChange, self).reject()

    def on_templlist_currentIndexChanged(self, ite):
        if type(ite) == type(1) and self.loaded:
            item = self.typedialog.templlist.currentText()
            res = SquadTemplate.SquadTemplate.get_by(id=int(item.split(':')[0]))
            self.typedialog.label.setText(res.printer())

    def on_tllist_currentIndexChanged(self, ite):
        if type(ite) == type(1):
            curtl = int(self.typedialog.tllist.currentText().split(':')[1])
            self.fill_types(curtl)


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


class ExpChanger(QtGui.QDialog):
    def __init__(self, parent=None, exp=None, item=None):
        QtGui.QDialog.__init__(self, parent)
        self.typedialog = Ui_ExpChange()
        self.typedialog.setupUi(self)
        self.res = 0
        self.item = item
        self.fill_types(exp)

    def fill_types(self, types):
        self.typedialog.explist.clear()
        quer = SquadExp.SquadExp.query.all()
        items = ['%s: %s' % (str(templ.id), templ.name) for templ in quer]
        self.typedialog.explist.addItems(items)
        self.typedialog.explist.setCurrentIndex(items.index('%s: %s' % (str(types.id), types.name)))

    def accept(self):
        item = self.typedialog.explist.currentText()
        self.item.exp = SquadExp.SquadExp.get_by(id=int(item.split(':')[0]))
        core.saveData()
        super(ExpChanger, self).accept()

    def reject(self):
        super(ExpChanger, self).reject()

    def on_explist_currentIndexChanged(self, ite):
        if type(ite) == type(1):
            item = self.typedialog.explist.currentText()
            res = SquadExp.SquadExp.get_by(id=int(item.split(':')[0]))
            self.typedialog.label.setText(res.name)

class SquadMod(QtGui.QDialog):
    def __init__(self, parent=None, arm=None, item=None):
        QtGui.QDialog.__init__(self, parent)
        self.typedialog = Ui_SquadMod()
        self.typedialog.setupUi(self)
        self.res = 0
        self.item = item
        self.trans = arm.get_transport_list()
        self.fill_types()

    def fill_types(self):
        self.typedialog.casualities.setValue(self.item.casualities)
        self.typedialog.transportlist.clear()
        list = ['%d: %s(free %d)' % (int(tr), self.trans[tr]['name'],self.trans[tr]['free']) for tr in self.trans.iterkeys() if (self.trans[tr]['free'] > self.item.weight) and not self.item.id == tr]
        list.append('None')
        self.typedialog.transportlist.addItems(list)

    def accept(self):
        item = self.typedialog.transportlist.currentText()
        if not item == 'None':
            self.item.transported = ArmySquad.ArmySquad.get_by(id=int(item.split(':')[0]))
        else:
            self.item.transported = None
        self.item.casualities = self.typedialog.casualities.value()
        core.saveData()
        super(SquadMod, self).accept()

    def reject(self):
        super(SquadMod, self).reject()

    def on_transportlist_currentIndexChanged(self, ite):
        if type(ite) == type(1):
            item = self.typedialog.transportlist.currentText()
            if not item == 'None':
                id = int(item.split(':')[0])
                sel = self.trans[id]
                #name speed free transporting
                self.typedialog.label.setText('%s - %s - %d \n %s' % (sel['name'], sel['speed'], sel['free'], sel['transporting']))
            else:
                self.typedialog.label.setText('None')