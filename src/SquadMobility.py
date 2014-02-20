__author__ = 'a.libkind'

from elixir import *

class SquadMobility(Entity):

    using_options(tablename='mobility')
    id = Field(Integer, autoincrement=True, primary_key=True)
    name = Field(Unicode, required=True)
    squads = OneToMany('ArmySquad')
    templ = OneToMany('SquadTemplate')
    fields = [id, name]

    def __repr__(self):
        return 'Mobility %s' % self.name

