from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images


class UploadForm(FlaskForm):
    upload = FileField('Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    submit = SubmitField('Upload')
