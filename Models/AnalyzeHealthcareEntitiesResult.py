import uuid
from datetime import datetime

class AnalyzeHealthcareEntitiesResult:
    
    def __init__(self, dataset, entities, entity_relations) -> None:
        self.dataset = dataset
        self.entities = entities
        self.entity_relations = entity_relations

    def to_dict(result):
        if isinstance(result, AnalyzeHealthcareEntitiesResult):
            source_x = result.dataset['source_x'].split('; ') if ';' in result.dataset['source_x'] else result.dataset['source_x']

            authors = None
            if result.dataset['authors'] is not None:
                authors = result.dataset['authors'].split('; ') if ';' in result.dataset['authors'] else result.dataset['authors']

            dict = {
                'id': result.dataset['cord_uid'],
                'cord_uid': result.dataset['cord_uid'],
                'source_x': source_x,
                'title': result.dataset['title'],
                'doi': result.dataset['doi'],
                'pmcid': result.dataset['pmcid'],
                'pubmed_id': f"{result.dataset['pubmed_id']}",
                'license': result.dataset['license'],
                'abstract': result.dataset['abstract'],
                'publish_time': f"{result.dataset['publish_time'].date()}",
                'authors': authors,
                'journal': result.dataset['journal'],
                'arxiv_id': result.dataset['arxiv_id'],
                's2_id': result.dataset['s2_id'],
                'entities': result.entities,
                'entity_relations': result.entity_relations
            }
            return dict
        else:
            type_name = result.__class__.__name__
            raise TypeError("MY LOG >> Unexpected type {0}".format(type_name))