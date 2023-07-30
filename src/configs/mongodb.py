import os


class MongoDBConfigs:
    DEFAULT_CHUNK_SIZE: int = 100000 # records
    HOST: str = os.environ.get('MONGO_HOST', 'mongo')
    PORT = os.environ.get('MONGO_PORT', 27017)
    USERNAME = os.environ.get('USERNAME', 'root')
    PASSWORD = os.environ.get('PASSWORD', 'example')
    MONGO_DATABASE = os.environ.get('MONGO_DATABASE', 'startup')
    INVESTMENT_COLLECTION = os.environ.get('MONGO_INVESTMENT_COLLECTION', 'investment')