from app import app, models
from flask import Flask
from flask import render_template

@app.route('/')
def hello_world(name=None):
    return render_template('sample.html', name=name)

from flask import jsonify

@app.route('/users')
def show_users():
    users = [i.serialize for i in models.User.query.all()]
    return jsonify(user_list=users)

@app.route('/sign_up', methods=['POST'])
def sign_up():
    print "here!"
    error = None
    if request.method == 'POST':
        username = request.form['twitter_name']
        bus = request.form['bus']
        save_sign_up(username, bus)
    return request
        
import datetime

def save_sign_up(username, bus):
    sign_up = models.SignUp(user_name=username, bus_name=bus, added=datetime.datetime.utcnow())
    app.db.session.add(sign_up)
    app.db.session.commit()

