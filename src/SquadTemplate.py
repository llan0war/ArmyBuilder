__author__ = 'a.libkind'

from elixir import *


class SquadTemplate(Entity):

    using_options(tablename='templates')
    id = Field(Integer, autoincrement=True, primary_key=True)
    name = Field(Text, required=True)
    ts = Field(Integer, required=False, default=0)
    raise_cost = Field(Integer, required=False, default=0)
    supply = Field(Integer, required=False, default=0)
    weight = Field(Integer, required=False, default=0)
    tl = Field(Integer, required=False, default=0)
    type = ManyToMany('SquadTypes')
    squads = OneToMany('ArmySquad')
    mobility = ManyToOne('SquadMobility')
    speed = Field(Text, required=False)
    transport = Field(Integer, required=False, default=0)
    support = Field(Boolean, required=False, default=False)
    stype = 'Squad'


    fields = [id, name, ts, raise_cost, supply, weight, tl, type, mobility, speed, transport]

    def __repr__(self):
        return 'Template %s ts: %s raise: %s supply: %s weight: %s tl: %s type: %s ' % \
               (self.name, str(self.ts), str(self.raise_cost), str(self.supply), str(self.weight), str(self.tl), self.type)

    def printer(self):
        return 'TS: %s Raise Cost: %s Supply: %s Weight: %s TL: %s Type: %s ' % \
               (str(self.ts), str(self.raise_cost), str(self.supply), str(self.weight), str(self.tl), ','.join([t.name for t in self.type]))

    def calcer(self):
        res = ''
        if self.support:
            res = 'X'
        return [str(self.id), self.name, str(self.ts), str(self.raise_cost), str(self.supply), str(self.weight),
                str(self.tl), ', '.join([t.name for t in self.type]), self.mobility.name, self.speed, str(self.transport), res,'']

