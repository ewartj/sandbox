#from flask_autoindex import AutoIndex
import os

from flask import Flask, render_template, Response, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, literal

from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine) # sqlalchemy learns what the columns are

def directory(path):
    tree = []
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree.append(name)
    return tree

def filefinder(path):
    tree = []
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            if os.path.isfile(os.path.join(path, name)):
                tree.append(name)
    return tree

def filemover():
    #Moving forward code
    forward_message = "Moving Forward..."
    print(forward_message)

class Schools(db.Model):
    __tablename__ = 'test'
    __table_args__ = { 'extend_existing': True }
    Name = db.Column(db.Text, primary_key=True) 
#    test = test.query.all()

class SubmitForm(FlaskForm):
#    target_path = '/home/jsheldon/Documents/Code/flask_viewer/Flask'
    file_choice = ((1,1),(2,2,),(3,3))
    language = SelectField('Run', choices = file_choice)
    remember_me = BooleanField('Submit for analysis?')
    submit = SubmitField('Submit')

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    show = Schools.query.count()
    lists = Schools.query.all()
    form = SubmitForm()
    if form.validate_on_submit():
        if request.method == 'GET':
            form.process()
    return render_template("index.html", count=show, schools=lists, form=form)



@app.route('/dirtree', methods=['GET','POST'])
def dirtree():
    target_path = os.path.join(os.getcwd())
    destination_path = os.path.join(os.getcwd())
    target = filefinder(target_path)
    destination = directory(destination_path)
    forward = filemover()
    return render_template('dirtree.html', target=target, destination=destination, forward = forward)

@app.route('/runs/<slug>')
def detail(slug):
    school = Schools.query.filter_by(Name=slug).first()
    return render_template("detail.html", school=school)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

"""
@app.route('/forward/', methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    print(forward_message)
    return render_template('dirtree.html', forward_message=forward_message)
"""

#def button():
#    return  "Hello World"
#   return render_template("button.html", line=line)
#    return "Hello World"
#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    files = os.listdir()
#    currentDirectory = os.getcwd()
#    idx = AutoIndex(app, browse_root=currentDirectory)
#    return idx


"""
@app.route('/index')
def index():
    user = [i for i in test.query.order_by('type_of_appeal desc').all()]
    return render_template('index.html',
                           title='Home')
"""
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/viewer.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Viewer startup')

if __name__ == '__main__':
    app.run()
