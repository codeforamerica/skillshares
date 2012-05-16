"""
My Flask website.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cfa')
def cfa():
    return "Code for America"


@app.route('/my/name/is/<name>')
def my_name(name):
    return name.title()


@app.route('/my/favorite/number/is/<int:number>')
def favorite_number(number):
    return str(number)


if __name__ == '__main__':
    app.run(debug=True)
