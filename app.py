from flask import Flask, render_template, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://azdzqgug:OfKkSBFGLAzhDvyH1BggTpnBOst1M_po@kesavan.db.elephantsql.com/azdzqgug'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('landing_page.html')


@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

# class Jogo(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column(db.String(150), nullable=False)
#     imagem = db.Column(db.String(500), nullable=False)
#     descricao = db.Column(db.String(500), nullable=False)
#     link = db.Column(db.String(300), nullable=False)

#     def __init__(self, nome, imagem, descricao, link):
#         self.nome = nome
#         self.imagem = imagem
#         self.descricao = descricao
#         self.link = link


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)

    # sims = Jogo("The Sims", "sims.png", "Jogo de pessoa", "www.sims.com")
    # db.session.add(sims)
    # db.session.commit()
