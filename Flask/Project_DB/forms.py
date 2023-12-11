from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from .forms import 
class UserCreateForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    email = StringField("E-Mail", [Email(message="Wrong E-Mail address"), DataRequired()])