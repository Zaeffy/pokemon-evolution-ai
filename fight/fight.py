from random import choice
from .team import Team


class Fight(object):
    def __init__(self, team1, team2, pokemons_list, moves_list, types_list):
        self._team1 = Team(team1, pokemons_list, moves_list, types_list)
        self._team2 = Team(team2, pokemons_list, moves_list, types_list)

    def fight(self):
        max_turn = 100  # We need to limit the max number of turn to avoid being stuck if no player have attack
        while not (self._team1.lost or self._team2.lost):
            (priority1, attack1) = self._team1.action(self._team2.pokemon)
            (priority2, attack2) = self._team2.action(self._team1.pokemon)

            if priority1 > priority2 or \
                (priority1 == priority2 and self._team1.pokemon.speed > self._team2.pokemon.speed) or \
                    (priority1 == priority2 and self._team1.pokemon.speed == self._team2.pokemon.speed and choice([True, False])):
                self._team2.hit(attack1)
                if self._team2.lost:
                    return True, False
                self._team1.hit(attack2)
                if self._team1.lost:
                    return False, True
            else:
                self._team1.hit(attack2)
                if self._team1.lost:
                    return False, True
                self._team2.hit(attack1)
                if self._team2.lost:
                    return True, False
            max_turn -= 1
            if max_turn <= 0:
                return False, False
        return self._team2.lost, self._team1.lost
