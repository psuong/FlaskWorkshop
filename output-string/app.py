# If you're not used to Python syntax, what the line below is stating is
# from the flask file import a specific module called Flask.
# For those used a C like language, think of it as the "using" keyword.
from flask import Flask

# The line below creates an object called app.
# The __name__ is used for single web apps! This lets Flask know which
# directories to look at.
app = Flask(__name__)

# Line 15 contains a decorator due to the @ symbol. So what are decorators?
# Decorators are simply ways of extending a function's functionality without
# directly having to change the function.
# @app.route('/') has an innate functionality to provide the URL of a specific
# page, while the function def index() provides the functionality to return a
# string to be rendered at that specific URL.


@app.route('/')
def index():
    return "Congratulations! You just launched a flask app!"

# The following if statement below lets Python know that this specific file is
# the main file to execute.
if __name__ == '__main__':
    # Let the app run on a port at address 5000 and allow some debugging.
    app.run(port=5000, debug=True)
