#!/usr/bin/env python3
"""
Initialization of a Flask application with Babel for text localization.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    Retrieves the user from the 'login_as' URL parameter.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """
    Executes before each request to set the global user.
    """
    g.user = get_user()

@app.route('/')
def index():
    """
    Displays the home page.
    """
    return render_template('5-index.html')

@babel.localeselector
def get_locale():
    """
    Selects the appropriate locale based on the HTTP request.
    """
    return request.accept_languages.best_match(['en', 'fr'])

if __name__ == "__main__":
    app.run(debug=True)
