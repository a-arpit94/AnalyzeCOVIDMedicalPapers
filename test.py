from Providers.MachineLearningProvider import MachineLearningProvider


def main():
    print("working")
    dataset = MachineLearningProvider().getMLDataset(probability = 0.012)

    CHUNK_SIZE = 50

    num = len(dataset) - (len(dataset) % CHUNK_SIZE)
    # num = 5622 - (5622 % CHUNK_SIZE)
    print(dataset.shape)
    print(num)
    # print(dataset.cord_uid[0])

    # for i in range(0, len(dataset)):
        # print(dataset.iloc[i])
        # print("-------")
    # for index, i in enumerate(dataset):
        # print(i['cord_uid'])
    # for i in range(len(dataset)):
        # print(dataset.loc[i, 'cord_uid'], dataset.loc[i, 'publish_time']) 



main()