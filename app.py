from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
def create_app():
    app = Flask(__name__)
    with app.app_context()
        init_db()
        return app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')
@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name ': 'amit', 'ankitmaurya.899@gmail.com': '893212299897', 'phone': 500},
        {'id': 2, 'name': 'ankit ', 'adress': '123985473165', 'phone': 900},
        {'id': 3, 'name': 'anuj', 'adress': '231985128446', 'phone': 150}
    ]
    return render_template('market.html', items=items)


