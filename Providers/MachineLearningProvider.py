
from EntityNames import EntityNames
from Services.MachineLearningService import MachineLearningService

class MachineLearningProvider:

    def __init__(self) -> None:
        self.ml = MachineLearningService(EntityNames.resourcegroup, EntityNames.mlworkspace)

    def getMLDataset(self, numberOfRows):
        dataset = self.ml.getDataset(EntityNames.mldataset)
        return (dataset.take(numberOfRows).to_pandas_dataframe())