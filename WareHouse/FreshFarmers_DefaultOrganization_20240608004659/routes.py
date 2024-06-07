'''
Defines the routes/endpoints for the FreshFarmers application.
'''
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, User, Farmer, Product, Order
from forms import LoginForm, RegisterForm, OrderForm
from utils import send_email, send_sms, calculate_distance
from werkzeug.security import check_password_hash
main_blueprint = Blueprint('main', __name__)
@main_blueprint.route('/')
def index():
    return render_template('index.html')
@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)
@main_blueprint.route('/home')
def home():
    # Logic to display farms within 50km
    return render_template('home.html')
@main_blueprint.route('/profile')
def profile():
    # Logic to display user profile
    return render_template('profile.html')
@main_blueprint.route('/cart')
def cart():
    # Logic to manage cart
    return render_template('cart.html')
@main_blueprint.route('/manage_orders')
def manage_orders():
    # Logic to manage orders lifecycle
    return render_template('manage_orders.html')