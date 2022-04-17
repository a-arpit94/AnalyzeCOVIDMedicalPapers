
from datetime import datetime
from EntityNames import EntityNames
from Services.MachineLearningService import MachineLearningService

class MachineLearningProvider:

    def __init__(self) -> None:
        self.ml = MachineLearningService(EntityNames.resourcegroup, EntityNames.mlworkspace)

    def getMLDataset(self, numberOfRows=1000, probability=100):
        dataset = self.ml.getDataset(EntityNames.mldataset)
    
        # return (dataset.take(numberOfRows).time_after(datetime(2003, 1, 1)).to_pandas_dataframe())
        # return (dataset.with_timestamp_columns(timestamp='publish_time').time_after(datetime(2022, 1, 1)).to_pandas_dataframe())
        #return (dataset.with_timestamp_columns(timestamp='publish_time').time_after(datetime(2019, 12, 12)).take(numberOfRows).to_pandas_dataframe())
        return (dataset.with_timestamp_columns(timestamp = 'publish_time').time_after(datetime(2019, 12, 12)).take_sample(probability).to_pandas_dataframe())
        #return (dataset.take(numberOfRows).to_pandas_dataframe())