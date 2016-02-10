## Templates

Templates are a way to dynamically change content of a webpage without having to modify the HTML directly or create new HTML files that have the content you need.

Content you need on specific webpages can instead be loaded through a function in your Flask app. Templating in Flask is done through Jinja2, you can view the API [here](http://jinja.pocoo.org).

This directory specifically deals with Jinja's {% extends ... %} functionality.

## Project Directory

root/
 - app.py
 - templates/
    - HTML files

## Quick overview on Variables

- {{ ... }} - Are expressions that will be printed onto the webpage.
- {% ... %} - Are statements, they don't get printed to the webpage.
- {# ... #} - They're comments, they don't get used in the template.

View more at the [Jinja Documentation](http://jinja.pocoo.org/docs/dev/templates/).