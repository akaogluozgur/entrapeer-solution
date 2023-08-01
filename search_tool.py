"""
Python CLI tool for search functionality
"""
import os
import argparse
import json
from typing import Dict, List
from pymongo import MongoClient


class Configs:  # pylint: disable=too-few-public-methods
    """
    A class to handle the configuration constants. 
    This includes settings related to the MongoDB connection and search functionality.
    """
    SEARCH_QUERY_COLUMN = 'source_description'
    HOST = os.environ.get('HOST', 'localhost')
    PORT = os.environ.get('PORT', 27017)
    USERNAME = os.environ.get('USER', 'root')
    PASSWORD = os.environ.get('PASSWORD', 'example')
    MONGO_DATABASE = 'startup'
    INVESTMENT_COLLECTION = 'investment'
    DOCUMENT_LIMIT = 10


class SearchTool:
    """
    This class handles the connection to the MongoDB and provides search functionality.
    """

    def __init__(self) -> None:
        """
        Constructor that initializes the MongoDB client with given host,
        port, username, and password.
        """
        self.client = MongoClient(
            host=Configs.HOST,
            port=Configs.PORT,
            username=Configs.USERNAME,
            password=Configs.PASSWORD,
        )
        self.database = self.client[Configs.MONGO_DATABASE]
        self.collection = self.database[Configs.INVESTMENT_COLLECTION]

    def sort_search_results(self, match_score_mapping: Dict) -> List[str]:
        """
        Sorts the search results based on the match score and returns the 
        top results as per the DOCUMENT_LIMIT.

        :param match_score_mapping: A dictionary containing document ids and their match scores.
        :return: A list of sorted document ids as per match score.
        """
        sorted_results = [
            document_id
            for document_id, _
            in sorted(match_score_mapping.items(), key=lambda item: item[1], reverse=True)
        ]
        return sorted_results[:Configs.DOCUMENT_LIMIT]

    def search(self, query: str) -> List[Dict]:
        """
        Performs a search on the MongoDB collection based on the query string.

        :param query: The search query string.
        :return: A list of search results sorted by match score.
        """
        query_words = query.split()

        match_score_mapping = {}
        document_id_to_document_mapping = {}
        for word in query_words:
            word_results = self.search_word(word)

            for result in word_results:
                document_id = result.get("_id")
                match_score_mapping.setdefault(document_id, 0)
                match_score_mapping[document_id] += 1
                document_id_to_document_mapping[document_id] = result

        sorted_result_ids = self.sort_search_results(match_score_mapping)
        sorted_documents = [
            {
                **document_id_to_document_mapping[result_id],
                "match_score": match_score_mapping[result_id]
            }
            for result_id in sorted_result_ids
        ]
        return sorted_documents

    def search_word(self, word: str):
        """
        Performs a search on the MongoDB collection for a single word.

        :param word: The word to search for.
        :return: A list of search results that contain the word.
        """
        query = {"$text": {"$search": f"\"{word}\""}}
        sort_order = [("score", {"$meta": "textScore"})]
        cursor = self.collection.find(
            query
        ).sort(sort_order)
        results = list(cursor)
        return results


def main():
    """
    The main function that parses command-line arguments and performs search operations.
    """
    parser = argparse.ArgumentParser(
        description="Search tool for source_description column in MongoDB."
    )
    parser.add_argument(
        "query",
        type=str,
        help="Keyword to search in source_description column."
    )
    args = parser.parse_args()

    search_tool = SearchTool()

    results = search_tool.search(args.query)
    if not results:
        print("No results found.")
    else:
        json_results = json.dumps(results, indent=4, default=str)
        print(json_results)


if __name__ == "__main__":
    main()
