# -*- coding: utf-8 -*-
import os
from . import app
from flask import ( send_from_directory,
    render_template, 
    request)
from flask.views import View
from .forms import UploadForm , EuropeanForm
from werkzeug.utils import secure_filename
from flask import json
from .european import euporpen_option_simulation
'''
Example render template directly
'''
@app.route('/')
def index():
    # app.logger.debug('Debug test')
    return render_template('welcome.html')

'''
Hello world
'''
@app.route('/hello-template/<name>')
# @app.route('/hello/<name>')
def hello_world(name = None):
    return render_template('hello.html', name=name)
    #return 'Hello, World!'

@app.route('/hello')
# @app.route('/hello/<name>')
def raw_hello_world(name = None):
    # model storage
    model= '<!doctype html><html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/><title>Hello World</title></head>' \
           '      <div style="margin: 0 auto;width:85%;max-width:256px;"><h1>Hello World</h1><p >Hello Data Application Lab</p></div></html>'
    return model

@app.route('/hello-json')
# @app.route('/hello/<name>')
def json_hello_world(name = None):
    return json.jsonify(username="data application lab",
                   email="info@datalaus.com",
                   content="hello world!")
'''
Route Dispatch Example
'''
# yet another router
class MyView(View):
    methods = ['GET']

    def dispatch_request(self, name):
        return 'Hello %s!' % name

app.add_url_rule('/hello/<name>', view_func=MyView.as_view('myview'))

'''
POST Example for upload File
'''
# handler for upload data file
@app.route('/upload/',methods=('GET', 'POST'))
def upload():
    form = UploadForm()
    app.logger.debug('upload form')

    if form.is_submitted():
        filename = secure_filename(form.DataFile.data.filename)
        strDir = os.getcwd()
        filepath = os.path.join(strDir, 'uploads', filename)
        app.logger.debug(filepath)
        form.DataFile.data.save(filepath)
        return 'Upload Done!'
    else:
        filename = None
    return render_template('upload.html', form=form, filename=filename)

# endpoint page
@app.route('/result/')
def submit():
    return render_template('result.html')

@app.route('/about')
def about():
    return 'The about page'

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route('/output/<path:path>')
def send_upload(path):
    return send_from_directory('results', path)

# below method just for test
@app.route('/user/<name>')
def show_user_profile(name):
    return 'User %s name' % name

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


    # S0 = 100.
    # r = 0.05
    # sigma = 0.25
    # T = 1.0
    # I = 50000

@app.route('/european/', methods=('GET', 'POST'))
def european_option():
    form = EuropeanForm()

 #def euporpen_option_simulation(S0, r, sigma, T, I):
    result_pic, result_pic2 ='',''
    if form.is_submitted():
        result_model = euporpen_option_simulation(form.S0.data, form.R.data, form.Sigma.data, form.T.data, form.I.data)
        result_pic = '/output/%s' % result_model['pic1']
        result_pic2 = '/output/%s' % result_model['pic2']

    return render_template('option.html', form=form, pic1=result_pic, pic2=result_pic2)  # view_function
   # return render_template('py.html')


