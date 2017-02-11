from flask import Flask, render_template, jsonify 

app = Flask (__name__)

# home
@app.route('/')
def index():
    return render_template('home.html')

# birthday
@app.route('/birthday')
def birthday():
    return ('July 16,1992')

# name
@app.route('/greeting/<name>')
def greet(name):
    return('Hello {}!'.format(name))

# add
@app.route('/add/<int:a>/<int:b>')
def sum(a, b):
    return "{0} plus {1} is {2}.".format(a, b, a + b)

# multiply
@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return "{0} mulitplied by {1} is {2}.".format(a, b, a * b)

# subtract
@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return "{0} minus {1} is {2}".format(a, b, a - b)

# fave foods
@app.route('/favoritefoods')
def favorite_foods():
    foods = ['pho', 'bacon', 'tri-tip', 'sushi']
    return jsonify(foods)
