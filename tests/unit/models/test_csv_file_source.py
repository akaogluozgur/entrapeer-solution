import pytest

from src.app import CsvFileSource
import pandas as pd


def test_csv_file_source_load(csv_file_source_fixture):
    df = csv_file_source_fixture.load()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert set(df.columns) == {'col1', 'col2'}


def test_csv_file_source_invalid_file():
    invalid_file_path = '/path/to/invalid/file.csv'
    with pytest.raises(FileNotFoundError):
        CsvFileSource(file_path=invalid_file_path).load()


def test_csv_file_source_empty_file(tmpdir):
    empty_file = tmpdir.join('empty.csv')
    open(empty_file, 'w').close()

    with pytest.raises(pd.errors.EmptyDataError):
        CsvFileSource(file_path=str(empty_file)).load()
