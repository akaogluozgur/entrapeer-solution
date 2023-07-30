'''
transformer.py - Module for defining the Transformer abstract class.
'''

from abc import ABC, abstractmethod
from typing import Any

class Transformer(ABC):
    '''
    Abstract base class for data transformers.

    This class defines an abstract interface for data transformers. Subclasses should inherit
    from this class and implement the 'transform()' method to provide data transformation
    functionality.

    Methods:
        __init__(input_data: Any) -> None:
            Constructor for the Transformer class.
            
        transform(input: Any) -> Any:
            Abstract method to be implemented by subclasses for data transformation.
    '''

    def __init__(self, input_data: Any) -> None: # pragma: no cover
        """
        Constructor for the Extractor class.

        Args:
            input_data (Any): Any object representing the input data from 
            which the transformer will transform the data
            from.
        """
        super().__init__()
        self.input_data = input_data

    @abstractmethod
    def transform(self) -> Any: # pragma: no cover
        """
        Abstract method to be implemented by subclasses for data transformation.

        Args:
            input_data (Any): The input data to be transformed.

        Returns:
            Any: The transformed data after applying the transformation.
        """
        raise NotImplementedError()

    def __str__(self) -> str: # pragma: no cover
        """
        String representation of the Transformer object.

        Returns:
            str: The string representation of the Transformer object.
        """
        raise NotImplementedError()
