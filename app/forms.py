from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images


class UploadForm(FlaskForm):
    image = HiddenField(id='inp_img')
    submit = SubmitField('Upload')
