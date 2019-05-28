from flask import render_template
from . import main
from flask_login import login_required


@main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    pass


@main.route('/')
def whatever():
    return render_template('index.html')