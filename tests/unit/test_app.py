'''
Module for defining the App class tests.

This module contains  tests for the App class using the pytest framework.

Tests:
    test_run: Test for the 'run' method of the App class.
    test_create_csv_file_sources: Test for the 'create_csv_file_sources' method of the App class.
'''

from unittest.mock import MagicMock, call
import pytest

from src import App
from src.models.csv_file_source import CsvFileSource
from src.models.csv_file_extractor import CsvFileExtractor
from src.models.df_transformer import DataFrameRowDictTransformer
from src.models.mongodb_loader import MongoDBLoader, MongoDBStorage

def test_run(monkeypatch):
    '''
    Test for the 'run' method of the App class.
    '''
    file_paths = ['/path/to/file1.csv', '/path/to/file2.csv']

    csv_file_sources = [
        CsvFileSource(file_path=file_paths[0]),
        CsvFileSource(file_path=file_paths[1]),
    ]

    mock_source = MagicMock(return_value=csv_file_sources)
    monkeypatch.setattr(App, 'create_csv_file_sources', mock_source)

    extracted_data_iterator = [
        MagicMock(),
        MagicMock(),
    ]

    mock_extract = MagicMock(return_value=extracted_data_iterator)
    monkeypatch.setattr(CsvFileExtractor, 'extract', mock_extract)

    transformed_data = MagicMock()


    mock_transformer = MagicMock(return_value=transformed_data)
    monkeypatch.setattr(DataFrameRowDictTransformer, 'transform', mock_transformer)

    mock_loader = MagicMock()
    monkeypatch.setattr(MongoDBLoader, 'load', mock_loader)

    def mock_init(_):
        pass

    monkeypatch.setattr(MongoDBStorage, '__init__', mock_init)

    App.run(file_paths)
    App.create_csv_file_sources.assert_called_once_with(file_paths)

    mock_extract.assert_called_once()

    assert mock_transformer.call_count == len(extracted_data_iterator)

    assert mock_loader.call_count == len(extracted_data_iterator)

    expected_calls = [call(input_data=transformed_data) for _ in extracted_data_iterator]
    mock_loader.assert_has_calls(expected_calls)

@pytest.mark.parametrize(
    "file_paths, expected_sources",
    [
        (['file1.csv'], [CsvFileSource(file_path='file1.csv')]),
        (
            ['file1.csv', 'file2.csv', 'file3.csv'],
            [
                CsvFileSource(file_path='file1.csv'),
                CsvFileSource(file_path='file2.csv'),
                CsvFileSource(file_path='file3.csv')
            ]
        )
    ]
)
def test_create_csv_file_sources(file_paths, expected_sources):
    '''
    Test for the 'create_csv_file_sources' method of the App class.
    '''
    sources = App.create_csv_file_sources(file_paths)
    assert len(sources) == len(expected_sources)
    for i, expected_source in enumerate(expected_sources):
        assert isinstance(sources[i], CsvFileSource)
        assert sources[i].file_path == expected_source.file_path
