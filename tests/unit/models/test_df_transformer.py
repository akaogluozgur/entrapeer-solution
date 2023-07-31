import pandas as pd

from src.models.df_transformer import DataFrameRowDictTransformer


def test_transform(sample_data_fixture):
    sample_data_frame = pd.DataFrame([sample_data_fixture])
    transformer = DataFrameRowDictTransformer(sample_data_frame)

    result = transformer.transform()

    assert isinstance(result, list)
    assert len(result) == len(sample_data_frame)

    for item in result:
        assert isinstance(item, dict)

    for i, row in enumerate(sample_data_frame.iterrows()):
        _, expected_dict = row
        assert result[i] == expected_dict.to_dict()
