from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(100), unique=True, nulable=False)
    email = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('user_list')
def user_list():
    data = db.session.quuery(User).all()
    return render_template('user_list.html', user_list =data)