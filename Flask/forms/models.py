from db import db


product_label = db.Table(
    "product_label",
    db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
    db.Column("label_id", db.Integer, db.ForeignKey("label.id")),
)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    code = db.Column(db.String(200), unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category")
    labels = db.relationship(
        "Label", secondary=product_label, back_populates="products"
    )


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=True)


class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    products = db.relationship(
        "Product", secondary=product_label, back_populates="labels"
    )
