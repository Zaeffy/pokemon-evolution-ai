from random import choice, randint
from .pokemon import Pokemon


class Team(object):
    def __init__(self, dna, pokemons_list, moves_list, types_list):
        self._pokemons = []
        self._current = None
        self._alive = 0
        for i in range(6):
            pokemon = dna[i * 5]
            moves = [dna[i * 5 + j + 1] for j in range(4)]
            if 0 <= pokemon < len(pokemons_list):
                self._pokemons.append(Pokemon(pokemons_list[pokemon], moves, moves_list, types_list))
                self._alive += 1
        if self._pokemons:
            self._current = choice(self._pokemons)

    @property
    def lost(self):
        return self._alive == 0

    @property
    def pokemon(self):
        return self._current

    def _change_pokemon(self):
        new_pokemon = self._current
        while new_pokemon == self._current or new_pokemon is None or not new_pokemon.alive:
            new_pokemon = choice(self._pokemons)
        self._current = new_pokemon

    def action(self, target):
        if self._alive > 1 and randint(0, 100) < 10:
            self._change_pokemon()
            return 1000, 0
        else:
            ret = self._current.attack(target)
            return ret

    def hit(self, amount):
        if not self._current.damage(amount):
            self._alive -= 1
            if self._alive > 0:
                self._change_pokemon()
