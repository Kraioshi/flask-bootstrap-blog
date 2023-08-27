from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    return render_template('index.html')


@app.route('/register', methods=["GET"])
def register_get():
    form = RegistrationForm()
    return render_template('register.html', form=form)


@app.route('/register', methods=["POST"])
def register_post():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('register_get'))


@app.route('/login')
def login_get():
    pass


@app.route('/logout')
def logout():
    pass


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
