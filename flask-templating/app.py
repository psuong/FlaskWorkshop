# In order for Flask to use templates, you need to import another module called "render_template"
# Essentially, "render_template" does exactly what it sounds like; it takes an HTML template file and
# loads it onto a webpage.
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    # The following return statement below renders the base.html file and locates each variable within
    # the html files. Assign each variable a value and run the app. Your browser will display the contents
    # you've written for each variable.

    # TODO: Add the line number the reader should reference.
    # Note: If you are missing a variable that needs to be assigned Flask will spout an error in your terminal
    # and on the webpage as long as debugging is enabled! (See line )

    # Play around with the values if you feel like you need to try it for yourself. :)
    return render_template('base.html', title="Showcasing Templating!", 
                                        body_content="This content will be loaded into the "
                                        "base.html file whose variable name is \"body_content\"!")


@app.route('/clean-variables')
def cleaner_variable_loading():
    # TODO: Show kwargs using a dict rather than getting every variable in HTML files and assigning it in the 
    # return statement.
    pass


if __name__ == '__main__':
    app.run(debug=True)
