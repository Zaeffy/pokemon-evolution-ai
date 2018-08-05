# Pokemon fight simulator

This tool is a example of genetic algorithm applied to pokemon fighting.

Details about the algorithm and the idea behind it can be found [on Twitter](https://twitter.com/Vent_Ouest/status/1026144423594344448).

## How to use

### Pre-requisites

This code is meant to be used in _python3_ only (python2 will fail). You also need to have _requests_.

```bash
# pip3 install -r requirements.txt
```

### Importing the database

The database used in this tool must be extracted from [PokeApi](https://www.pokeapi.co). This database is not included in this repository to avoid legal problems. You have to extract it using the `construct_db` script.

__Important note__: you only have to do this step once. Please, do not do it multiple time to avoid overloading the API, it's a great (and free) service!

To extract the database, use:

```bash
# python3 construct_db.py
```   

This will create three json files (`move.json`, `pokemon.json` and `type.json`) in the data folder.

### Running the script

Now that you have the data you need, you can run the simulation using the `simulator` script:

```bash
# python3 simulator.py
```