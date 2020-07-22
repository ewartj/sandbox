import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, literal

from app import app
from app.forms import MoveForm#, DestForm
from app.functions import directory, filefinder, filemover  # , path
from app.models import Schools

# out functions in new py script?

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    The home page. This will display a sql table (sequenced runs)
    """
    show = Schools.query.count()
    lists = Schools.query.all()
    return render_template("index.html", count=show, schools=lists)


@app.route('/dirtree', methods=['GET'])
def dirtree():
    """
    A page that shows a list of files in a folder. The folder is specified in the argument.
    """
    target_path = os.path.join(os.getcwd())
    destination_path = os.path.join(os.getcwd())
    target = filefinder(target_path)
    destination = directory(destination_path)
    return render_template('dirtree.html', target=target, destination=destination)


@app.route('/move_file', methods=['GET','POST'])
def move_file():
    form = MoveForm()
#    destForm = DestForm(request.form)
    if request.method == 'POST' and form.validate():
        #move the file
        fileToMove = request.form.get('target_location')
        destinationFolder = request.form.get('destination_location')
        print(fileToMove)
        print(destinationFolder)
        filemover(fileToMove, destinationFolder)
    return render_template('move_file.html', form = form)


@app.route('/runs/<slug>')
def detail(slug):
    """
    A page that will display more information about a sample
    """
    school = Schools.query.filter_by(Name=slug).first()
    return render_template("detail.html", school=school)

"""
@app.route('/')
@app.route('/index')
def index(): # show the database
    show = School.query.count()
    lists = School.query.all()
    return render_template("index.html", count=show, schools=lists)

path = os.path.abspath(os.path.dirname(__file__))

@app.route('/list')
def make_tree():
    path = os.path.abspath(os.path.dirname(__file__))
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                with open(fn) as f:
                    contents = f.read()
                tree['children'].append(dict(name=name, contents=contents))
    return render_template("list.html", tree = tree)
"""
