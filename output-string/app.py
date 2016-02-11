# Import the Flask module from the flask file.
from flask import Flask, redirect, request

# The line below creates an object called app.
# The __name__ is used for single web apps! This lets Flask know which
# directories to look at.
app = Flask(__name__)

# Line 17 contains a decorator due to the @ symbol. So what are decorators?
# Decorators are simply ways of extending a function's functionality without
# directly having to change the function.
# @app.route('/') has an innate functionality to provide the URL of a specific
# page, while the function def index() provides the functionality to return a
# string to be rendered at that specific URL.


@app.route('/')
def index():
    return "Congratulations! You just launched a flask app!"


#get request example
@app.route('/greet', methods=['GET'])
def greeting():

    page = ''' 
            <!DOCTYPE html>
            <html lang="en-US">
            <head>
            <title>Greet student</title>
            <meta charset="utf-8">
            </head>
            <body>
            
            <h1>Greeting human</h1>
            <p> Your name is {0} and your major is {1} </p>
            </body>
            </html>
            '''

    if request.method == 'GET':
        #expecting a name and major
        name = request.args.get('name')
        major = request.args.get('major')
        return page.format(name, major) 


# The following if statement below lets Python know that this specific file is
# the main file to execute.
if __name__ == '__main__':
    # Let the app run on a port at address 5000 and allow some debugging.
    app.run(port=5000, debug=True)
