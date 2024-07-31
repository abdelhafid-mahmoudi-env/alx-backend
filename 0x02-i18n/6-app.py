#!/usr/bin/env python3
"""
Initialization of a Flask application with Babel
for text localization.
This script also handles user login simulation
and adjusts the localization
based on URL parameters, user preferences,
or request headers.
"""
from flask import Flask, request, g, redirect, url_for, render_template
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'


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


@babel.localeselector
def get_locale():
    """
    Selects the appropriate locale based on:
    1. URL parameters
    2. User settings
    3. Request headers
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Displays the home page.
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)
