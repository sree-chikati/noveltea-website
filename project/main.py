from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/search')
@login_required
def search():
    return render_template('search.html', name=current_user.name)

@main.route('/book')
@login_required
def book():
    return render_template('book.html', name=current_user.name)