import json
from EntityNames import EntityNames
from Services.CosmosDBService import CosmosDBService


class CosmosDBProvider:

    def __init__(self) -> None:
        cosmosClient = CosmosDBService(EntityNames.cosmosDBAccountName)
        cosmosClient.setDatabase(EntityNames.medPaperDBName)
        self.containerClient = cosmosClient.getDatabaseContainerClient( EntityNames.medPaperContainer)

    def upsertDataToContainer(self, data):
        self.containerClient.upsert_item(data)

    def getData(self):
        db_query = "select * from r "
        dic = []
        for item in self.containerClient.query_items(query= db_query, enable_cross_partition_query=True):
            i = json.dumps(item, indent = True)
            dic.append(i)
        return dic

    # Append each item as a dictionary to list
        # dflist.append(dict(item))
        # self.containerClient.