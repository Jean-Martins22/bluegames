from flask import Flask, render_template, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tmdbmgbz:TaQhYFew5JO6OxG_X3Vwq-UyP5FzqmTL@kesavan.db.elephantsql.com/tmdbmgbz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('landing_page.html')


@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(52), nullable=True)
    max_players = db.Column(db.Integer, nullable=True)
    genre = db.Column(db.String(52), nullable=True)
    publisher = db.Column(db.String(20), nullable=True)
    price = db.Column(db.Float, nullable=True)
    release_year = db.Column(db.Integer, nullable=True)

    def __init__(self, title, max_players, genre, publisher, price, release_year):
        self.title = title
        self.max_players = max_players
        self.genre = genre
        self.publisher = publisher
        self.price = price
        self.release_year = release_year


@app.route('/gameslist')
@app.route('/admin')
def gamelist():
    games = Games.query.all()
    return render_template('admin.html', games=games)


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)

    # sims = Jogo("The Sims", "sims.png", "Jogo de pessoa", "www.sims.com")
    # db.session.add(sims)
    # db.session.commit()
