from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tmdbmgbz:TaQhYFew5JO6OxG_X3Vwq-UyP5FzqmTL@kesavan.db.elephantsql.com/tmdbmgbz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.context_processor
def handle_context():
    return dict(os=os)

class Games(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    title = db.Column(
        db.String(52),
        nullable=True
    )
    max_players = db.Column(
        db.Integer,
        nullable=True
    )
    genre = db.Column(
        db.String(52),
        nullable=True
    )
    publisher = db.Column(
        db.String(20),
        nullable=True
    )
    price = db.Column(
        db.Float,
        nullable=True
    )
    release_year = db.Column(
        db.Integer,
        nullable=True
    )

    def __init__(self, title, max_players, genre, publisher, price, release_year):
        self.title = title
        self.max_players = max_players
        self.genre = genre
        self.publisher = publisher
        self.price = price
        self.release_year = release_year


@app.route('/')
def home():
    return render_template('landing_page.html')


@app.route('/dash')
def go_dash():
    games = Games.query.all()
    return render_template('dashboard.html', games=games)


@app.route('/list')
def go_list():
    games = Games.query.all()
    return render_template('gameslist.html', games=games)


@app.route('/admin')
def go_adm():
    games = Games.query.all()
    return render_template('admin.html', games=games)

@app.route('/add')
def go_add():
    return render_template()


@app.route('/add_game', methods=['GET', 'POST'])
def adm_add():
    if request.method == 'POST':
        game = Games(
            request.form['title'],
            request.form['max_players'],
            request.form['genre'],
            request.form['publisher'],
            request.form['price'],
            request.form['release_year'])
        db.session.add(game)
        db.session.commit()
    return redirect('/admin')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def adm_edit(id):
    gameEdit = Games.query.get(id)
    if request.method == 'POST':
        gameEdit.title = request.form['title']
        gameEdit.genre = request.form['genre']
        gameEdit.max_players = request.form['max_players']
        gameEdit.price = request.form['price']
        gameEdit.publisher = request.form['publisher']
        gameEdit.release_year = request.form['release_year']
        db.session.commit()
        return redirect('/admin')

    return render_template('admin.html', gameEdit=gameEdit)


@app.route('/del/<id>', methods=['GET', 'POST'])
def adm_del(id):
    gameEdit = Games.query.get(id)
    db.session.delete(gameEdit)
    db.session.commit()
    return redirect('/admin')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
