"""
Module containing common fixtures
"""
from unittest.mock import MagicMock
import pytest
import pandas as pd
from pymongo import MongoClient

from src.models.csv_file_source import CsvFileSource


@pytest.fixture
def csv_file_source_fixture(tmpdir):
    """
    CsvFileSource fixture for testing
    """
    data = {'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}
    csv_file = tmpdir.join('test.csv')
    data_frame = pd.DataFrame(data)
    data_frame.to_csv(csv_file, index=False)
    return CsvFileSource(file_path=str(csv_file))


@pytest.fixture
def sample_data_fixture():
    '''
    Sample data fixture for testing
    '''
    return {
        'col1': [1, 2, 3],
        'col2': ['A', 'B', 'C'],
    }


@pytest.fixture
def mongo_client_fixture(monkeypatch):
    '''
    MongoClient fixture for testing
    '''
    mock_client = MagicMock(spec=MongoClient)
    monkeypatch.setattr(MongoClient, "__new__", lambda cls, *args, **kwargs: mock_client)

    return mock_client
