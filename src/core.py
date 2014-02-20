__author__ = 'a.libkind'

import os
from elixir import *
from src import SquadTemplate, ArmySquad, SquadTypes, SquadMods, Army, SquadMobility, SquadEquip, SquadExp

dbdir = os.path.join(os.getcwd(), "db")
dbfile = os.path.join(dbdir, "army.sqlite")

saveData = None

def calc_all():
    quer = ArmySquad.ArmySquad.query.all()
    for cur, templ in enumerate(quer):
        templ.calc_all()
        templ.speed = speed_calcer(templ.mobility, templ.tl)
        emptysq = []
        if not templ.army:
            emptysq.append(templ)
    freearm = Army.Army.get_by(id=999)
    freearm.squads.extend(emptysq)
    quer = Army.Army.query.all()
    for cur, templ in enumerate(quer):
        templ.calcer()
    quer = SquadTemplate.SquadTemplate.query.all()
    for cur, templ in enumerate(quer):
        templ.speed = speed_calcer(templ.mobility, templ.tl)



    saveData()


def speed_calcer(mob, tl):
    if mob.name == u'Foot': res = u'%s/%s/%s' % ('20', '10', '0')
    elif mob.name == u'Mount': res = u'%s/%s/%s' % ('30', '15', '0')
    elif mob.name == u'Mechanized': res = u'%s/%s/%s' % (str(int(80+20*(tl-6))), str(int(60+15*(tl-6))), '0')
    elif mob.name == u'Motorized': res = u'%s/%s/%s' % (str(int(120+30*(tl-6))), str(int(20+5*(tl-6))), '0')
    elif mob.name == u'Immovable': res = u'%s/%s/%s' % ('0', '0', '0')

    elif mob.name == u'Coast': res = u'%s/%s/%s' % ('0', '0', str(int(160+40*(tl-3))))
    elif mob.name == u'Sea': res = u'%s/%s/%s' % ('0', '0', str(int(160+40*(tl-3))))
    elif mob.name == u'Fast air': res = u'%s/%s/%s' % ('9999', '9999', '9999')
    elif mob.name == u'Slow air': res = u'%s/%s/%s' % (str(int(100*(tl-5))), str(int(100*(tl-5))), str(int(100*(tl-5))))
    else: res = u'123/456/789'
    return res


def initDB():
    print dbfile
    if not os.path.isdir(dbdir):
        os.mkdir(dbdir)
    metadata.bind = "sqlite:///%s" % dbfile
    setup_all()
    first_time = os.path.exists(dbfile)
    if not first_time:
        create_all()

    # This is so Elixir 0.5.x and 0.6.x work
    # Yes, it's kinda ugly, but needed for Debian
    # and Ubuntu and other distros.

    global saveData
    import elixir
    if elixir.__version__ < "0.6":
        saveData = session.flush
    else:
        saveData = session.commit

    if not first_time:
        sampleArmy()


def sampleArmy():
    cavalery = SquadTypes.SquadTypes(name=u'Cavalery')
    recon = SquadTypes.SquadTypes(name=u'Recon')
    armor = SquadTypes.SquadTypes(name=u'Armor')
    naval = SquadTypes.SquadTypes(name=u'Naval')
    air = SquadTypes.SquadTypes(name=u'Air')
    artillery = SquadTypes.SquadTypes(name=u'Artillery')
    C3I = SquadTypes.SquadTypes(name=u'C3I')
    Engeneering = SquadTypes.SquadTypes(name=u'Engeneering')
    Fire = SquadTypes.SquadTypes(name=u'Fire')
    foot = SquadMobility.SquadMobility(name=u'Foot')
    mount = SquadMobility.SquadMobility(name=u'Mount')
    mechanized = SquadMobility.SquadMobility(name=u'Mechanized')
    motorized = SquadMobility.SquadMobility(name=u'Motorized')
    zero = SquadMobility.SquadMobility(name=u'Immovable')
    coast = SquadMobility.SquadMobility(name=u'Coast')
    sea = SquadMobility.SquadMobility(name=u'Sea')
    fair = SquadMobility.SquadMobility(name=u'Fast air')
    sair = SquadMobility.SquadMobility(name=u'Slow air')
    eq1 = SquadEquip.SquadEquip(name=u'Very Fine')
    eq2 = SquadEquip.SquadEquip(name=u'Fine')
    eq3 = SquadEquip.SquadEquip(name=u'Good')
    eq4 = SquadEquip.SquadEquip(name=u'Basic')
    eq5 = SquadEquip.SquadEquip(name=u'Poor')
    exp1 = SquadExp.SquadExp(name=u'Elite')
    exp2 = SquadExp.SquadExp(name=u'Good')
    exp3 = SquadExp.SquadExp(name=u'Average')
    exp4 = SquadExp.SquadExp(name=u'Inferior')
    templ99 = SquadTemplate.SquadTemplate(name=u'Magic Pony', mobility=foot, type=[naval, Fire], raise_cost=5, supply=5, weight=5, tl=5, ts=5)
    templ98 = SquadTemplate.SquadTemplate(name=u'Battle Pony', mobility=mount,  type=[armor], raise_cost=5, supply=5, weight=5, tl=4, ts=5)
    templ97 = SquadTemplate.SquadTemplate(name=u'Fly Pony', mobility=mechanized, type=[air, naval], raise_cost=5, supply=5, weight=5, tl=3, ts=5)
    templ96 = SquadTemplate.SquadTemplate(name=u'Pony1', mobility=foot, type=[naval, Fire], raise_cost=5, supply=5, weight=5, tl=5, ts=5)
    templ95 = SquadTemplate.SquadTemplate(name=u'Pony2', mobility=mount,  type=[armor], raise_cost=5, supply=5, weight=5, tl=4, ts=5)
    templ94 = SquadTemplate.SquadTemplate(name=u'Pony13', mobility=mechanized, type=[air, naval], raise_cost=5, supply=5, weight=5, tl=3, ts=5)
    hero = SquadMods.SquadMods(name=u'Hero', ts=100, raise_cost=100, supply=100)
    child = SquadMods.SquadMods(name=u'Child', ts=-50, raise_cost=-50, supply=-50)
    squad1 = ArmySquad.ArmySquad(name=u'Applejack', templ=templ99, mods=[hero], equip=eq4, exp=exp1)
    squad2 = ArmySquad.ArmySquad(name=u'Rarity', templ=templ98, equip=eq4, exp=exp1)
    squad3 = ArmySquad.ArmySquad(name=u'Fluttershy', templ=templ97, mods=[child], equip=eq4, exp=exp1)
    squad4 = ArmySquad.ArmySquad(name=u'nyan', templ=templ99, mods=[hero], equip=eq4, exp=exp1)
    squad5 = ArmySquad.ArmySquad(name=u'dsfdsfds', templ=templ99, mods=[hero], equip=eq4, exp=exp1)
    squad6 = ArmySquad.ArmySquad(name=u'2342352', templ=templ99, mods=[hero], equip=eq4, exp=exp1)
    squad7 = ArmySquad.ArmySquad(name=u'3dgfgdfgdf', templ=templ99, mods=[hero], equip=eq4, exp=exp1)
    army1 = Army.Army(name=u'Pony Force', squads=[squad1, squad2, squad3, squad4, squad5])
    army2 = Army.Army(name=u'Second Force', squads=[squad6, squad7])
    army3 = Army.Army(name=u'Free units', id=999, squads=[])
    saveData()
