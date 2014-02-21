__author__ = 'a.libkind'

import os
from elixir import *
from src import SquadTemplate, ArmySquad, SquadTypes, SquadMods, Army, SquadMobility, SquadEquip, SquadExp

dbdir = os.path.join(os.getcwd(), "db")
dbfile = os.path.join(dbdir, "army.sqlite")

saveData = None

def calc_all():
    quer = SquadTemplate.SquadTemplate.query.all()
    for cur, templ in enumerate(quer):
        templ.speed = speed_calcer(templ.mobility, templ.tl)
    quer = ArmySquad.ArmySquad.query.all()
    emptysq = []
    for cur, templ in enumerate(quer):
        templ.calc_all()
        templ.speed = speed_calcer(templ.mobility, templ.tl, (True if u'Hovercraft' in [nm.name for nm in templ.mods] else False))
        if not templ.army:
            emptysq.append(templ)
    freearm = Army.Army.get_by(name=u'Free units')
    freearm.squads.extend(emptysq)
    quer = Army.Army.query.all()
    for cur, templ in enumerate(quer):
        templ.calcer()
    saveData()


def speed_calcer(mob, tl, hov=False):
    if mob.name == u'Foot': res = u'%s/%s/%s' % ('20', '10', '0')
    elif mob.name == u'Mount': res = u'%s/%s/%s' % ('30', '15', '0')
    elif mob.name == u'Mechanized': res = u'%s/%s/%s' % (str(int(80+20*(tl-6))), str(int(60+15*(tl-6))), '0')
    elif mob.name == u'Motorized':
        if hov:
            res = u'%s/%s/%s' % (str(int(80+20*(tl-6))), str(int(60+15*(tl-6))), str(int(160+40*(tl-3))))
        else:
            res = u'%s/%s/%s' % (str(int(120+30*(tl-6))), str(int(20+5*(tl-6))), '0')
    elif mob.name == u'Immovable': res = u'%s/%s/%s' % ('0', '0', '0')
    elif mob.name == u'Coast':
        if hov:
            res = u'%s/%s/%s' % (str(int((80+20*(tl-6))), str(int(60+15*(tl-6))), str(int(160+40*(tl-3)))))
        else:
            res = u'%s/%s/%s' % ('0', '0', str(int(160+40*(tl-3))))
    elif mob.name == u'Sea': res = u'%s/%s/%s' % ('0', '0', str(int(160+40*(tl-3))))
    elif mob.name == u'Fast air': res = u'Unlimited'
    elif mob.name == u'Slow air': res = u'%s' % (str(int(100*(tl-5))))
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
    Cavalery = SquadTypes.SquadTypes(name=u'Cavalery')
    Recon = SquadTypes.SquadTypes(name=u'Recon')
    Armor = SquadTypes.SquadTypes(name=u'Armor')
    Naval = SquadTypes.SquadTypes(name=u'Naval')
    Air = SquadTypes.SquadTypes(name=u'Air')
    Artillery = SquadTypes.SquadTypes(name=u'Artillery')
    C3I = SquadTypes.SquadTypes(name=u'C3I')
    Engeneering = SquadTypes.SquadTypes(name=u'Engeneering')
    Fire = SquadTypes.SquadTypes(name=u'Fire')
    Foot = SquadMobility.SquadMobility(name=u'Foot')
    Mount = SquadMobility.SquadMobility(name=u'Mount')
    Mechanized = SquadMobility.SquadMobility(name=u'Mechanized')
    Motorized = SquadMobility.SquadMobility(name=u'Motorized')
    Zero = SquadMobility.SquadMobility(name=u'Immovable')
    Coast = SquadMobility.SquadMobility(name=u'Coast')
    Sea = SquadMobility.SquadMobility(name=u'Sea')
    Fair = SquadMobility.SquadMobility(name=u'Fast air')
    Sair = SquadMobility.SquadMobility(name=u'Slow air')
    eq1 = SquadEquip.SquadEquip(name=u'Very Fine', ts=150, raise_cost=200, supply=150)
    eq2 = SquadEquip.SquadEquip(name=u'Fine', ts=100, raise_cost=100, supply=100)
    eq3 = SquadEquip.SquadEquip(name=u'Good', ts=50, raise_cost=50, supply=50)
    eq4 = SquadEquip.SquadEquip(name=u'Basic', ts=0, raise_cost=0, supply=0)
    eq5 = SquadEquip.SquadEquip(name=u'Poor', ts=-25, raise_cost=-25, supply=-25)
    exp1 = SquadExp.SquadExp(name=u'Elite', ts=100, raise_cost=200, supply=40)
    exp2 = SquadExp.SquadExp(name=u'Good', ts=50, raise_cost=100, supply=20)
    exp3 = SquadExp.SquadExp(name=u'Average', ts=0, raise_cost=0, supply=0)
    exp4 = SquadExp.SquadExp(name=u'Inferior', ts=-50, raise_cost=-50, supply=-50)
    templ99 = SquadTemplate.SquadTemplate(name=u'Magic Pony', mobility=Foot, type=[Naval, Fire], raise_cost=5, supply=5, weight=5, tl=5, ts=5)
    templ98 = SquadTemplate.SquadTemplate(name=u'Battle Pony', mobility=Mount,  type=[Armor], raise_cost=5, supply=5, weight=5, tl=4, ts=5)
    templ97 = SquadTemplate.SquadTemplate(name=u'Fly Pony', mobility=Mechanized, type=[Air, Naval], raise_cost=5, supply=5, weight=5, tl=3, ts=5)
    templ96 = SquadTemplate.SquadTemplate(name=u'Pony1', mobility=Foot, type=[Naval, Fire], raise_cost=5, supply=5, weight=5, tl=5, ts=5)
    templ95 = SquadTemplate.SquadTemplate(name=u'Pony2', mobility=Mount,  type=[Armor], raise_cost=5, supply=5, weight=5, tl=4, ts=5)
    templ94 = SquadTemplate.SquadTemplate(name=u'Pony13', mobility=Mechanized, type=[Air, Naval], raise_cost=5, supply=5, weight=5, tl=3, ts=5)
    templ1 = SquadTemplate.SquadTemplate(name=u'Bowmen', mobility=Foot, type=[Fire], raise_cost=40, supply=8, weight=1, tl=2, ts=2, support=False)
    templ2 = SquadTemplate.SquadTemplate(name=u'Balloon', mobility=Zero, type=[Air], raise_cost=50, supply=5, weight=2, tl=5, ts=1, support=True)
    templ3 = SquadTemplate.SquadTemplate(name=u'Cavalry Pistol', mobility=Mount, type=[Cavalery, Fire], raise_cost=100, supply=20, weight=2, tl=4, ts=3, support=False)
    templ4 = SquadTemplate.SquadTemplate(name=u'Cavalry Pistol', mobility=Mount, type=[Cavalery, Fire], raise_cost=100, supply=20, weight=2, tl=5, ts=6, support=False)
    templ5 = SquadTemplate.SquadTemplate(name=u'Draft Team', mobility=Mount, type=[], raise_cost=100, supply=10, weight=2, tl=1, ts=0, support=False, transport=2)
    templ6 = SquadTemplate.SquadTemplate(name=u'Heavy Artillery', mobility=Foot, type=[Artillery], raise_cost=100, supply=10, weight=2, tl=2, ts=3, support=True)
    templ7 = SquadTemplate.SquadTemplate(name=u'Heavy Artillery', mobility=Foot, type=[Artillery], raise_cost=100, supply=10, weight=2, tl=3, ts=5, support=True)
    templ8 = SquadTemplate.SquadTemplate(name=u'Heavy Artillery', mobility=Foot, type=[Artillery], raise_cost=100, supply=10, weight=2, tl=4, ts=10, support=True)
    templ9 = SquadTemplate.SquadTemplate(name=u'Heavy Artillery', mobility=Foot, type=[Artillery], raise_cost=100, supply=10, weight=2, tl=5, ts=20, support=True)
    templ10 = SquadTemplate.SquadTemplate(name=u'Light Artillery', mobility=Foot, type=[Artillery], raise_cost=40, supply=8, weight=1, tl=2, ts=1, support=True)
    templ11 = SquadTemplate.SquadTemplate(name=u'Light Artillery', mobility=Foot, type=[Artillery], raise_cost=40, supply=8, weight=1, tl=3, ts=2, support=True)
    templ12 = SquadTemplate.SquadTemplate(name=u'Light Artillery', mobility=Foot, type=[Artillery], raise_cost=40, supply=8, weight=1, tl=4, ts=4, support=True)
    templ13 = SquadTemplate.SquadTemplate(name=u'Light Artillery', mobility=Foot, type=[Artillery], raise_cost=40, supply=8, weight=1, tl=5, ts=8, support=True)
    templ14 = SquadTemplate.SquadTemplate(name=u'Light Cavalry', mobility=Mount, type=[Cavalery, Recon], raise_cost=100, supply=20, weight=2, tl=2, ts=2, support=False)
    templ15 = SquadTemplate.SquadTemplate(name=u'medium Cavalry', mobility=Mount, type=[Cavalery, Fire], raise_cost=150, supply=30, weight=2, tl=2, ts=3, support=False)
    templ16 = SquadTemplate.SquadTemplate(name=u'Heavy Cavalry', mobility=Mount, type=[Cavalery], raise_cost=200, supply=40, weight=2, tl=2, ts=5, support=False)
    templ17 = SquadTemplate.SquadTemplate(name=u'Light Chariot', mobility=Mount, type=[Cavalery, Fire], raise_cost=100, supply=20, weight=4, tl=1, ts=2, support=False)
    templ18 = SquadTemplate.SquadTemplate(name=u'Heavy Chariot', mobility=Mount, type=[Cavalery], raise_cost=160, supply=32, weight=4, tl=1, ts=4, support=False)
    templ19 = SquadTemplate.SquadTemplate(name=u'Light Infantry', mobility=Foot, type=[Recon], raise_cost=40, supply=8, weight=1, tl=1, ts=2, support=False)
    templ20 = SquadTemplate.SquadTemplate(name=u'Medium Infantry', mobility=Foot, type=[], raise_cost=30, supply=6, weight=1, tl=1, ts=3, support=False)
    templ21 = SquadTemplate.SquadTemplate(name=u'Heavy Infantry', mobility=Foot, type=[], raise_cost=40, supply=8, weight=1, tl=2, ts=4, support=False)
    templ22 = SquadTemplate.SquadTemplate(name=u'Horse Artillery', mobility=Mount, type=[Artillery], raise_cost=150, supply=30, weight=2, tl=5, ts=10, support=False)
    templ24 = SquadTemplate.SquadTemplate(name=u'Line Infantry', mobility=Foot, type=[Fire], raise_cost=30, supply=6, weight=1, tl=5, ts=3, support=False)
    templ25 = SquadTemplate.SquadTemplate(name=u'Horse Archer', mobility=Mount, type=[Cavalery, Fire, Recon], raise_cost=120, supply=24, weight=2, tl=2, ts=2, support=False)
    templ26 = SquadTemplate.SquadTemplate(name=u'Miners', mobility=Foot, type=[Engeneering], raise_cost=30, supply=6, weight=1, tl=2, ts=1, support=True)
    templ27 = SquadTemplate.SquadTemplate(name=u'Miners', mobility=Foot, type=[Engeneering], raise_cost=30, supply=6, weight=1, tl=3, ts=1, support=True)
    templ28 = SquadTemplate.SquadTemplate(name=u'Miners', mobility=Foot, type=[Engeneering], raise_cost=30, supply=6, weight=1, tl=4, ts=2, support=True)
    templ29 = SquadTemplate.SquadTemplate(name=u'Miners', mobility=Foot, type=[Engeneering], raise_cost=30, supply=6, weight=1, tl=5, ts=4, support=True)
    templ30 = SquadTemplate.SquadTemplate(name=u'Mounts', mobility=Mount, type=[], raise_cost=60, supply=8, weight=1, tl=1, ts=0, support=False, transport=1)
    templ31 = SquadTemplate.SquadTemplate(name=u'Musketeers', mobility=Foot, type=[Fire], raise_cost=30, supply=6, weight=1, tl=4, ts=3, support=False)
    templ32 = SquadTemplate.SquadTemplate(name=u'Skirmishers', mobility=Foot, type=[Recon, Fire], raise_cost=30, supply=6, weight=1, tl=5, ts=3, support=False)
    templ33 = SquadTemplate.SquadTemplate(name=u'Stone-Age Warriors', mobility=Foot, type=[Recon], raise_cost=25, supply=5, weight=1, tl=0, ts=1, support=False)
    templ34 = SquadTemplate.SquadTemplate(name=u'War Beast', mobility=Foot, type=[Armor], raise_cost=400, supply=80, weight=4, tl=2, ts=20, support=False)
    templ35 = SquadTemplate.SquadTemplate(name=u'Boat', mobility=Coast, type=[], raise_cost=5, supply=1, weight=1, tl=1, ts=0, support=False, transport=1)
    templ36 = SquadTemplate.SquadTemplate(name=u'Large Boat', mobility=Coast, type=[], raise_cost=10, supply=1, weight=2, tl=1, ts=0, support=False, transport=2)
    templ37 = SquadTemplate.SquadTemplate(name=u'Light Galley', mobility=Coast, type=[], raise_cost=70, supply=14, weight=99, tl=1, ts=3, support=False, transport=1)
    templ38 = SquadTemplate.SquadTemplate(name=u'Longship', mobility=Coast, type=[], raise_cost=150, supply=30, weight=99, tl=2, ts=3, support=False, transport=7)
    templ39 = SquadTemplate.SquadTemplate(name=u'War Galley', mobility=Coast, type=[Naval], raise_cost=500, supply=100, weight=99, tl=2, ts=10, support=False, transport=3)
    templ40 = SquadTemplate.SquadTemplate(name=u'Cog', mobility=Sea, type=[], raise_cost=75, supply=8, weight=99, tl=3, ts=4, support=False, transport=5)
    templ41 = SquadTemplate.SquadTemplate(name=u'Brig', mobility=Sea, type=[Naval, Artillery], raise_cost=150, supply=15, weight=99, tl=4, ts=6, support=False, transport=6)
    templ42 = SquadTemplate.SquadTemplate(name=u'Galleon', mobility=Sea, type=[Naval, Artillery], raise_cost=750, supply=75, weight=99, tl=4, ts=30, support=False, transport=6)
    templ43 = SquadTemplate.SquadTemplate(name=u'Frigate', mobility=Sea, type=[Naval, Artillery], raise_cost=1000, supply=50, weight=99, tl=5, ts=150, support=False, transport=4)
    templ44 = SquadTemplate.SquadTemplate(name=u'Ship-of-the-Line', mobility=Sea, type=[Naval, Artillery], raise_cost=4000, supply=400, weight=99, tl=5, ts=300, support=False, transport=10)
    templ45 = SquadTemplate.SquadTemplate(name=u'Aquatic Warriors', mobility=Coast, type=[Naval], raise_cost=30, supply=6, weight=1, tl=0, ts=2, support=False)
    templ46 = SquadTemplate.SquadTemplate(name=u'Battle Mages', mobility=Foot, type=[Artillery, C3I, Fire, Recon], raise_cost=200, supply=40, weight=1, tl=0, ts=5, support=False)
    templ47 = SquadTemplate.SquadTemplate(name=u'Beasts', mobility=Mount, type=[Cavalery, Recon], raise_cost=50, supply=10, weight=2, tl=0, ts=1, support=False)
    templ48 = SquadTemplate.SquadTemplate(name=u'Flying Beasts', mobility=Sair, type=[Air], raise_cost=120, supply=40, weight=2, tl=0, ts=1, support=False, transport=1)
    templ49 = SquadTemplate.SquadTemplate(name=u'Flying Cavalery', mobility=Sair, type=[Air, Fire], raise_cost=600, supply=60, weight=2, tl=1, ts=2, support=False)
    templ50 = SquadTemplate.SquadTemplate(name=u'Flying Infantry', mobility=Sair, type=[Air, Recon], raise_cost=60, supply=20, weight=2, tl=0, ts=2, support=False)
    templ51 = SquadTemplate.SquadTemplate(name=u'Flying Leviathan', mobility=Sair, type=[Air], raise_cost=1000, supply=40, weight=99, tl=0, ts=150, support=False, transport=10)
    templ52 = SquadTemplate.SquadTemplate(name=u'Ogres', mobility=Foot, type=[], raise_cost=80, supply=8, weight=4, tl=0, ts=8, support=False)
    hero = SquadMods.SquadMods(name=u'Hero', ts=100, raise_cost=100, supply=100)
    child = SquadMods.SquadMods(name=u'Child', ts=-50, raise_cost=-50, supply=-50)
    Fanatic = SquadMods.SquadMods(name=u'Fanatic')
    Flagship = SquadMods.SquadMods(name=u'Flagship')
    Hovercraft = SquadMods.SquadMods(name=u'Hovercraft')
    SuperSoldier = SquadMods.SquadMods(name=u'Super-Soldier')
    Impetuous = SquadMods.SquadMods(name=u'Impetuous')
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
