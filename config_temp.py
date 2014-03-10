import os
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = "postgresql://cshotwell:@localhost/startup_bus"
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True

PROPAGATE_EXCEPTIONS = True

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

SENDGRID_KEY = ''
SENDGRID_PASS = ''
