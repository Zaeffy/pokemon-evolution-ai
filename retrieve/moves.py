from .retriever import Retriever


class Move(Retriever):
    def __init__(self):
        super(Move, self).__init__('move')

    def _format_object(self, json):
        return {
            'name': json['name'],
            'priority': int(json['priority']) if json['priority'] else 0,
            'power': float(json['power']) if json['power'] else 0,
            'accuracy': int(json['accuracy']) if json['accuracy'] else 0,
            'special': json['damage_class']['name'] == 'special',
            'type': Retriever.extract_id(json['type']['url'], 'type')
        }
