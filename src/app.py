'''
App class' module
'''

from typing import List
from loguru import logger

from src.models.csv_file_source import CsvFileSource
from src.models.csv_file_extractor import CsvFileExtractor


class App:
    '''
    App class that contains solution steps.
    '''
    @staticmethod
    def run(file_paths:List[str]) -> None:
        """
        Executes the application logic using the provided list of file paths.

        Args:
            file_paths (List[str]): A list of file paths for CSV files to process.
        """
        logger.info(f'Running for {file_paths}.')
        csv_file_sources = App.create_csv_file_sources(file_paths)
        logger.info(f'Extracted from {csv_file_sources}.')
        extracted_data = CsvFileExtractor(csv_file_sources).extract()

    @staticmethod
    def create_csv_file_sources(file_paths:List[str]) -> List[CsvFileSource]:
        """
        Creates a list of CsvFileSource objects based on the provided list of file paths.

        Args:
            file_paths (List[str]): A list of file paths for CSV files.

        Returns:
            List[CsvFileSource]: A list of CsvFileSource objects created from the file paths.
        """
        csv_file_sources = [
            CsvFileSource(file_path=file_path)
            for file_path in file_paths
        ]
        return csv_file_sources