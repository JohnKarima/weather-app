from flask import render_template,request,redirect,url_for, flash
from . import main
from flask_login import login_required, current_user
from ..request import get_weather_data
from ..models import User, City
from .. import db
import requests




@main.route('/')
def index():
    cities = City.query.all()
    weather_data = []
    for city in cities:
        r = get_weather_data(city.name)
        print(r)
        weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'wind': r['wind']['speed'],
            'humidity': r['main']['humidity']
        }
        
        weather_data.append(weather)

    title = 'Home: WeatherApp'
    return render_template('index.html', title = title, weather_data = weather_data)

@main.route('/', methods=['POST'])
def index_post():
    err_msg = ''
    new_city = request.form.get('city')
        
    if new_city:
        existing_city = City.query.filter_by(name=new_city).first()
        if not existing_city:
            new_city_data = get_weather_data(new_city)
            if new_city_data['cod'] == 200:
                new_city_obj = City(name=new_city)
                db.session.add(new_city_obj)
                db.session.commit()

            else:
                err_msg = 'City does not exist. Check your spelling and try again!'
        else:
            err_msg = 'City already present in the database.'

    if err_msg:
        flash(err_msg, 'error')
    else:
        flash('City added succesfully!')

    return redirect(url_for('main.index'))

@main.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()

    flash(f'Successfully deleted { city.name }', 'success')
    return redirect(url_for('main.index'))