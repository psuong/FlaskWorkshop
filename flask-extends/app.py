from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    # Extends allows you to override the content within some statement
    # variable in the HTML file, which allows you to create dynamically
    # different pages wihtout having to create a new static html file.
    content_dict = {"content": "With extends, you only need to render the"
                               " child template, not the parent template."
                               " The child template will inherit the "
                               "parent template's contents.",
                    "title": "Using Extends."}
   
    return render_template('content.html', **content_dict)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
