"""
My Flask website.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/cfa')
def cfa():
    return "Code for America"


@app.route('/my/name/is/<name>')
def my_name(name):
    return name.title()


if __name__ == '__main__':
    app.run(debug=True)
