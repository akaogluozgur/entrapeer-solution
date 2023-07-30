'''
loader.py - Module for defining the Loader abstract class.
'''
from abc import ABC, abstractmethod
from src.interfaces.storage import Storage

from typing import Iterable

class Loader(ABC):
    '''
    Abstract base class for data loaders.

    This class defines an abstract interface for different types of data loaders.
    Subclasses should inherit from this class and implement the 'load' method to
    provide data loading functionality.

    Attributes:
        storage (Storage): An instance of a class that implements the Storage interface, 
        representing the data storage from which data will be loaded.

    Methods:
        load(input_data: Iterable) -> None:
            Abstract method to be implemented by subclasses for loading data.
    '''
    def __init__(self, storage: Storage) -> None: # pragma: no cover
        '''
        Constructor for the Loader class.

        Args:
            storage (Storage): An instance of a class that implements the Storage interface,
            representing the data storage from which data will be loaded.
        '''
        super().__init__()
        self.storage = storage

    @abstractmethod
    def load(self, input_data: Iterable): # pragma: no cover
        '''
        Abstract method for loading data.

        Subclasses should implement this method to provide functionality for loading data from
        the specified data storage.

        Args:
            input_data (Iterable): An iterable of input data needed for loading (e.g., file paths,
            database connections, etc.).

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        '''
        raise NotImplementedError()
        