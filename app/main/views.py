from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home: WeatherApp'
    return render_template('index.html', title = title)