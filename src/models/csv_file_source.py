'''
csv_file_source.py - Module for defining the CsvFileSource class.

This module contains the implementation of the CsvFileSource class, which is a specific
implementation of the DataSource abstract class. It provides functionality to load data from
a CSV file.

Classes:
    CsvFileSource: A class for loading data from a CSV file.
'''

import pandas as pd

from src.interfaces.data_source import DataSource



class CsvFileSource(DataSource):
    '''
    CsvFileSource class for loading data from a CSV file.

    This class is a specific implementation of the DataSource abstract class,
    providing functionality to load data from a CSV file.

    Attributes:
        file_path (str): The file path of the CSV file from which data will be loaded.

    Methods:
        __init__(file_path: str) -> None:
            Constructor for the CsvFileSource class.

        load() -> pd.DataFrame:
            Method to load data from the CSV file as a pandas DataFrame.

        __str__() -> str:
            Returns a string representation of the CsvFileSource object.
    '''
    def __init__(self, file_path: str) -> None:
        """
        Constructor for the CsvFileSource class.

        Args:
            file_path (str): The file path of the CSV file from which data will be loaded.
        """
        super().__init__()
        self.file_path = file_path

    def load(self) -> pd.DataFrame:
        """
        Load data from the CSV file as a pandas DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing the data loaded from the CSV file.
        """
        return pd.read_csv(self.file_path)

    def __str__(self):
        """
        String representation of the CsvFileSource object.

        Returns:
            str: The file path of the CSV file.
        """
        return self.file_path
