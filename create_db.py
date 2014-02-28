from migrate.versioning import api
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path

engine = create_engine(SQLALCHEMY_DATABASE_URI)
conn = engine.connect()
conn.execute("commit")
conn.execute("create database startup_bus")
conn.close()

