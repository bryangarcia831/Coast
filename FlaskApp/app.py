import datetime
import json
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, Blueprint
from flask_navigation import Navigation
from flask_restplus import Api, fields, Resource

app = Flask(__name__, static_folder='../static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
nav = Navigation(app)


@app.route('/', methods=['POST', 'GET'])
def home():
    """Home page for user's todos"""

    return render_template('main-page.html')


nav.Bar('top', [
    nav.Item('Home', 'home'),

])

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()
