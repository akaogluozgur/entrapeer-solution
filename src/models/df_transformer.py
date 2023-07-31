"""
data_frame_row_dict_transformer.py - Module for defining the DataFrameRowDictTransformer class.

This module contains the implementation of the DataFrameRowDictTransformer class, which is a
specific implementation of the Transformer abstract class. It provides functionality to transform
a DataFrame into a list of dictionaries, where each dictionary represents a row in the DataFrame.

Classes:
    DataFrameRowDictTransformer: Class for transforming a DataFrame into a list of dictionaries.
"""
from typing import Dict, List
import pandas as pd

from src.interfaces.transformer import Transformer


class DataFrameRowDictTransformer(Transformer):
    """
    Class for transforming a DataFrame into a list of dictionaries.

    This class is a specific implementation of the Transformer abstract class, providing
    functionality to transform a DataFrame into a list of dictionaries. Each dictionary in
    the list represents a row in the DataFrame.

    Attributes:
        input_data (pd.DataFrame): The input DataFrame to be transformed.

    Methods:
        transform() -> List[Dict]:
            Transform the input DataFrame into a list of dictionaries.
    """

    def __init__(self, input_df: pd.DataFrame) -> None:
        """
        Constructor for the DataFrameRowDictTransformer class.

        Args:
            input_df (pd.DataFrame): The input DataFrame to be transformed.
        """
        super().__init__(input_data=input_df)

    def transform(self) -> List[Dict]:
        """
        Transform the input DataFrame into a list of dictionaries.

        Returns:
            List[Dict]: A list of dictionaries, where each dictionary represents a row in
            the input DataFrame.
        """
        output_dicts = self.input_data.to_dict(orient='records')
        return output_dicts

    def __str__(self) -> str:  # pragma: no cover
        """
        String representation of the DataFrameRowDictTransformer object.

        Returns:
            str: The string representation of the DataFrameRowDictTransformer object.
        """
        return str(self.input_data)
