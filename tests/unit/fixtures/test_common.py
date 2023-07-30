import pytest
import pandas as pd

from src.models.csv_file_source import CsvFileSource

@pytest.fixture
def csv_file_source_fixture(tmpdir):
    # Create a temporary CSV file for testing
    data = {'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}
    csv_file = tmpdir.join('test.csv')
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    return CsvFileSource(file_path=str(csv_file))