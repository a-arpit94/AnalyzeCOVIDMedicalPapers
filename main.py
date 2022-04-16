from Providers.MachineLearningProvider import MachineLearningProvider
from Providers.TextAnalyticsProvider import TextAnalyticsProvider
from Providers.CosmosDBProvider import CosmosDBProvider
from Models.HealthcareRelation import HealthcareRelation
from Models.HealthcareEntity import HealthcareEntity
from Models.AnalyzeHealthcareEntitiesResult import AnalyzeHealthcareEntitiesResult

def main():
    MEDICAL_PAPER_COUNT = 1
    dataset = MachineLearningProvider().getMLDataset(numberOfRows = 1)
    
    # listOfMedPaperAbstracts = dataset['abstract'].astype(str).values.tolist()
    db = CosmosDBProvider()

    CHUNK_SIZE = 1

    for i in range(0, len(dataset), CHUNK_SIZE):
        temp_abstract_list = [dataset.loc[i+a, 'abstract'] for a in range(CHUNK_SIZE)]
        
        poller =  TextAnalyticsProvider().getHealthcareEntities(document = temp_abstract_list)
        textAnalysisResult = list(poller.result())
        
        for idx, item in enumerate(textAnalysisResult):
            entities = []
            entity_relations = []

            for entity in item.entities:
                healthcareEntity = HealthcareEntity(entity)
                entities.append(healthcareEntity.to_dict())

            for relation in item.entity_relations:
                healthcareRelation = HealthcareRelation(relation)
                entity_relations.append(healthcareRelation.to_dict())
            
            analyzeHealthcareEntitiesResult = AnalyzeHealthcareEntitiesResult(dataset.loc[i+idx], entities, entity_relations)
            db.upsertDataToContainer(analyzeHealthcareEntitiesResult.to_dict())
            print("Medical Paper Processed:", MEDICAL_PAPER_COUNT)
            MEDICAL_PAPER_COUNT+=1


if __name__ == "__main__":
    main()
