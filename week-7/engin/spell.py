class Spell:
    def __init__(self, name="Fireball", damage=30, mana_cost=50, cast_range=2):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    @property
    def get_spell(self):
        sepell_prop = {}
        sepell_prop['name'] = self.name
        sepell_prop['damage'] = self.damage
        sepell_prop['mana_cost'] = self.mana_cost
        sepell_prop['cast_range'] = self.cast_range
        return sepell_prop

    def __str__(self):
        return str(self.name) + ' ' + str(self.damage) + ' mana cost ' + str(self.mana_cost) + ' cast range ' + str(self.cast_range)
