'''
extractor.py - Module for defining the Extractor abstract class.
'''
from abc import ABC, abstractmethod
from typing import List, Iterable

from src.interfaces.data_source import DataSource

class Extractor(ABC):
    '''
    Abstract base class for data extractors.

    This class defines an abstract interface for extracting data from different data sources.
    Subclasses should inherit from this class and implement the 'extract()' method to
    provide data extraction functionality.

    Attributes:
        data_sources (List[DataSource]): A list of DataSource objects representing the data
            sources from which the extractor will retrieve data.

    Methods:
        __init__(data_sources: List[DataSource]) -> None:
            Constructor for the Extractor class.

        extract() -> Iterable:
            Abstract method to be implemented by subclasses for data extraction.
    '''
    @abstractmethod
    def __init__(self, data_sources: List[DataSource]) -> None:
        """
        Constructor for the Extractor class.

        Args:
            data_sources (List[DataSource]): A list of DataSource objects representing the data
                sources from which the extractor will retrieve data.
        """
        super().__init__()
        self.data_sources = data_sources

    @abstractmethod
    def extract(self) -> Iterable: # pragma: no cover
        """
        Abstract method to be implemented by subclasses for data extraction.

        This method must be implemented by subclasses to provide data extraction functionality
        from the specified data sources. The method should return the extracted data as an iterable.

        Returns:
            Iterable: The extracted data as an iterable.

        Raises:
            NotImplementedError: This method is abstract and must be implemented in subclasses.
        """
        raise NotImplementedError()

    def __str__(self):
        '''
        Default string representation for the DataSource class.
        '''
        raise NotImplementedError()
