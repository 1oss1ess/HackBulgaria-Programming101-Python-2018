from unit import Unit


class Enemy(Unit):

    def __init__(self, health=100, mana=100, damage=20):
        super().__init__(health, mana)
        self.attack_points = damage

    def __repr__(self):
        return '{} with {}/{} health/mana'.format(Enemy.__name__, self.current_health, self.current_mana)


enemy1 = Enemy(100, 100, 20)
print(enemy1.attack_points)
