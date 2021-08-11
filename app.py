from flask import Flask, render_template, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tmdbmgbz:TaQhYFew5JO6OxG_X3Vwq-UyP5FzqmTL@kesavan.db.elephantsql.com/tmdbmgbz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('landing_page.html')


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(52), nullable=True)
    max_players = db.Column(db.Integer, nullable=True)
    genre = db.Column(db.String(52), nullable=True)
    publisher = db.Column(db.String(20), nullable=True)
    price = db.Column(db.Float, nullable=True)
    release_year = db.Column(db.Integer, nullable=True)
    # brand_new = db.Column(db.Boolean, nullable=False)


    def __init__(self, title, max_players, genre, publisher, price, release_year):
        self.title = title
        self.max_players = max_players
        self.genre = genre
        self.publisher = publisher
        self.price = price
        self.release_year = release_year

@app.route('/dashboard')
def dash():
    games = Games.query.all()
    return render_template('dashboard.html',games=games)
    
@app.route('/gameslist')
def gamelist():
    games = Games.query.all()
    return render_template('gameslist.html', games=games)


@app.route('/admin')
def adm():
    games = Games.query.all()
    return render_template('admin.html', games=games)

@app.route('/admin/<id>', methods=['GET','POST'])
def edit(id):
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

@app.route('/add', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        game = Games(
            request.form['title'],
            request.form['max_players'],
            request.form['genre'],
            request.form['publisher'],
            request.form['price'],
            request.form['release_year'],
        )
        db.session.add(game)
        db.session.commit()
        return redirect('/admin')


@app.route('/edit', methods=['GET', 'POST'])
def edit_game():
    id = request.form['id']
    if request.method == 'POST':
        gameEdit = Games.query.get(id)
        gameEdit.title = request.form['title']
        gameEdit.max_players = request.form['max_players']
        gameEdit.genre = request.form['genre']
        gameEdit.publisher = request.form['publisher']
        gameEdit.price = request.form['price']
        gameEdit.release_year = request.form['release_year']

        db.session.commit()
        return redirect('/admin')


@app.route('/delete', methods=['GET', 'POST'])
def delete_game():
    id = request.form['id']
    gameEdit = Games.query.get(id)
    db.session.delete(gameEdit)
    db.session.commit()
    return redirect('/admin')


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)

    # sims = Jogo("The Sims", "sims.png", "Jogo de pessoa", "www.sims.com")
    # db.session.add(sims)
    # db.session.commit()
