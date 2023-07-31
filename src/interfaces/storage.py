"""
storage.py - Module for defining the Storage abstract class.
"""
from abc import ABC, abstractmethod
from typing import Iterable


class Storage(ABC):
    """
    Abstract base class for data storage.

    This class defines an abstract interface for different types of data storage.
    Subclasses should inherit from this class and implement the 'save' method to
    provide data loading functionality.

    Methods:
        save(input_data: Iterable) -> None:
            Abstract method to be implemented by subclasses for loading data from storage.
    """

    @abstractmethod
    def save(self, input_data: Iterable) -> None:  # pragma: no cover
        """
        Abstract method for loading data from storage.

        Subclasses should implement this method to provide functionality for loading data from
        a specific data storage.

        Args:
            input_data (Iterable): An iterable of input data needed for loading (e.g., file paths,
            database connections, etc.).

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError()

    def __str__(self):  # pragma: no cover
        """
        Default string representation for the Storage class.
        """
        raise NotImplementedError()
