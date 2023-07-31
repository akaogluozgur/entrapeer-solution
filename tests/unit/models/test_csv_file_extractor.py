import pytest
import pandas as pd

from src.models.csv_file_source import CsvFileSource
from src.models.csv_file_extractor import CsvFileExtractor


@pytest.mark.parametrize("file_paths, expected_num_dataframes", [
    ([], 0),
    (
            [
                'path/to/file1.csv',
                'path/to/file2.csv',
                'path/to/file3.csv',
            ], 3
    ),
    (
            [
                'path/to/file1.csv',
            ], 1
    ),
])
def test_extract(file_paths, expected_num_dataframes, sample_data_fixture):
    class MockCsvFileSource(CsvFileSource):
        def load(self) -> pd.DataFrame:
            return pd.DataFrame(sample_data_fixture)

    extractor = CsvFileExtractor([MockCsvFileSource(path) for path in file_paths])

    extracted_data = list(extractor.extract())

    assert isinstance(extracted_data, list)
    assert len(extracted_data) == expected_num_dataframes
    for df in extracted_data:
        assert isinstance(df, pd.DataFrame)
        assert df.shape == (len(sample_data_fixture['col1']), len(sample_data_fixture))
