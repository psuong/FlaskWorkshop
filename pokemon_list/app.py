from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# go to python interpreter, import db and create it
# import Pokemon class, add create some instances, add them and commit
class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    element = db.Column(db.String(20), unique=True)

    def __init__(self, name, element):
        self.name = name 
        self.element = element 

    def __repr__(self):
        return '<Pokemon %r>' % self.name



@app.route('/')
def hello_world():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run()
