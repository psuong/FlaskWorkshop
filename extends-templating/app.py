from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    # TODO: Render the content.html file here to showcase "extends" functionality.
    pass
if __name__ == '__main__':
    app.run(port=5000, debug=True)
