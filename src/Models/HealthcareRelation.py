class HealthcareRelation:
    
    def __init__(self, relation) -> None:
        self.relation_type = relation.relation_type
        self.roles = relation.roles
    
    def to_dict(hcr):
        if isinstance(hcr, HealthcareRelation):
            roles = []
            if hcr.roles is not None:
                for r in hcr.roles:
                    roles.append({
                        'name':r.name,
                        'entity_text': r.entity.text,
                        'entity_normalized_text': r.entity.normalized_text,
                        'entity_category': r.entity.category,
                        'entity_subcategory': r.entity.subcategory
                        
                    })
            dict = {
                'relation_type': hcr.relation_type,
                'roles': roles
            }
            return dict
        else:
            type_name = hcr.__class__.__name__
            raise TypeError("MY LOG >> Unexpected type {0}".format(type_name))
