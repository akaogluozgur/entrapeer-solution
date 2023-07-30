'''
App class' module
'''

from typing import List
from loguru import logger

from src.models.csv_file_source import CsvFileSource
from src.models.csv_file_extractor import CsvFileExtractor
from src.models.df_transformer import DataFrameRowDictTransformer
from src.models.mongodb_loader import MongoDBLoader, MongoDBStorage

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

        extracted_data_iterator = CsvFileExtractor(csv_file_sources).extract()
        logger.info(f'Extracted from {csv_file_sources}.')

        storage = MongoDBStorage()
        loader = MongoDBLoader(mongo_storage=storage)

        for index, extracted_data in enumerate(extracted_data_iterator):
            transformed_data = DataFrameRowDictTransformer(input_df=extracted_data).transform()
            logger.info(f'Transformed the extracted data part:{index}.')

            loader.load(input_data=transformed_data)
            logger.info(f'Loaded the transformed data part:{index}')

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
