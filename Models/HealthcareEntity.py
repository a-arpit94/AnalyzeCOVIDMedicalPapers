class HealthcareEntity:
    
    def __init__(self, entity) -> None:
        self.text = entity.text
        self.normalized_text = entity.normalized_text
        self.category = entity.category
        self.subcategory = entity.subcategory
        self.assertion = entity.assertion
        self.length = entity.length
        self.offset = entity.offset
        self.confidence_score = entity.confidence_score
        self.data_sources = entity.data_sources
    
    def to_dict(hce):
        if isinstance(hce, HealthcareEntity):
            hce_datasource = []
            if hce.data_sources is not None:
                for data_source in hce.data_sources:
                    hce_datasource.append({
                        'entity_id': data_source.entity_id,
                        'name': data_source.name
                    })

            assertionValue = None
            if hce.assertion is not None:
                assertionValue = {
                    'conditionality': hce.assertion.conditionality,
                    'certainty': hce.assertion.certainty,
                    'association': hce.assertion.association
                }

            dict = {
                'text': hce.text,
                'normalized_text': hce.normalized_text,
                'category': hce.category,
                'subcategory': hce.subcategory,
                'assertion': assertionValue,
                'length': hce.length,
                'offset': hce.offset,
                'confidence_score': hce.confidence_score,
                'data_source': hce_datasource
            }
            return dict
        else:
            type_name = hce.__class__.__name__
            raise TypeError("MY LOG >> Unexpected type {0}".format(type_name))
