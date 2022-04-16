from Providers.MachineLearningProvider import MachineLearningProvider
from Providers.TextAnalyticsProvider import  TextAnalyticsProvider
from Providers.CosmosDBProvider import CosmosDBProvider
from Models.HealthcareEntity import HealthcareEntity
from Models.HealthcareRelation import HealthcareRelation
from Models.AnalyzeHealthcareEntitiesResult import AnalyzeHealthcareEntitiesResult

def main():
    
    document = MachineLearningProvider().getMLDataset(numberOfRows = 2)
    
    poller =  TextAnalyticsProvider().getHealthcareEntities(document = document)
    res = list(poller.result())
    
    print("##############")

    db = CosmosDBProvider()
    for idx, item in enumerate(res):
        entities = []
        entity_relations = []
        print("START ITEM", idx)
        for entity in item.entities:
            healthcareEntity = HealthcareEntity(entity)
            entities.append(healthcareEntity.to_dict())

        for relation in item.entity_relations:
            healthcareRelation = HealthcareRelation(relation)
            entity_relations.append(healthcareRelation.to_dict())

        analyzeHealthcareEntitiesResult = AnalyzeHealthcareEntitiesResult(idx, entities, entity_relations)
        db.upsertDataToContainer(analyzeHealthcareEntitiesResult.to_dict())
        print("END ITEM", idx)

    # for idx, doc in enumerate(res):
    #     for entity in doc.entities:
    #         print(f"Entity: {entity.text}")
    #         print(f"...Normalized Text: {entity.normalized_text}")
    #         print(f"...Category: {entity.category}")
    #         print(f"...Subcategory: {entity.subcategory}")
    #         print(f"...Confidence score: {entity.confidence_score}")
    #         if entity.data_sources is not None:
    #             print("...Data Sources:")
    #             for data_source in entity.data_sources:
    #                 print(f"......Entity ID: {data_source.entity_id}")
    #                 print(f"......Name: {data_source.name}")
    #         if entity.assertion is not None:
    #             print("...Assertion:")
    #             print(f"......Conditionality: {entity.assertion.conditionality}")
    #             print(f"......Certainty: {entity.assertion.certainty}")
    #             print(f"......Association: {entity.assertion.association}")
    #     for relation in doc.entity_relations:
    #         print(f"Relation of type: {relation.relation_type} has the following roles")
    #         for role in relation.roles:
    #             print(f"...Role '{role.name}' with entity '{role.entity.text}'")
    #     print("------------------------------------------")
    print("##############")



if __name__ == "__main__":
    main()
