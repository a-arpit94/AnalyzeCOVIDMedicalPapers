from azure.core.credentials import AzureKeyCredential
from EntityNames import EntityNames

class AzureCredentials:
    
    @staticmethod
    def getCognitiveServicesCredentials(serviceName):
        return AzureKeyCredential(EntityNames.AZURE_COGNITIVE_SERVICES_API_KEY[serviceName])

    # @staticmethod
    # def getCosmosDBCredentials(dbName):
    #     return AzureKeyCredential(EntityNames.AZURE_COSMOSDB_KEY[dbName])