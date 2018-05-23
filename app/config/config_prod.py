import os
from src.resources import users


config_prod = {
    'MONGO_HOST': os.environ['MONGO_HOST'],
    'MONGO_PORT': int(os.environ['MONGO_PORT']),
    'MONGO_DBNAME': os.environ['MONGO_DBNAME'],
    'MONGO_USERNAME': os.environ['MONGO_USERNAME'],
    'MONGO_PASSWORD': os.environ['MONGO_PASSWORD'],
    # MongoEngine Configuration
    'MONGODB_SETTINGS': {
        'host': os.environ['MONGO_HOST'],
        'port': int(os.environ['MONGO_PORT']),
        'db': os.environ['MONGO_DBNAME'],
        'username': os.environ['MONGO_USERNAME'],
        'password': os.environ['MONGO_PASSWORD'],
        'connect': True
    },
    'URL_PREFIX': 'api',
    'API_VERSION': 'v1',
    # set a 'SECRET_KEY' to enable the Flask session cookies
    'SECRET_KEY': os.environ['SECRET_KEY'],
    'DEBUG': False,
    'TESTING': False,
    # Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
    # individual items  (defaults to read-only item access).
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    # Enable reads (GET), inserts (POST) and DELETE for resources/collections
    # (if you omit this line, the API will default to ['GET'] and provide
    # read-only access to the endpoint).
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'DOMAIN': {
        'users': users.users_resource
    }
}
