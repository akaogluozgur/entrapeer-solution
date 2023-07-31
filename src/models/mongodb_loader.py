"""
Module for defining the MongoDBStorage and MongoDBLoader classes.

This module contains the implementation of the MongoDBStorage class, which is a specific
implementation of the Storage abstract class. It provides functionality to store data in a
MongoDB collection. Additionally, it includes the MongoDBLoader class, which is a specific
implementation of the Loader abstract class, providing functionality to load data into a
MongoDB collection in chunks.

Classes:
    MongoDBStorage: Class for handling data storage in MongoDB.
    MongoDBLoader: Class for loading data into MongoDB.
"""

from typing import List, Dict
from pymongo import MongoClient

from src.interfaces.loader import Loader
from src.interfaces.storage import Storage
from src.configs.mongodb import MongoDBConfigs


class MongoDBStorage(Storage):
    """
    MongoDBStorage class for handling data storage in MongoDB.

    This class is a specific implementation of the Storage abstract class,
    providing functionality to store data in a MongoDB collection.

    Attributes:
        client (MongoClient): A MongoClient instance representing the MongoDB client.
        name (str): The name of the MongoDB database.

    Methods:
        __init__() -> None:
            Constructor for the MongoDBStorage class.
        initialize_database() -> None:
            Initialize the MongoDB database and collection.
        save(input_data: List[Dict]) -> None:
            Save the input data in the MongoDB collection.
        __str__() -> str:
            Returns a string representation of the MongoDBStorage object.
    """

    def __init__(self) -> None:
        """
        Constructor for the MongoDBStorage class.

        Initializes the MongoDB client and database.
        """
        super().__init__()
        self.client = MongoClient(
            host=MongoDBConfigs.HOST,
            port=MongoDBConfigs.PORT,
            username=MongoDBConfigs.USERNAME,
            password=MongoDBConfigs.PASSWORD,
        )
        self.name = MongoDBConfigs.MONGO_DATABASE
        self.initialize_database()

    def initialize_database(self):
        """
        Initialize the MongoDB database and collection.

        If the specified text index does not exist, it creates the text index
        for the source_description column.
        """
        self.database = self.client[MongoDBConfigs.MONGO_DATABASE]
        self.collection = self.database[MongoDBConfigs.INVESTMENT_COLLECTION]

        index_info = self.collection.index_information()
        index_name = f'{MongoDBConfigs.SEARCH_QUERY_COLUMN}_text'
        if index_name not in index_info:
            self.collection.create_index(
                [(MongoDBConfigs.SEARCH_QUERY_COLUMN, 'text')],
                name=index_name
            )

    def save(self, input_data: List[Dict]) -> None:
        """
        Save the input data in the MongoDB collection.

        Args:
            input_data (List[Dict]): A list of dictionaries representing the data to be stored.
        """
        self.collection.insert_many(input_data)

    def __str__(self):  # pragma: no cover
        """
        String representation of the MongoDBStorage object.

        Returns:
            str: The string representation of the MongoDBStorage object.
        """
        return str(self.name)


class MongoDBLoader(Loader):
    """
    MongoDBLoader class for loading data into MongoDB.

    This class is a specific implementation of the Loader abstract class,
    providing functionality to load data into a MongoDB collection.

    Attributes:
        storage (MongoDBStorage): An instance of MongoDBStorage representing the MongoDB collection
            where data will be loaded.
        chunk_size (int): The number of documents to insert in a single batch.

    Methods:
        __init__(mongo_storage: MongoDBStorage,
        chunk_size: int = MongoDBConfigs.DEFAULT_CHUNK_SIZE) -> None:
            Constructor for the MongoDBLoader class.
        load(input_data: List[Dict]) -> None:
            Load the input data into the MongoDB collection in chunks.
        __str__() -> str:
            Returns a string representation of the MongoDBLoader object.
    """

    def __init__(
            self, mongo_storage: MongoDBStorage,
            chunk_size: int = MongoDBConfigs.DEFAULT_CHUNK_SIZE
    ):
        """
        Constructor for the MongoDBLoader class.

        Args:
            mongo_storage (MongoDBStorage): An instance of MongoDBStorage representing the
            MongoDB collection where data will be loaded.
            chunk_size (int, optional): The number of documents to insert in a single batch.
            Default is MongoDBConfigs.DEFAULT_CHUNK_SIZE.
        """
        super().__init__(storage=mongo_storage)
        self.chunk_size = chunk_size

    def load(self, input_data: List[Dict]):
        """
        Load the input data into the MongoDB collection in chunks.

        Args:
            input_data (List[Dict]): A list of dictionaries representing the data to be loaded.
        """
        total_size = len(input_data)
        for data_ix in range(0, total_size, self.chunk_size):
            start, end = data_ix, data_ix + self.chunk_size
            data_chunk = input_data[start:end]
            self.storage.save(data_chunk)

    def __str__(self):  # pragma: no cover
        """
        String representation of the MongoDBLoader object.

        Returns:
            str: The string representation of the MongoDBLoader object.
        """
        return str(self.storage)
