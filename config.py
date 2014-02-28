import os
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = "postgresql://cshotwell:@localhost/startup_bus"
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True

PROPAGATE_EXCEPTIONS = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CONSUMER_KEY = 'pdbdJxVaKClslVV3YHKWQ'
CONSUMER_SECRET = 'Sa3ETL5ICForVs7UfkqcIERtLHljwWs3Boy6Y11K2aw'
