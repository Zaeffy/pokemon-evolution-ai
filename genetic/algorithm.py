from .population import Population


class Algorithm(object):
    def __init__(self, pokemons_list, moves_list, types_list):
        self._population = Population(pokemons_list, moves_list)
        self._types = types_list
        self._moves = moves_list
        self._pokemons = pokemons_list
        print("Initialize population...")
        self._population.populate()
        print("Population ready.")
        self._generation = 0

    def __str__(self):
        res = "Here is a subset of the current population (generation " + str(self._generation) + "):\n"
        res += str(self._population)
        return res

    def run_generations(self, generations):
        print("Starting " + str(generations) + " generations. Please wait, this may take some time.")
        for i in range(generations):
            self._population.evaluate(self._types)
            new_population = Population(self._pokemons, self._moves)
            new_population.reproduce(self._population.population)
            self._generation += 1
            print("Done " + str(i + 1) + "/" + str(generations) + " generations (Total " + str(self._generation) + ")")
            print(self._population)
            self._population = new_population
        print("Done generations.")
