import random


class Pokemon(object):
    def __init__(self, pokemon, selected_moves, moves_list, types_list):
        self._name = pokemon['name']
        self._stats = pokemon['stats']
        self._types_id = pokemon['types']
        self._types = [types_list[t] for t in pokemon['types']]
        self._moves = [moves_list[pokemon['moves'][m]] if 0 <= m < len(pokemon['moves']) else None for m in selected_moves]
        self._hp = self._stats['hp']

    @property
    def defense(self):
        return self._stats['defense']

    @property
    def special_defense(self):
        return self._stats['special-defense']

    @property
    def speed(self):
        return self._stats['speed']

    @property
    def alive(self):
        return self._hp > 0

    def type_effect(self, target_type):
        res = 1
        for t in self._types:
            res = res * t[target_type]
        return res

    def attack(self, target):
        move = None
        if not any(self._moves):
            return 0, 0
        while move is None:
            move = self._moves[random.randint(0, 3)]
        if move['special']:
            attack = self._stats['special-attack']
            defense = float(target.special_defense)
        else:
            attack = float(self._stats['attack'])
            defense = float(target.defense)
        defense = 1 if defense == 0.0 else defense
        base_damage = (22.0 * float(move['power']) * (attack / defense)) / 50.0 + 2.0
        critical = 1.5 if random.random() < 4.167 else 1.0
        rand = random.uniform(0.85, 1.0)
        stab = 1.5 if move['type'] in self._types_id else 1
        types = target.type_effect(move['type'])
        hit = 0 if random.randint(0, 100) > move['accuracy'] else 1
        return move['priority'], base_damage * critical * rand * stab * types * hit

    def damage(self, amount):
        self._hp -= amount
        return self._hp > 0
