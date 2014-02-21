#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'a.libkind'

from elixir import *
from src import SquadTemplate

class ArmySquad(Entity):

    using_options(tablename='squads')
    templ = ManyToOne('SquadTemplate')
    id = Field(Integer, autoincrement=True, primary_key=True)
    name = Field(Text, required=True)
    mods = ManyToMany('SquadMods')
    casualities = Field(Integer, required=False, default=0)
    ts = Field(Integer, required=False, default=0)
    type = ManyToMany('SquadTypes')
    raise_cost = Field(Integer, required=False, default=0)
    supply = Field(Integer, required=False, default=0)
    weight = Field(Integer, required=False, default=0)
    tl = Field(Integer, required=False, default=0)
    speed = Field(Text, required=False)
    mobility = ManyToOne('SquadMobility')
    equip = ManyToOne('SquadEquip')
    exp = ManyToOne('SquadExp')
    army = ManyToOne('Army')
    count = Field(Integer, required=True, default=1)
    transport = Field(Integer, required=False, default=0)
    support = Field(Boolean, required=False, default=False)
    transporting = OneToMany('ArmySquad') # кого везем
    transported = ManyToOne('ArmySquad') # кто нас везет
    fields = [id, name, type, mods, casualities, templ, mobility, equip, exp, count]
    stype = 'Squad'

    def calc_all(self):
        modes = self.mods
        self.type = self.templ.type
        self.mobility = self.templ.mobility
        self.tl = self.templ.tl
        self.transport = self.templ.transport * self.count
        self.support = self.templ.support

        ts_mod = sum([md.ts for md in modes]) + self.equip.ts + self.exp.ts
        self.ts = int(self.templ.ts * self.count * (100 + max(ts_mod, -80))/100 + 0.5)*(1 if not u'Super-Soldier' in [md.name for md in modes] else 2)

        raise_mod = sum([md.raise_cost for md in modes]) + self.equip.raise_cost + self.exp.raise_cost + \
                    (-50 if ('Fanatic' in [md.name for md in modes]) and self.exp.name == u'Good' else 0) + \
                    (-100 if ('Fanatic' in [md.name for md in modes]) and self.exp.name == u'Elite' else 0)
        self.raise_cost = int(self.templ.raise_cost * self.count * (100 + max(raise_mod, -80))/100 + 0.5)

        supply_mod = sum([md.supply for md in modes]) + self.equip.supply + self.exp.supply
        self.supply = int(self.templ.supply * self.count * (100 + max(supply_mod, -80))/100 + 0.5)

        self.weight = int(self.templ.weight * self.count * (100 + max(sum([md.weight for md in modes]), -80))/100 + 0.5)

    def __repr__(self):
        return 'ArmySquad %s ts: %s raise: %s supply: %s weight: %s tl: %s type: %s id: %s ' % \
               (self.name, str(self.ts), str(self.raise_cost), str(self.supply), str(self.weight), str(self.tl), self.type, str(self.id))

    def calcer(self):
        self.calc_all()
        '''return [str(self.id), self.name, str(self.ts), str(self.raise_cost), str(self.supply), str(self.weight),
                str(self.tl), ', '.join([t.name for t in self.type]), ', '.join([t.name for t in self.mods]),
                str(self.casualities), self.templ.name, self.mobility.name, self.speed, '']'''

        return [str(self.id), self.name, ', '.join([t.name for t in self.type]), ', '.join([t.name for t in self.mods]),
                str(self.casualities), self.templ.name, self.mobility.name, self.equip.name, self.exp.name, str(self.count), '']

    def typelist(self):
        supp = ''
        if self.support:
            supp = ' \n Support \n'
        res = 'Squad: %s \n TS: %s \n Raise Cost: %s \n Weight: %s \n TL: %s \n Supply: %s \n Speed: %s \n Transport: %s \n Army: %s \n' % \
              (self.name, str(self.ts), str(self.raise_cost), str(self.weight), str(self.tl), str(self.supply), self.speed, self.transport, self.army.name)
        res = res + supp
        res = res + '\n '.join(['%s: %s' % (md.name, md.comment) for md in self.mods if len(md.comment) > 0])
        res = res + '\n %s: %s' % (self.mobility.name, self.mobility.comment)
        return res
