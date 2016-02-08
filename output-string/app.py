from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "You just launched a flask app!"


if __name__ == '__main__':
    app.run(debug=True)
