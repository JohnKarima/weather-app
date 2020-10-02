from flask_wtf import FlaskForm
from flask import render_template,request,redirect,url_for,abort
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from flask_login import login_required
from ..models import User
from . import main

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
