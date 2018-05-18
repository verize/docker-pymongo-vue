# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.

import os
from src.resources import users
from dotenv import load_dotenv

load_dotenv(verbose=True)

config_prod = {
    'MONGO_HOST': os.environ['MONGO_HOST'],
    'MONGO_PORT': os.environ['MONGO_PORT'],
    'MONGO_DBNAME': os.environ['MONGO_DBNAME'],
    'MONGO_USERNAME': os.environ['MONGO_USERNAME'],
    'MONGO_PASSWORD': os.environ['MONGO_PASSWORD'],
    'MONGODB_SETTINGS': {
        'db': os.environ['MONGO_DBNAME'],
        'username': os.environ['MONGO_USERNAME'],
        'password': os.environ['MONGO_PASSWORD'],
        'connect': True
    },
    'URL_PREFIX': 'api',
    'API_VERSION': 'v1',
    # set a 'SECRET_KEY' to enable the Flask session cookies
    'SECRET_KEY': os.environ['SECRET_KEY'],
    # Settings for MongoEngine
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
