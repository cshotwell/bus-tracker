from app import app, models
from flask import Flask
from flask import render_template
from flask import redirect
from app import db

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
    error = None
    if request.method == 'POST':
        print request.form.keys
        username = request.form['user_name']
        bus = request.form['bus_name']
        save_sign_up(username, bus)
    return redirect('/')
        
import datetime
from flask import request
from app import db

def save_sign_up(username, bus):
    sign_up = models.SignUp(user_name=username, bus_name=bus, added=datetime.datetime.utcnow())
    db.session.add(sign_up)
    db.session.commit()

