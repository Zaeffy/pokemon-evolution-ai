from random import choice
from threading import Thread
from fight import Fight
from .individual import Individual


POPULATION_SIZE = 1000
MATCH_PER_TEAM = 30


class ThreadedFight(Thread):
    def __init__(self, team1, team2, pokemons_list, moves_list, types_list):
        super(ThreadedFight, self).__init__()
        self._team1 = team1
        self._team2 = team2
        self._pokemons = pokemons_list
        self._moves = moves_list
        self._types = types_list

    def run(self):
        fight = Fight(self._team1.dna, self._team2.dna, self._pokemons, self._moves, self._types)
        (victory1, victory2) = fight.fight()
        if victory1:
            self._team1.win()
        if victory2:
            self._team2.win()


class Population(object):
    def __init__(self, pokemons_list, moves_list):
        self._individuals = []
        self._pokemons = pokemons_list
        self._moves = moves_list

    @property
    def population(self):
        return self._individuals

    def populate(self):
        for i in range(POPULATION_SIZE):
            individual = Individual(self._pokemons, self._moves)
            individual.create_from_list()
            self._individuals.append(individual)

    def evaluate(self, types_list):
        i = 0
        for pokemon1 in self._individuals:
            threads = []
            for _ in range(MATCH_PER_TEAM):
                pokemon2 = choice(self._individuals)
                fight = ThreadedFight(pokemon1, pokemon2, self._pokemons, self._moves, types_list)
                fight.start()
                threads.append(fight)
            for thread in threads:
                thread.join()
            i += 1
            print("Done pokemon " + str(i) + "/" + str(len(self._individuals)), end="\r")

    def reproduce(self, original_population):
        classified_array = []
        for individual in original_population:
            for i in range(individual.score + 1):
                classified_array.append(individual)
        for i in range(POPULATION_SIZE):
            individual = Individual(self._pokemons, self._moves)
            parent1 = choice(classified_array)
            parent2 = choice(classified_array)
            individual.create_from_parents(parent1.dna, parent2.dna)
            self._individuals.append(individual)
        return True

    def __str__(self):
        self._individuals.sort(key=lambda elem: -elem.score)  # We want to see the best ones
        res = "Top 3 team:\n"
        for i in self._individuals[:3]:
            res += str(i)
        res += "Flop 3 team:\n"
        for i in self._individuals[-3:]:
            res += str(i)
        return res
