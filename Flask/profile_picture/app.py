from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SECRET_KEY'] = '!)=UDHSU)Z&=)FSUJFSIKUF)O9sf089gs7d89ß2405'
# initialize the app with the extension
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(30), nullable=False, default='default.jpg')
    email = db.Column(db.String(200), unique=True, nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


class UserCreateForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    email = StringField("E-Mail", [Email(message="Wrong E-Mail address"), DataRequired()])
    submit = SubmitField("Submit")

    def validate_username(self, username):
        user = db.session.query(User).filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'User {username.data} already exists.')

    def validate_email(self, email):
        user = db.session.query(User).filter_by(email=email.data).first()
        if user:
            raise ValidationError(f'Email {email.data} already exists.')


class UserUpdateForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    email = StringField("E-Mail", [Email(message="Wrong E-Mail address"), DataRequired()])
    picture = FileField('Profile Picture', [FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

    def validate_username(self, username):
        user = db.session.query(User).filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'User {username.data} already exists.')

    def validate_email(self, email):
        user = db.session.query(User).filter_by(email=email.data).first()
        if user:
            raise ValidationError(f'Email {email.data} already exists.')


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
        if not user.password == password.data:
            raise ValidationError('Password incorrect.')


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


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(username=form.username.data).first()
        if user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password1.data,
            email=form.email.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('sign_up.html', form=form)


# CRUD (Create Retrieve Update Delete)

# Retrieve
@app.route('/user_list')
def user_list():
    data = db.session.query(User).all()
    return render_template('user_list.html', user_list=data)


# Create
@app.route('/user_create', methods=['GET', 'POST'])
def user_create():
    form = UserCreateForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data,
            email=form.email.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_list'))

    return render_template('user_create.html', form=form)


# Update
@app.route('/user_update/<user_id>', methods=['GET', 'POST'])
def user_update(user_id):
    user = db.get_or_404(User, user_id)
    form = UserUpdateForm()
    form.username.data = user.username
    form.email.data = user.email
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        db.session.commit()
        return redirect(url_for('user_list'))

    return render_template('user_update.html', form=form, user_id=user_id)


@app.route("/user_delete/<user_id>", methods=["GET", "POST"])
def user_delete(user_id):
    user = db.get_or_404(User, user_id)

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("user_list"))

    return render_template("user_delete.html", user=user)


app.run(debug=True)
