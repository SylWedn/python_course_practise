import os

from flask_admin import Admin
from sqlalchemy.testing.pickleable import User
from flask_migrate import Migrate
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from db import db
from models import User, IncomeEntry, ExpenseEntry, MyModelView
from flask_bcrypt import Bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'account_database.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'_eml5#y2L"F3Q8z\n\xec]/'
Migrate(app, db)
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)
bcrypt = Bcrypt(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


admin = Admin(app)
admin.add_view(MyModelView(User, db.session))

with app.app_context():
    db.create_all()
    from forms import ContactForm, SignUpForm, LoginForm, IncomeEntryForm, ExpenseEntryForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(username=form.username.data).first()
        login_user(user)
        return redirect(url_for('home'))
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
            password=bcrypt.generate_password_hash(form.password1.data).decode('utf-8'),
            email=form.email.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('sign_up.html', form=form)


@app.route('/home')
def home():
    income_amount = IncomeEntry.query.filter_by(user_id=current_user.id).all()
    expense_amount = ExpenseEntry.query.filter_by(user_id=current_user.id).all()
    total_income = sum(entry.amount for entry in income_amount)
    total_expenses = sum(entry.amount for entry in expense_amount)
    balance = total_income - total_expenses
    income_entries = [ie for ie in IncomeEntry.query.filter_by(user_id=current_user.id).all()]
    expense_entries = [ee for ee in ExpenseEntry.query.filter_by(user_id=current_user.id).all()]
    return render_template('home.html', balance=balance, income_entries=income_entries, expense_entries=expense_entries)


@app.route('/income', methods=["GET", 'POST'])
def income():
    income_entry_form = IncomeEntryForm()
    if income_entry_form.validate_on_submit():
        income_entry = IncomeEntry(
            user_id=current_user.id,
            amount=income_entry_form.amount.data,
            sender=income_entry_form.sender.data,
            additional_info=income_entry_form.additional_info.data
        )

        db.session.add(income_entry)
        db.session.commit()
        return render_template('income.html', income_entry_form=income_entry_form)
    return render_template('income.html', income_entry_form=income_entry_form)


@app.route('/expense', methods=["GET", "POST"])
def expense():
    expense_entry_form = ExpenseEntryForm()
    if expense_entry_form.validate_on_submit():
        expense_entry = ExpenseEntry(
            user_id=current_user.id,
            amount=expense_entry_form.amount.data,
            payment_option_id=expense_entry_form.payment_option.data.id,
            good_or_service=expense_entry_form.good_or_service.data
        )
        db.session.add(expense_entry)
        db.session.commit()
        return render_template('expense.html', expense_entry_form=expense_entry_form)
    return render_template('expense.html', expense_entry_form=expense_entry_form)


@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template("contact_success.html", form=form)
    return render_template("contact_us.html", form=form)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
