from Services.TextAnalyticsService import TextAnalyticsService
from EntityNames import EntityNames

class TextAnalyticsProvider:

    def __init__(self) -> None:    
        service = TextAnalyticsService(EntityNames.azureCognitiveServiceName)
        self.textAnalyticsClient = service.createClient()

    def getHealthcareEntities(self, document):
        return self.textAnalyticsClient.begin_analyze_healthcare_entities(document)