
from db import db
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user
from sqlalchemy import ForeignKey


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    income_entries = db.relationship('IncomeEntry', back_populates='user')
    expense_entries = db.relationship('ExpenseEntry', back_populates='user')


class PaymentOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_option = db.Column('Payment option', db.String)
    entries = db.relationship("ExpenseEntry", back_populates="payment_option")

    def __str__(self):
        return f'{self.payment_option}'


class IncomeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    user = db.relationship('User', back_populates='income_entries')
    sender = db.Column(db.String(100))
    additional_info = db.Column(db.String(200))

    def __init__(self, user_id, amount, sender, additional_info):
        self.user_id = user_id
        self.amount = amount
        self.sender = sender
        self.additional_info = additional_info

    def __str__(self):
        return f'{self.amount}, {self.sender}, {self.additional_info}'

    def __repr__(self):
        return f'{self.amount}, {self.sender}, {self.additional_info}'


class ExpenseEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    user = db.relationship('User', back_populates='expense_entries')
    payment_option = db.relationship("PaymentOption", back_populates="entries")
    payment_option_id = db.Column(db.Integer, ForeignKey('payment_option.id'))
    good_or_service = db.Column(db.String(200))

    def __init__(self, user_id, amount, payment_option_id, good_or_service):
        self.user_id = user_id
        self.amount = amount
        self.payment_option_id = payment_option_id
        self.good_or_service = good_or_service

    def __str__(self):
        return f'{self.amount}, {self.payment_option}, {self.good_or_service}'

    def __repr__(self):
        return f'{self.amount}, {self.payment_option}, {self.good_or_service}'


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.username == "AivarasCer"