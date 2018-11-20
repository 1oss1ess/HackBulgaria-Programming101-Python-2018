from hero import Hero
from treasures import Treasures


class Dungeon:
    SPAWNING_POINT = 'S'
    EXIT = 'G'
    WALL = '#'
    WALKABLE_PATH = '.'
    TRESURE = 'T'
    ENEMY = 'E'
    HERO = "H"

    def __init__(self, dungeon_map):
        self.dungeon_map = open(dungeon_map)
        self.array_map = self.read_map
        self.hero_position = None
        self.enemy_position = None
        self.spawning_positions = self.find_spawining_points

    @property
    def read_map(self):
        row = self.dungeon_map.read()

        self.array_map = []

        for index in row.split():
            self.array_map.append(list(index))
        return self.array_map

    def print_map(self):
        return self.__str__()

    def close_file(self):
        if self.dungeon_map:
            self.dungeon_map.close()
            self.dungeon_map = None

    def __str__(self):
        return '\n'.join([''.join(line) for line in self.array_map])

    def spawn(self, hero):
        if type(hero) is not Hero:
            raise ThisIsNotAHero
        if len(self.spawning_positions) == 0:
            raise NoMoreSpawnPoints
        self.hero = hero
        self.hero_position = self.spawning_positions.pop(0)
        self.array_map[self.hero_position[0]][self.hero_position[1]] = Dungeon.HERO

    @property
    def find_spawining_points(self):
        spawn_points = []
        for cuurent_row, row in enumerate(self.array_map):
            for current_col, col in enumerate(row):
                if col == Dungeon.SPAWNING_POINT:
                    spawn_points.append((cuurent_row, current_col))
        return spawn_points

    def move_hero(self, direction):
        move_row, move_col = self.directions(direction)
        hero_row, hero_col = self.hero_position
        hero_future_position = (hero_row + move_row, hero_col + move_col)
        if self.array_map[hero_future_position[0]][hero_future_position[1]] is Dungeon.WALKABLE_PATH:
            self.hero_move_and_update_map(hero_future_position)
            return True
        elif self.array_map[hero_future_position[0]][hero_future_position[1]] is Dungeon.TRESURE:
            self.hero_move_and_update_map(hero_future_position)
            self.hero_found_treasure()
            return True
        elif self.array_map[hero_future_position[0]][hero_future_position[1]] is Dungeon.ENEMY:
            self.enemy_position = hero_future_position
            return True
        elif self.array_map[hero_future_position[0]][hero_future_position[1]] is Dungeon.EXIT:
            print('The hero is exit the dungeon')
            return True
        else:
            return False

    def hero_found_treasure(self):
        my_treasure = Treasures()
        found_treasure = my_treasure.pick_treasure()
        for index in found_treasure:
            if index is 'weapon':
                self.hero.equip_weapon(found_treasure[index])
            elif index is 'spell':
                self.hero.learn_spell(found_treasure[index])
            elif index == 'mana potion':
                self.hero.take_mana(found_treasure[index])
            elif index == 'health potion':
                self.hero.take_healing(found_treasure[index])
            print('Hero found treasure: {0} {1}'.format(index, found_treasure[index]))

    def hero_move_and_update_map(self, position):
        self.array_map[self.hero_position[0]][self.hero_position[1]] = Dungeon.WALKABLE_PATH
        self.hero_position = position
        self.array_map[self.hero_position[0]][self.hero_position[1]] = Dungeon.HERO
        return True

    def directions(self, direction):
        dict_directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'right': (0, 1),
            'left': (0, -1)
        }
        return dict_directions[direction]

    def hero_attack(self, by):
        pass


class ThisIsNotAHero(Exception):
    'Object is not a Hero instance'


class NoMoreSpawnPoints(Exception):
    'Ther is no more spawning positions'


map = Dungeon("level1.txt")
print(map.print_map())
print()
some_hero_instance = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
map.spawn(some_hero_instance)
print(map.print_map())
map.move_hero('right')
map.move_hero('up')
map.move_hero('down')
print()
print(map.print_map())
map.close_file()
