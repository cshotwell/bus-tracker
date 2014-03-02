from app import db
from app import models
from sys import argv

def add_user(username, bus):
    username = username.lower()
    user = models.User.query.filter_by(username=username).first()
    if not user: #if there is no user, save this one
        user = models.User(username=username, bus=bus, role=models.ROLE_USER)
        db.session.add(user)
        db.session.commit()


if __name__ == '__main__':
    username = argv[1]
    bus = argv[2]
    add_user(username, bus)

