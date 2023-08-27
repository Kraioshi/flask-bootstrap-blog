from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
Bootstrap5(app)


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
