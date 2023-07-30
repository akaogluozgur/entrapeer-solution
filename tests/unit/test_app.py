import pytest

from src import App
from src.models.csv_file_source import CsvFileSource


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
    sources = App.create_csv_file_sources(file_paths)
    assert len(sources) == len(expected_sources)
    for i, expected_source in enumerate(expected_sources):
        assert isinstance(sources[i], CsvFileSource)
        assert sources[i].file_path == expected_source.file_path





