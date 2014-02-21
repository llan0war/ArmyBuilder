#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'a.libkind'

from elixir import *
from sqlalchemy import select, func

class Army(Entity):

    using_options(tablename='army')
    squads = OneToMany('ArmySquad')
    name = Field(Text, required=True)
    ts = Field(Integer, required=False, default=0)
    id = Field(Integer, autoincrement=True, primary_key=True)
    type = ManyToMany('SquadTypes')
    raise_cost = Field(Integer, required=False, default=0)
    supply = Field(Integer, required=False, default=0)
    weight = Field(Integer, required=False, default=0)
    tl = Field(Integer, required=False, default=0)
    stype = 'Army'

    def __repr__(self):
        return 'Army %s %d' % (self.name, self.id)

    def calcer(self):
        armlst = self.squads
        self.ts = sum([int(al.ts*(100 - al.casualities)/100 + 0.5) for al in armlst if not al.support])
        self.raise_cost = sum([int(al.raise_cost*(100 - al.casualities)/100 + 0.5) for al in armlst])
        self.supply = sum([int(al.supply*(100 - al.casualities)/100 + 0.5) for al in armlst])
        self.weight = sum([int(al.weight*(100 - al.casualities)/100 + 0.5) for al in armlst])
        if len(armlst) > 0:
            self.tl = max([al.tl for al in armlst])
        else:
            self.tl = 0
        return [self.name, str(self.ts), str(self.raise_cost), str(self.supply), str(self.weight), str(self.tl), '', '', '']

    def calcer2(self):
        res = {}
        res['army'] = [self.name, str(self.id), self.stype, str(self.ts), str(self.raise_cost), str(self.supply), str(self.weight), str(self.tl), '', '', '']
        res['squads'] = []
        for sq in self.squads:
            if not sq.transported:
                tmpsquad = self.squad_data(sq)
                res['squads'].append(tmpsquad)
        return res

    def squad_data(self, sq):
        res_sq = {}
        tmpsquad = []
        tmpsquad.append(sq.name)
        tmpsquad.append(str(sq.id))
        tmpsquad.append(sq.stype)
        tmpsquad.append(str(int(sq.ts*(100 - sq.casualities)/100 + 0.5)))
        tmpsquad.append(str(int(sq.raise_cost*(100 - sq.casualities)/100 + 0.5)))
        tmpsquad.append(str(int(sq.supply*(100 - sq.casualities)/100 + 0.5)))
        tmpsquad.append(str(int(sq.weight*(100 - sq.casualities)/100 + 0.5)))
        tmpsquad.append(str(int(sq.tl)))
        tmpsquad.append(','.join([t.name for t in sq.type]))
        tmpsquad.append(','.join([t.name for t in sq.mods]))
        tmpsquad.append(str(int(sq.casualities)))
        trans = []
        if len(sq.transporting) > 0:
            for passenger in sq.transporting:
                trans.append(self.squad_data(passenger))
        res_sq['data'] = tmpsquad
        res_sq['transporting'] = trans
        return res_sq

    def typelist(self):
        typecoll = {}
        for sq in self.squads:
            for t in sq.type:
                typecoll[t.name] = 0
        for sq in self.squads:
            for t in sq.type:
                typecoll[t.name] += int(int(sq.ts*(100 - sq.casualities)/100 + 0.5))
        res = 'Army: %s \n %s' % (self.name, '\n'.join(['%s: %s' % (key, val) for key, val in typecoll.iteritems()]))
        return res

    def impetous_fanatics_calcer(self):
        self.calcer()
        squad_num = sum([sq.count for sq in self.squads])
        armts = self.ts
        if squad_num == 0 or armts == 0:
            return '\n Fanatics: %d \n Impetous: %d' % (0, 0)
        fan_num = float((sum([sq.count for sq in self.squads if u'Fanatic' in [md.name for md in sq.mods]])))
        fan_ts = float((sum([int(sq.ts*(100 - sq.casualities)/100 + 0.5) for sq in self.squads if u'Fanatic' in [md.name for md in sq.mods]])))
        imp_num = float((sum([sq.count for sq in self.squads if u'Impetuous' in [md.name for md in sq.mods]])))
        imp_ts = float((sum([int(sq.ts*(100 - sq.casualities)/100 + 0.5) for sq in self.squads if u'Impetuous' in [md.name for md in sq.mods]])))
        fan_per = max(int((fan_num/squad_num)*100), int((fan_ts/armts)*100))
        imp_per = max(int((imp_num/squad_num)*100), int((imp_ts/armts)*100))
        return '\n Fanatics: %d \n Impetous: %d' % (fan_per, imp_per)

    def speed_calc(self):
        pass

    def get_transport_list(self):
        tranlst = {}
        for sq in self.squads:
            if sq.transport > 0:
               tran = {}
               tran['speed'] = sq.speed
               tran['space'] = sq.transport
               tran['free'] = sq.transport - sum(str.weight for str in sq.transporting)
               tran['transporting'] = ', '.join(['%s(%d)' % (str.name, str.weight)for str in sq.transporting])
               tran['name'] = sq.name
               tranlst[sq.id] = tran
        return tranlst