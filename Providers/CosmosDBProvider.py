
from EntityNames import EntityNames
from Services.CosmosDBService import CosmosDBService


class CosmosDBProvider:

    def __init__(self) -> None:
        cosmosClient = CosmosDBService(EntityNames.cosmosDBAccountName)
        cosmosClient.setDatabase(EntityNames.medPaperDBName)
        self.containerClient = cosmosClient.getDatabaseContainerClient( EntityNames.medPaperContainer)

    def upsertDataToContainer(self, data):
        self.containerClient.upsert_item(data)