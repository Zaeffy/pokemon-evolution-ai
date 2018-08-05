from .retriever import Retriever


class Pokemons(Retriever):
    def __init__(self):
        super(Pokemons, self).__init__('pokemon')

    def _format_object(self, json):
        base_obj = {
            "stats": {
                "speed": 0,
                "special-defense": 0,
                "special-attack": 0,
                "defense": 0,
                "attack": 0,
                "hp": 0
            },
            "name": json["name"],
            "types": [],
            "moves": []
        }
        for stat in json['stats']:
            base_obj["stats"][stat['stat']['name']] = float(stat['base_stat'])
        for t in json['types']:
            base_obj['types'].append(Retriever.extract_id(t['type']['url'], 'type'))
        for move in json['moves']:
            can_use = False
            for group in move['version_group_details']:
                if group['version_group']['name'] == 'sun-moon':
                    can_use = True
                    break
            if can_use:
                base_obj['moves'].append(Retriever.extract_id(move['move']['url'], 'move'))
        return base_obj
