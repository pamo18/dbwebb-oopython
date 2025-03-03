#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Minimal Flask application, including useful error handlers.
"""

import os
import re
from flask import Flask, render_template, request, redirect, url_for, session
#pylint: disable=no-name-in-module
from handler import QuestionManager

app = Flask(__name__)
app.secret_key = re.sub(r"[^a-z\d]", "", os.path.realpath(__file__))

qm = QuestionManager()

@app.route("/")
def main():
    """ Home route """
    return render_template("index.html")



@app.route("/question", methods=["POST", "GET"])
def question():
    """ question route """
    qm.read_session(session)

    if request.method == "POST":
        qm.correct_answer(request.form)

    qm.write_session(session)

    if qm.has_next():
        return render_template("question.html",
                               count=qm.get_quest_count(),
                               question=qm.get_next()
                              )

    return redirect(url_for('score_screen'))




@app.route("/score_screen", methods=["GET"])
def score_screen():
    """ Score screen """
    qm.read_session(session)
    return render_template("score_screen.html",
                           score=qm.get_score(),
                           max_score=qm.get_max_score()
                          )



@app.route("/reset")
def reset():
    """ Reset questions """
    qm.reset()
    qm.write_session(session)
    return redirect(url_for('main'))



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
