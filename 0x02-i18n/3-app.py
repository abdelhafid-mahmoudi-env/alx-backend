#!/usr/bin/env python3
"""
Initialization of a Flask application with Babel for text localization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Optional

app = Flask(__name__)

class Config:
    """
    Babel configuration with languages and default settings.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Selects the appropriate locale from the HTTP request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Displays the home page with localization.
    """
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run()
