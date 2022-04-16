from azureml.core import Workspace, Dataset
from AzureCredentials import AzureCredentials
from EntityNames import EntityNames

class MachineLearningService:

    def __init__(self, resourcegroup, mlWorkspace) -> None:
        self.resourcegroupName = resourcegroup
        self.mlWorkspace = mlWorkspace

    def getDataset(self, datasourcename):
        mlWorkspace = Workspace(EntityNames.SUBSCRIPTION_ID, self.resourcegroupName, self.mlWorkspace)
        dataset = Dataset.get_by_name(mlWorkspace, name = datasourcename)
        return dataset