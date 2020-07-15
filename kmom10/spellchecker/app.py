#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application, including useful error handlers.
"""
import os
import re
from flask import Flask, render_template, request, session
#pylint: disable=no-name-in-module
from spellchecker import SpellChecker

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

sc = SpellChecker()

@app.route("/")
def main():
    """ Home route """
    return render_template("index.html")


@app.route("/find", methods=["POST", "GET"])
def find_word():
    """ Find a word"""
    if request.method == "POST":
        if session.get("word_list"):
            sc.word_list = session.get("word_list")

        sc.add_words()
        word = request.form["find"]
        search = sc.find_word(word)

        if not word:
            r = False
        elif search:
            r = "'" + word + "' is in the list and spelled correctly!"
        else:
            r = "'" + word + "' is not in the list!"

    return render_template("index.html", result=r)


@app.route("/words")
def words():
    """ View all words """
    if session.get("word_list"):
        sc.word_list = session.get("word_list")

    sc.add_words()
    sc.make_web_list()
    return render_template("words.html", spellchecker=sc)


@app.route("/dictionary")
def dictionary():
    """ Change the dictionary """
    if session.get("word_list"):
        current_list = session.get("word_list")
    else:
        current_list = sc.get_word_list()
    return render_template("dictionary.html", spellchecker_list=current_list)


@app.route("/change_dictionary", methods=["POST", "GET"])
def change_dictionary():
    """ Change the dictionary """
    if request.method == "POST":
        new_word_list = request.form["dictionary"]
        session["word_list"] = new_word_list
        current_list = session.get("word_list")
        sc.new_trie()

    return render_template("dictionary.html", spellchecker_list=current_list)


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
    app.run(debug=True, use_reloader=False)
