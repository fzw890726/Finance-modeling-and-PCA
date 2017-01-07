# coding: utf-8

"""
    forms.py
    ~~~~~~~~
    http://wtforms.readthedocs.io/en/latest/fields.html
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import FloatField,IntegerField

class UploadForm(FlaskForm):
    DataFile = FileField('Your data file', validators=[
        FileRequired(),
        FileAllowed(['csv', 'txt'], 'plain text file only!')
    ])

class EuropeanForm(FlaskForm):
    S0 = FloatField('S0')
    R = FloatField('R')
    Sigma = FloatField('Sigma')
    T = FloatField('T')
    I = IntegerField('I')