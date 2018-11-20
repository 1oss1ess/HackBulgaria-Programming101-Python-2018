from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell
from fight import Fight


h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)
h.equip_weapon(w)
s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
h.learn_spell(s)
e = Enemy()
f = Fight(h, e)
f.start_fight()
