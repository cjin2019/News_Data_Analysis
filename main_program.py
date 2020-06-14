from core.data_retriever import DataRetriever

if __name__ == '__main__':
    print('retrieving headlines and storing data in database...')
    DataRetriever.gather_all_data()
    print('finished retriving headlines')