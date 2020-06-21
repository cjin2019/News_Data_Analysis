from core.data_retriever import DataRetriever

if __name__ == '__main__':
    print('retrieving headlines and storing data in core.database...')
    data_retriever = DataRetriever()
    data_retriever.gather_all_data()
    print('finished retriving headlines')