from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app.functions import filefinder, directory
import os

class MoveForm(FlaskForm):
#    target_path = '/home/jsheldon/Documents/Code/flask_viewer/Flask'
#    file_choice = filefinder(target_path)
#    language = SelectField('Run', choices = file_choice)
    target_path = os.path.join(os.getcwd())    
    target = filefinder(target_path)
    target = list(zip(target, target))#,3,4,5,6)#tuple(filefinder(target_path))        
    target_location = SelectField('Please select file', choices=target)    
#    submit1 = SubmitField('Submit')
    destination_path = os.path.join(os.getcwd())
    destination = directory(destination_path)
    destination = list(zip(destination, destination))# (1,2,3,4,5,6)#tuple(directory(destination_path))
    destination_location = SelectField('Please select file', choices=destination)
    submit = SubmitField('Submit')