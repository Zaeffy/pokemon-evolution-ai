import os
from json import load
from genetic import Algorithm


move_file = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "move.json"))
pokemon_file = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "pokemon.json"))
type_file = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "type.json"))

with open(move_file, "r") as fp:
    moves = load(fp)
    print("Loaded " + str(len(moves)) + " moves.")
with open(pokemon_file, "r") as fp:
    pokemons = load(fp)
    print("Loaded " + str(len(pokemons)) + " pokemons.")
with open(type_file, "r") as fp:
    types = load(fp)
    print("Loaded " + str(len(types)) + " types.")

algorithm = Algorithm(pokemons, moves, types)
print(algorithm)

generations = 1
while generations > 0:
    print("To exit, enter 0.")
    try:
        generations = int(input("Number of generation to simulate: "))
    except ValueError:
        print("Invalid generation count, exiting.")
        generations = 0
    if generations > 0:
        algorithm.run_generations(generations)
