from datetime import datetime
from flask import render_template, redirect, url_for, request
from . import main

from .. import db
from ..models import Ranking, MovieProfile


@main.route('/', methods=['GET'])
@main.route('/<int:page>', methods=['GET'])
def index(page=1):
    per_page = 8
    ranks = Ranking.query.order_by().paginate(page, per_page, error_out=False)

    return render_template('index.html', ranks=ranks)


@main.route('/details/<int:mid>', methods=['GET'])
def details(mid):
    profile = MovieProfile.query.filter_by(id=mid).first()
    rank = Ranking.query.filter_by(id=mid).first()

    return render_template('details.html', profile=profile, rank=rank)
