import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CONSUMER_KEY = 'pdbdJxVaKClslVV3YHKWQ'
CONSUMER_SECRET = 'Sa3ETL5ICForVs7UfkqcIERtLHljwWs3Boy6Y11K2aw'
