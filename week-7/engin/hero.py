from unit import Unit


class Hero(Unit):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate

    def __str__(self):
        return self.known_as()

    def known_as(self):
        return f'{self.name} the {self.title}'
