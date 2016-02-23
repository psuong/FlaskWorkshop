from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# go to python interpreter, import db and create it
# import Pokemon class, add create some instances, add them and commit
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    element = db.Column(db.String(20), unique=False)

    def __init__(self, name, element):
        self.name = name 
        self.element = element 

    def __repr__(self):
        return '<Pokemon %r>' % self.name


@app.route('/')
def hello_world():
    return "hello, your first flask app" 

# hits GET request by default
@app.route('/pokemons')
def pokemons():
    # query db
    pokemons = Pokemon.query.all()

    return render_template("index.html", pokemons=pokemons)


@app.route('/add_pokemon', methods=['POST'])
def new_pokemon():

    name = request.form['name']
    element = request.form['element']

    new_pokemon = Pokemon(name, element)
    db.session.add(new_pokemon)
    db.session.commit()

    return redirect('/pokemons')


@app.route('/delete_pokemons', methods=['POST'])
def delete_pokemons():

    Pokemon.query.delete()
    db.session.commit()
    return redirect('/pokemons')

if __name__ == '__main__':
    # always have debug true while developing
    app.run(debug=True)


