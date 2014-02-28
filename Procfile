web: gunicorn run:app
create_db: python create_db.py
upgrade_db: python db_upgrade.py
init: python db_create.py && python fetch_tweets.py
