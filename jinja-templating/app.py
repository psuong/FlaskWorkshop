# In order for Flask to use templates, you need to import another module called
# "render_template" Essentially, "render_template" does exactly what it sounds
# like; it takes an HTML template file and loads it onto a webpage.
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    # Extends allows you to override the content within some statement
    # variable in the HTML file. This allows you to create dynamically
    # different pages wihtout having to create a new static html file.    
    
    # Assign each variable found within both base.html and content.html
    # such that Flask can return a legitimate page to be rendered.

    # Note: If you are missing a variable that needs to be assigned, Flask
    # will spout an error in your terminal and on the webpage as long as
    # debugging is enabled. 

    # Modify the strings if you'd like to try it for yourself. :)
    return render_template('content.html',
                           title="Showcasing Templating with Flask",
                           block_description="Think of {% include \"<html_file"
                                             ">}\" as a way to load \"objects\""
                                             " into a webpage.",
                           body_content="This content will be loaded into the "
                                        "base.html file whose variable name is"
                                        "\"body_content\"!",
                           show_link=True
                           )


@app.route('/clean-variables')
def cleaner_variable_loading():
    # Instead of assigning your variables in your return statement you can
    # place them in a dictionary and use Python's keyword arguments to assign
    # the variables.

    # So, a good question is why do this? Why not just stick with assigning
    # variables in the return statement?
    # Model View Controllers (MVC) are a software design pattern primarily
    # used in any kind of software dealing with user interfaces.
    
    # Models are databases.
    # Views deal with user interface.
    # Controllers deal with the logic on updating views and models.

    # This kind of design pattern will allow you to seperate your scripts
    # and thus allow for an easier time debugging, as you can isolate where
    # the error is taking place.

    # If you're a beginner you want to practice just setting up a dictionary
    # for Flask, but as you practice try splitting your scripts. Place the logic
    # into another file and simply import that logic into your views (files that
    # deal with any kind of routing, like this one). 
    
    content_dict = {"title": "Using a Dictionary Instead",
                    "body_content": "Simply create a dictionary with all of "
                    "your variable names as the keys and variable assignments "
                    "as the dictionary values. Pass the dictionary into "
                    "the return statement of the render_template as a keyword "
                    "argument, like this: **dictionary.",
                    "show_link": False,
                    "block_description": "Dictionaries are alternative ways."
                    }
    return render_template('content.html', **content_dict)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
