class URLBuilder:

    @staticmethod
    def buildCognitiveServicesEndpoints(serviceName):
        return f"https://{serviceName}.cognitiveservices.azure.com/"

    @staticmethod
    def buildCosmosDBEndpoints(databaseName):
        return f"https://{databaseName}.documents.azure.com:443/"