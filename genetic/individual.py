from random import randint

# Those values are "one out of..."
# Eg a crossover risk of 3 means one chance out of 3 (33%)
MUTATE_RISK = 3000
CROSSOVER_RISK = 3


# Note : pokemons list and moves list are in constructor because we need them to pretty print
class Individual(object):
    def __init__(self, pokemons_list, moves_list):
        self._dna = []
        self._pokemons = pokemons_list
        self._moves = moves_list
        self._score = 0

    def create_from_list(self):
        for i in range(6):
            pokemon = randint(0, len(self._pokemons) - 1)
            self._dna.append(pokemon)
            for _ in range(4):
                if len(self._pokemons[pokemon]['moves']) > 1:  # Some pokemon only have one move, this make randint crash
                    self._dna.append(randint(0, len(self._pokemons[pokemon]['moves']) - 1))
                else:
                    self._dna.append(0)

    def create_from_parents(self, parent1, parent2):
        from_parent1 = True
        for i in range(30):
            if i % 5 == 0 and randint(0, CROSSOVER_RISK) == 0:  # We want to keep pokemons "complete" so switch only on pokemon, not moves
                from_parent1 = not from_parent1
            new_value = parent1[i] if from_parent1 else parent2[i]
            if randint(0, MUTATE_RISK) == 0:
                new_value = new_value + randint(-10, 10)
            self._dna.append(new_value)

    @property
    def dna(self):
        return self._dna

    @property
    def score(self):
        return self._score

    def win(self):
        self._score += 1

    def __str__(self):
        res = "Team score: " + str(self._score) + "\n"
        for i in range(6):
            pokemon_id = self._dna[i * 5]
            if 0 <= pokemon_id < len(self._pokemons):
                moves = [self._dna[i * 5 + j + 1] for j in range(4)]
                pokemon = self._pokemons[pokemon_id]
                res += pokemon['name'] + "\t(Moves:"
                for j in moves:
                    if 0 <= j < len(pokemon['moves']):
                        res += " [" + self._moves[pokemon['moves'][j]]['name'] + "]"
                    else:
                        res += " [**Invalid move**]"
                res += ")"
            else:
                res += "[Invalid pokemon]"
            res += "\n"
        res += "\n"
        return res
