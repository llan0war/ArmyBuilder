__author__ = 'a.libkind'

from elixir import *

class SquadMobility(Entity):

    using_options(tablename='mobility')
    id = Field(Integer, autoincrement=True, primary_key=True)
    name = Field(Text, required=True)
    comment = Field(Text, required=False, default='')
    squads = OneToMany('ArmySquad')
    templ = OneToMany('SquadTemplate')
    fields = [id, name, comment]

    def __repr__(self):
        return 'Mobility %s' % self.name

