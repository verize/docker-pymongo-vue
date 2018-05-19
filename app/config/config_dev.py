import os
from src.resources import users
from dotenv import load_dotenv

load_dotenv(verbose=True)

config_dev = {
    # Eve configuration
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
    'TESTING': True,
    # Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
    # individual items  (defaults to read-only item access).
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    # Enable reads (GET), inserts (POST) and DELETE for resources/collections
    # (if you omit this line, the API will default to ['GET'] and provide
    # read-only access to the endpoint).
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
    'DOMAIN': {
        'users': users.users_resource
    },
    # Debug Toolbar Config
    'DEBUG_TB_PROFILER_ENABLED': True,
    'DEBUG_TB_PANELS': [
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        'flask_mongoengine.panels.MongoDebugPanel',
    ]
}
