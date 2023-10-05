from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from password_strength import PasswordPolicy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cisco@123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:new password@localhost/security'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

password_policy = PasswordPolicy.from_names(
    length=8,
    uppercase=1,
    numbers=1,
    special=1,
    nonletters=1,
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your username and password.', 'error')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
