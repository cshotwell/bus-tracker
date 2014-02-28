from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tweet = Table('tweet', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('tweet_id', String(length=50)),
    Column('body', String(length=300)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
    Column('lat', String(length=50)),
    Column('lon', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tweet'].columns['tweet_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tweet'].columns['tweet_id'].drop()
