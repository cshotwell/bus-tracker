from app import app
from flask import Flask
from flask import render_template

@app.route('/')
def hello_world(name=None):
    return render_template('sample.html', name=name)
