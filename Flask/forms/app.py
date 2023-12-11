from db import db
from flask import Flask, render_template
from models import Label, Product
from forms import CreateProductForm

app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = b"J-'zM=UBon1r,aQ,ll$)h#Z(I$P7F*9kovu,q}8;"
# initialize the app with the extension
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def index():
    form = CreateProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            code=form.code.data,
            category_id=form.category.data.id,
        )
        for label_data in form.labels.data:
            label = db.session.get(Label, label_data.id)
            product.labels.append(label)
        db.session.add(product)
        db.session.commit()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)
