__author__ = 'a.libkind'

from elixir import *
from sqlalchemy import select, func

class Army(Entity):

    using_options(tablename='army')
    squads = OneToMany('ArmySquad')
    name = Field(Unicode, required=True)
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
        #int(self.templ.ts * (100 + max(sum([md.ts for md in modes]), -80))/100 + 0.5)

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
            tmpsquad = []
            #['Name', 'TS', 'Raise', 'Supply', 'Weight', 'TL', 'Type', 'Mods', 'Casualities']
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
            res['squads'].append(tmpsquad)
        #[self.name, str(self.ts), str(self.raise_cost), str(self.supply), str(self.weight), str(self.tl), ','.join([t.name for t in self.type]), ','.join([t.name for t in self.mods]), str(self.casualities)]
        return res

    def typelist(self):

        typecoll = {}
        for sq in self.squads:
            for t in sq.type:
                typecoll[t.name] = 0

        for sq in self.squads:
            for t in sq.type:
                typecoll[t.name] += int(int(sq.ts*(100 - sq.casualities)/100 + 0.5))

        res = 'Army: %s \n' % (self.name)
        res = res + '\n'.join(['%s: %s' % (key, val) for key, val in typecoll.iteritems()])
        return res

