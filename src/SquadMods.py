__author__ = 'a.libkind'

from elixir import *


class SquadMods(Entity):
    using_options(tablename='mods')
    id = Field(Integer, autoincrement=True, primary_key=True)
    name = Field(Unicode, required=True)
    ts = Field(Integer, required=False, default=0)
    raise_cost = Field(Integer, required=False, default=0)
    supply = Field(Integer, required=False, default=0)
    weight = Field(Integer, required=False, default=0)
    tl = Field(Integer, required=False, default=0)
    squads = ManyToMany('ArmySquad')
    fields = [id, name, ts, raise_cost, supply, weight, tl]

    def __repr__(self):
        return 'Mod %s with %s' % (self.name, self.effect)