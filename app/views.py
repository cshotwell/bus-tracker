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

