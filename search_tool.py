import argparse
import json
from pymongo import MongoClient

class Configs:
    SEARCH_QUERY_COLUMN = 'source_description'
    HOST = 'localhost'
    PORT = 27017
    USERNAME = 'root'
    PASSWORD = 'example'
    MONGO_DATABASE = 'startup'
    INVESTMENT_COLLECTION = 'investment'
    
class SearchTool:
    def __init__(self) -> None:
        self.client = MongoClient(
            host='localhost',
            port=Configs.PORT,
            username=Configs.USERNAME,
            password=Configs.PASSWORD,
        )
    
    def connect_database(self):
        self.database = self.client[Configs.MONGO_DATABASE]
        self.collection = self.database[Configs.INVESTMENT_COLLECTION]
    

    def keyword_search(self, query: str):
        query = {"$text": {"$search": query}}
        sort_order = [("score", {"$meta": "textScore"})]
        cursor = self.collection.find(query).sort(sort_order).limit(10)
        results = list(cursor)
        return results


def main():
    parser = argparse.ArgumentParser(
        description="Search tool for source_description column in MongoDB."
    )
    parser.add_argument("query", type=str, help="Keyword to search in source_description column.")
    args = parser.parse_args()

    search_tool = SearchTool()
    search_tool.connect_database()
    
    results = search_tool.keyword_search(args.query)
    
    if not results:
        print("No results found.")
    else:
        json_results = json.dumps(results, indent=4, default=str)
        print(json_results)

if __name__ == "__main__":
    main()