## Templates

Templates are a way to dynamically change content of a webpage without having to modify the HTML directly or create new HTML files that have the content you need.

Content you need on specific webpages can instead be loaded through a function in your Flask app. Templating in Flask is done through Jinja2, you can view the API [here](http://jinja.pocoo.org).

## Project Directory

root/
 - app.py
 - templates/
    - HTML files

## Quick overview on Variables

- {{ ... }} - Are expressions that will be printed onto the webpage (think variables).
- {% ... %} - Are statements, they don't get printed to the webpage, but rather control what content you need to show on the webpage. (Great for `if` statements and `for` loops.)
- {# ... #} - They're comments, they don't get used in the template.

View more at the [Jinja Documentation](http://jinja.pocoo.org/docs/dev/templates/).

## Includes vs Extends, When to use them?

The short answer is, you'll use them simultaneously. 

**Includes** allows you to add little snippets from one HTML file into another. These are incredibly useful when having to deal with parts of a webpage that are static and don't intend to change between pages (think of a navigation bar per say).

**Extends** allows you to override content between pages using the same template. These are useful for creating web pages which use the same layout and structure but simply have different content (e.g. blog).
