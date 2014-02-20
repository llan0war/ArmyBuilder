__author__ = 'a.libkind'

from elixir import *

class SquadEquip(Entity):

    using_options(tablename='equip')
    id = Field(Integer, autoincrement=True, primary_key=True)
    name = Field(Unicode, required=True)
    squads = OneToMany('ArmySquad')
    fields = [id, name]

    def __repr__(self):
        return 'Equip %s' % self.name

