#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from datetime import date
from flask import Flask, render_template
import person

app = Flask(__name__)
about_me = person.Person("Paul", "Moreland", date(1980, 10, 4))
my_course = person.Course("OOPython-v2")

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html", me=about_me)

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html", course=my_course)

@app.route("/redovisning")
def redovisning():
    """ Redovisning route """
    return render_template("redovisning.html")

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=True)
