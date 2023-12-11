from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from wtforms_sqlalchemy.fields import (
    QuerySelectField,
    QuerySelectMultipleField,
)
from models import Category, Label, Product
from db import db


class CreateProductForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    code = StringField("Code", validators=[DataRequired()])
    category = QuerySelectField(
        "Category",
        query_factory=db.session.query(Category).all,
        allow_blank=True,
        get_label="code",
    )
    labels = QuerySelectMultipleField(
        "Labels",
        query_factory=db.session.query(Label).all,
        allow_blank=True,
        get_label="name",
    )
    submit = SubmitField("Create")

    def validate_code(self, code):
        product = db.session.query(Product).filter_by(code=code.data).first()
        if product:
            raise ValidationError("Product already exists")
