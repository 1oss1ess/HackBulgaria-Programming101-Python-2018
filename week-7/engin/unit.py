from weapon import Weapon
from spell import Spell


class Unit:
    def __init__(self, health, mana):
        if self.validate_value(health):
            raise TypeError('Value must be a number!')
        if self.validate_value(mana):
            raise TypeError('Value must be a number!')
        self.health = health
        self.mana = mana
        self.__max_hp = health
        self.__max_mana = mana
        self.weapon = None
        self.spell = None

    @staticmethod
    def validate_value(val):
        if val < 0:
            raise ValueError('Value cannot be negative!')
        if not isinstance(val, (int, float)):
            return True
        return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        if self.health <= 0:
            return False
        return True

    def can_cast(self):
        if not self.has_spell():
            return False
        if self.spell.mana_cost > self.mana:
            return False
        return True

    def has_weapon(self):
        return self.weapon is not None

    def has_spell(self):
        return self.spell is not None

    def take_damage(self, damage):
        if self.validate_value(damage):
            raise TypeError('Enter valid damage!')

        if self.health - damage < 0:
            self.health = 0
        else:
            self.health -= damage

    def take_healing(self, healing_points):
        if self.validate_value(healing_points):
            raise TypeError('Enter valid healing points!')

        if not self.is_alive():
            return 'Cannot heal a corpse!'

        if self.health + healing_points > self.__max_hp:
            self.health = self.__max_hp
        else:
            self.health += healing_points

    def take_mana(self, mana_points):
        if self.validate_value(mana_points):
            raise TypeError('Enter valid mana points!')

        if self.mana + mana_points > self.__max_mana:
            self.mana = self.__max_mana
        else:
            self.mana += mana_points

    def equip_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            raise TypeError('Weapon must be instance of Weapon!')
        else:
            self.weapon = weapon

    def learn_spell(self, spell):
        if not isinstance(spell, Spell):
            raise TypeError('Spell mist be instance of Spell!')
        else:
            self.spell = spell

    def get_damage_source(self):
        if self.has_spell() and self.has_weapon():
            if self.spell.damage >= self.weapon.damage:
                if self.can_cast():
                    return 'spell'
            return 'weapon'

        elif self.has_spell():
            if self.can_cast():
                return 'spell'

        elif self.has_weapon():
            return 'weapon'

        else:
            return None

    def attack(self, by=''):
        if by not in ('weapon', 'spell', ''):
            raise Exception('Enter valid attack type!')
        if by == 'weapon':
            if self.weapon is None:
                raise Exception('No Weapon!')
            return self.weapon.damage
        if by == 'spell':
            if not self.has_spell():
                raise Exception('No Spell Learned!')
            if self.can_cast():
                self.mana -= self.spell.mana_cost
                return self.spell.damage
            else:
                raise Exception('Not Enough Mana!')
        else:
            return None
