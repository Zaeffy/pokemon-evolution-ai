from .retriever import Retriever


class Types(Retriever):
    def __init__(self):
        super(Types, self).__init__('type')

    def _format_object(self, json):
        obj = [1.0 for _ in range(0, 19)]
        for t in json['damage_relations']['no_damage_to']:
            obj[int(Retriever.extract_id(t['url'], 'type'))] = 0.0
        for t in json['damage_relations']['half_damage_to']:
            obj[int(Retriever.extract_id(t['url'], 'type'))] = 0.5
        for t in json['damage_relations']['double_damage_to']:
            obj[int(Retriever.extract_id(t['url'], 'type'))] = 2.0
        return obj
