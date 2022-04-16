from AzureCredentials import AzureCredentials
from azure.ai.textanalytics import TextAnalyticsClient
from Builders.URLBuilder import URLBuilder

class TextAnalyticsService:

    def __init__(self, cognitiveServiceName):
        self.credential = AzureCredentials.getCognitiveServicesCredentials(cognitiveServiceName)
        self.endpoint = URLBuilder.buildCognitiveServicesEndpoints(cognitiveServiceName)
        
    def createClient(self):    
        text_analytics_client = TextAnalyticsClient(endpoint = self.endpoint, credential = self.credential)
        return text_analytics_client
