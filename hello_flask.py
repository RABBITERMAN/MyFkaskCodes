#!/usr/bin/env python

from flask import send_from_directory #, add_url_rule
from flask import Flask
import flask
# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    APP.debug=True
    APP.run()