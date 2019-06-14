from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main

from .. import db
from .. import connectdb


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')
