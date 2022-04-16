from Builders.URLBuilder import URLBuilder
from azure.cosmos import CosmosClient
from EntityNames import EntityNames

class CosmosDBService:

    def __init__(self, cosmosAccountName):
        cosmosURI = URLBuilder.buildCosmosDBEndpoints(cosmosAccountName)
        self.cosmosClient = CosmosClient(cosmosURI, EntityNames.AZURE_COSMOSDB_KEY[cosmosAccountName])
    
    def setDatabase(self, databaseName):
        self.cosmosClient.create_database_if_not_exists(id = databaseName)
        self.dbClient = self.cosmosClient.get_database_client(databaseName)

    def getDatabaseContainerClient(self, containerName):
        # self.dbClient.create_container_if_not_exists(id = containerName, partition_key=PartitionKey(path="/lastName"), offer_throughput=1000)
        return self.dbClient.get_container_client(containerName)
    