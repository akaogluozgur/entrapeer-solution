"""
Abstract base class for data sources with an abstract method 'load()' to be implemented by
subclasses for loading data as a pandas DataFrame.
"""
from abc import ABC, abstractmethod
import pandas as pd


class DataSource(ABC):
    """Abstract base class for data sources.
    
        This class defines an abstract interface for loading data from different sources.
        Subclasses should inherit from this class and implement the 'load()' method to
        provide data loading functionality.
        
        Methods:
            load(): Abstract method to be implemented by subclasses for loading data.
    """

    @abstractmethod
    def load(self) -> pd.DataFrame:  # pragma: no cover
        """
        Abstract method to be implemented by subclasses for loading data.

        Returns:
            pd.DataFrame: The loaded data as a pandas DataFrame.

        Raises:
            NotImplementedError: This method is abstract and must be implemented in subclasses.
        """
        raise NotImplementedError()

    def __str__(self):  # pragma: no cover
        raise NotImplementedError()
