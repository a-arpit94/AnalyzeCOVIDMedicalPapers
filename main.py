from Providers.MachineLearningProvider import MachineLearningProvider
from Providers.TextAnalyticsProvider import TextAnalyticsProvider
from Providers.CosmosDBProvider import CosmosDBProvider
from Models.HealthcareRelation import HealthcareRelation
from Models.HealthcareEntity import HealthcareEntity
from Models.AnalyzeHealthcareEntitiesResult import AnalyzeHealthcareEntitiesResult
import sys

def main():
    MEDICAL_PAPER_COUNT = 1
    dataset = MachineLearningProvider().getMLDataset(probability=0.015)
    
    # listOfMedPaperAbstracts = dataset['abstract'].astype(str).values.tolist()
    db = CosmosDBProvider()

    CHUNK_SIZE = 5
    num = len(dataset) - (len(dataset) % CHUNK_SIZE)

    try:
        for i in range(0, num, CHUNK_SIZE):
            try:
                temp_abstract_list = []
                temp_abstract_list = [dataset.abstract[i+a] for a in range(CHUNK_SIZE)]
                
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
                    
                    analyzeHealthcareEntitiesResult = AnalyzeHealthcareEntitiesResult(dataset.iloc[i+idx], entities, entity_relations)
                    db.upsertDataToContainer(analyzeHealthcareEntitiesResult.to_dict())
                    
                    print("Medical Paper Processed:", MEDICAL_PAPER_COUNT)
                    MEDICAL_PAPER_COUNT+=1
                
            except:
                print(f"ERROR OCCURRED FOR PAPER NUMBER {MEDICAL_PAPER_COUNT} :: {sys.exc_info()[0]}")
                MEDICAL_PAPER_COUNT+=1

    except:
        pass


if __name__ == "__main__":
    main()
