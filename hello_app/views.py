"""
This module contains a Flask application that returns a greeting message.
"""
import re
from datetime import datetime
from flask import render_template
from . import app

@app.route('/')
def home():
    """
    Renders the home.html template.

    Returns:
        The rendered home.html template.
    """
    return render_template('home.html')

@app.route('/about/')
def about():
    """
    Renders the about.html template.

    Returns:
        The rendered about.html template.
    """
    return render_template('about.html')

@app.route('/contact/')
def contact():
    """
    Renders the contact.html template.

    Returns:
        The rendered contact.html template.
    """
    return render_template('contact.html')

@app.route('/hello/<name>')
def hello_there(name):
    """
    Returns a personalized greeting message with the current date and time.

    :param name: A string representing the name of the person to greet.
    :return: A string containing the personalized greeting message.
    """
    now = datetime.now()

    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "<h1>Hello there, " + clean_name + "!</h1>" + "<p> It's " + formatted_now + "</p>"
    return content

@app.route('/template/<name>')
def hello_template(name):
    """
    Returns a personalized greeting message with the current date and time using a template.

    :param name: A string representing the name of the person to greet.
    :return: A string containing the personalized greeting message.
    """

    return render_template(
        'hello_template.html',
        name=name,
        date=datetime.now()
    )

@app.route('/api/data')
def get_data():
    """
    Returns some example data as a JSON object.

    :return: A JSON object containing example data.
    """
    return app.send_static_file('data.json')
