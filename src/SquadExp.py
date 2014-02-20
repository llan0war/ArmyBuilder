__author__ = 'a.libkind'

from elixir import *

class SquadExp(Entity):

    using_options(tablename='exp')
    id = Field(Integer, autoincrement=True, primary_key=True)
    name = Field(Unicode, required=True)
    squads = OneToMany('ArmySquad')
    ts = Field(Integer, required=True)
    raise_cost = Field(Integer, required=True)
    supply = Field(Integer, required=True)
    fields = [id, name]

    def __repr__(self):
        return 'Exp %s' % self.name

