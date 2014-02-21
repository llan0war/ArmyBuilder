__author__ = 'a.libkind'

from elixir import *

class SquadTypes(Entity):

    using_options(tablename='params')
    name = Field(Text, required=True)
    squads = ManyToMany('SquadTemplate')
    armies = ManyToMany('Army')
    armsquad = ManyToMany('ArmySquad')
    fields = [id, name]

    def __repr__(self):
        return 'Param ' + self.name
