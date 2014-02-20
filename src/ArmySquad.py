__author__ = 'a.libkind'

from elixir import *
from src import SquadTemplate

class ArmySquad(Entity):

    using_options(tablename='squads')
    templ = ManyToOne('SquadTemplate')
    id = Field(Integer, autoincrement=True, primary_key=True)
    name = Field(Unicode, required=True)
    mods = ManyToMany('SquadMods')
    casualities = Field(Integer, required=False, default=0)
    ts = Field(Integer, required=False, default=0)
    type = ManyToMany('SquadTypes')
    raise_cost = Field(Integer, required=False, default=0)
    supply = Field(Integer, required=False, default=0)
    weight = Field(Integer, required=False, default=0)
    tl = Field(Integer, required=False, default=0)
    speed = Field(Integer, required=False, default=0)
    mobility = ManyToOne('SquadMobility')
    equip = ManyToOne('SquadEquip')
    exp = ManyToOne('SquadExp')
    army = ManyToOne('Army')
    transport = Field(Integer, required=False, default=0)
    support = Field(Boolean, required=False, default=False)
    transporting = Field(String, required=False, default='') # id,id,id,id
    fields = [id, name, type, mods, casualities, templ, mobility]
    stype = 'Squad'

    def calc_all(self):
        modes = self.mods
        self.ts = int(self.templ.ts * (100 + max(sum([md.ts for md in modes]), -80))/100 + 0.5)
        self.type = self.templ.type
        self.mobility = self.templ.mobility
        self.raise_cost = int(self.templ.raise_cost * (100 + max(sum([md.raise_cost for md in modes]), -80))/100 + 0.5)
        self.supply = int(self.templ.supply * (100 + max(sum([md.supply for md in modes]), -80))/100 + 0.5)
        self.weight = int(self.templ.weight * (100 + max(sum([md.weight for md in modes]), -80))/100 + 0.5)
        self.tl = self.templ.tl
        self.transport = self.templ.transport
        self.support = self.templ.support

    def __repr__(self):
        return 'ArmySquad %s ts: %s raise: %s supply: %s weight: %s tl: %s type: %s id: %s ' % \
               (self.name, str(self.ts), str(self.raise_cost), str(self.supply), str(self.weight), str(self.tl), self.type, str(self.id))

    def calcer(self):
        self.calc_all()
        '''return [str(self.id), self.name, str(self.ts), str(self.raise_cost), str(self.supply), str(self.weight),
                str(self.tl), ', '.join([t.name for t in self.type]), ', '.join([t.name for t in self.mods]),
                str(self.casualities), self.templ.name, self.mobility.name, self.speed, '']'''

        return [str(self.id), self.name, ', '.join([t.name for t in self.type]), ', '.join([t.name for t in self.mods]),
                str(self.casualities), self.templ.name, self.mobility.name, self.equip.name, self.exp.name, '']

    def typelist(self):
        supp = ''
        if self.support:
            supp = ' \n Support'
        res = 'Squad: %s \n TS: %s \n Raise Cost: %s \n Weight: %s \n TL: %s \n Supply: %s \n Speed: %s \n Transport: %s' % \
              (self.name, str(self.ts), str(self.raise_cost), str(self.weight), str(self.tl), str(self.supply), self.speed, self.transport)
        return res + supp
