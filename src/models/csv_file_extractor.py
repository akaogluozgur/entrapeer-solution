"""
Module for defining the CsvFileExtractor class.

This module contains the CsvFileExtractor class, which is a specific implementation of the Extractor
abstract class. It provides functionality to extract data from CSV file sources.

Classes:
    CsvFileExtractor: A class for extracting data from CSV file sources.
"""
from typing import List, Iterable
import pandas as pd

from src.interfaces.extractor import Extractor
from src.models.csv_file_source import CsvFileSource


class CsvFileExtractor(Extractor):
    """
    CsvFileExtractor class for extracting data from CSV file sources.

    This class is a specific implementation of the Extractor abstract class,
    providing functionality to extract data from CSV file sources.

    Attributes:
        csv_file_sources (List[CsvFileSource]): A list of CsvFileSource objects representing
        the CSV file sources from which data will be extracted.

    Methods:
        __init__(csv_file_sources: List[CsvFileSource]) -> None:
            Constructor for the CsvFileExtractor class.

        extract() -> Iterable[pd.DataFrame]:
            Method to extract data from CSV file sources.

        __str__() -> str:
        Returns a string representation of the CsvFileExtractor object.
    """

    def __init__(self, csv_file_sources: List[CsvFileSource]) -> None:
        """
        Constructor for the CsvFileExtractor class.

        Args:
            csv_file_sources (List[CsvFileSource]): A list of CsvFileSource objects representing 
            the CSV file sources from which data will be extracted.
        """
        super().__init__(data_sources=csv_file_sources)

    def extract(self) -> Iterable[pd.DataFrame]:
        """
        Extract data from CSV file sources.

        This method iterates through the list of CsvFileSource objects and yields pandas DataFrames,
        each representing the data extracted from a CSV file.

        Yields:
            pd.DataFrame: A DataFrame containing the extracted data from a CSV file.
        """
        for source in self.data_sources:
            yield source.load()

    def __str__(self):  # pragma: no cover
        return ', '.join([str(source) for source in self.data_sources])
