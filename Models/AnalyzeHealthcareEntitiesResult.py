import uuid
class AnalyzeHealthcareEntitiesResult:
    
    def __init__(self, id, entities, entity_relations) -> None:
        self.id = id
        self.entities = entities
        self.entity_relations = entity_relations

    def to_dict(result):
        if isinstance(result, AnalyzeHealthcareEntitiesResult):
            dict = {
                'id': f'{uuid.uuid4()}',
                'entities': result.entities,
                'entity_relations': result.entity_relations
            }
            return dict
        else:
            type_name = result.__class__.__name__
            raise TypeError("MY LOG >> Unexpected type {0}".format(type_name))