from typing import List, Dict
from pymongo import MongoClient

from src.interfaces.loader import Loader
from src.interfaces.storage import Storage
from src.configs.mongodb import MongoDBConfigs

class MongoDBStorage(Storage):
    def __init__(self) -> None:
        super().__init__()
        self.client = MongoClient(
            host=MongoDBConfigs.HOST,
            port=MongoDBConfigs.PORT,
            username=MongoDBConfigs.USERNAME,
            password=MongoDBConfigs.PASSWORD,
        )
        
        self.initialize_database()
       
        
    def initialize_database(self):
        self.database = self.client[MongoDBConfigs.MONGO_DATABASE]
        self.collection = self.database[MongoDBConfigs.INVESTMENT_COLLECTION]
        
        index_info = self.collection.index_information()
        index_name = f'{MongoDBConfigs.SEARCH_QUERY_COLUMN}_text'
        if index_name not in index_info:
            self.collection.create_index([(MongoDBConfigs.SEARCH_QUERY_COLUMN, 'text')], name=index_name)
    
    def save(self, input_data: List[Dict]) -> None:
        self.collection.insert_many(input_data)

class MongoDBLoader(Loader):

    def __init__(self, mongo_storage: MongoDBStorage, chunk_size: int = MongoDBConfigs.DEFAULT_CHUNK_SIZE):
        super().__init__(storage=mongo_storage)
        self.chunk_size = chunk_size
        
    def load(self, input_data: List[Dict]):
        total_size = len(input_data)
        for data_ix in range(0, total_size, self.chunk_size):
            start, end = data_ix, data_ix + self.chunk_size
            data_chunk = input_data[start:end]
            self.storage.save(data_chunk)