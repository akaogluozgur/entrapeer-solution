import pytest
from unittest.mock import MagicMock, call
from src.models.mongodb_loader import MongoDBLoader, MongoDBStorage
from src.configs.mongodb import MongoDBConfigs


def test_load():
    mock_storage = MagicMock(spec=MongoDBStorage)

    input_data = [
        {"name": "Company 1", "industry": "Tech"},
        {"name": "Company 2", "industry": "Finance"},
        {"name": "Company 3", "industry": "Healthcare"},
    ]

    loader = MongoDBLoader(mongo_storage=mock_storage, chunk_size=2)

    loader.load(input_data)
    mock_storage.save.assert_has_calls(
        [
            call([
                {"name": "Company 1", "industry": "Tech"},
                {"name": "Company 2", "industry": "Finance"},
            ]),
            call([
                {"name": "Company 3", "industry": "Healthcare"},
            ]),
        ],
        any_order=False,
    )


def test_initialize_database(mongo_client_fixture):
    MongoDBStorage()
    mock_collection = mongo_client_fixture[MongoDBConfigs.MONGO_DATABASE][MongoDBConfigs.INVESTMENT_COLLECTION]
    mock_collection.index_information.return_value = {"_id_": {"key": [("_id", 1)], "v": 2}}
    mock_collection.create_index.assert_called_once_with(
        [(MongoDBConfigs.SEARCH_QUERY_COLUMN, "text")],
        name=f"{MongoDBConfigs.SEARCH_QUERY_COLUMN}_text",
    )


def test_save(mongo_client_fixture):
    storage = MongoDBStorage()

    input_data = [
        {"name": "Company A", "industry": "Tech", "founded": "2005"},
        {"name": "Company B", "industry": "Finance", "founded": "2010"},
    ]
    storage.save(input_data)
    mock_collection = mongo_client_fixture[MongoDBConfigs.MONGO_DATABASE][MongoDBConfigs.INVESTMENT_COLLECTION]
    mock_collection.insert_many.assert_called_once_with(input_data)
