class Weapon:
    def __init__(self, name="The Axe of Destiny", damage=20):
        self.name = name
        self.damage = damage

    @property
    def get_weapon(self):
        weapon_prop = {}
        weapon_prop['name'] = self.name
        weapon_prop['damage'] = self.damage
        return weapon_prop

    def __str__(self):
        return str(self.name) + ' ' + str(self.damage)
