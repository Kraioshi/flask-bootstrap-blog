from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
Bootstrap5(app)


@app.route('/')
def get_all_posts():
    return render_template('index.html')


@app.route('/register')
def register_get():
    pass


@app.route('/login')
def login_get():
    pass


@app.route('/logout')
def logout():
    pass


@app.route('/about')
def about():
    pass


@app.route('/contact')
def contact():
    pass


if __name__ == "__main__":
    app.run(debug=True)
