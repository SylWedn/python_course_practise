from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, FloatField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField

from models import User, PaymentOption
from db import db


class ContactForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    email = StringField(
        "Email", [Email(message="Wrong address."), DataRequired()])
    body = TextAreaField(
        "Your message",
        [DataRequired(), Length(min=10, message="Text too short.")])
    submit = SubmitField("Submit")


class IncomeEntryForm(FlaskForm):
    amount = FloatField('Amount', [DataRequired()])
    sender = StringField('Sender', [DataRequired()])
    additional_info = StringField('Additional info')
    submit = SubmitField("Create Income Entry")


class ExpenseEntryForm(FlaskForm):
    amount = FloatField('Amount', [DataRequired()])
    payment_option = QuerySelectField('Payment option', query_factory=db.session.query(PaymentOption).all,
                                      get_label='payment_option')
    good_or_service = StringField('Received good or service', [DataRequired()])
    submit = SubmitField("Create Expense Entry")


class LoginForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Login")

    def validate_username(self, username):
        user = db.session.query(User).filter_by(username=username.data).first()
        if not user:
            raise ValidationError(f'User {username.data} does not exist.')

    def validate_password(self, password):
        user = db.session.query(User).filter_by(username=self.username.data).first()
        if not user:
            return
        if not bcrypt.check_password_hash(user.password, password.data):
            raise ValidationError('Incorrect password.')


class SignUpForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password1 = PasswordField("Password1", [DataRequired()])
    password2 = PasswordField("Password2", [DataRequired(), EqualTo('password1', 'Passwords do not match.')])
    email = StringField("E-Mail", [Email(message="Wrong E-Mail address"), DataRequired()])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = db.session.query(User).filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'User {username.data} already exists.')

    def validate_email(self, email):
        user = db.session.query(User).filter_by(email=email.data).first()
        if user:
            raise ValidationError(f'Email {email.data} already exists.')

from app import bcrypt
