import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    with open("templates/index.json", "r", encoding="utf-8") as file:
        index_data = json.load(file)
    return render_template('index.html', data=index_data)


@app.route('/welcome')
def welcome():
    with open("templates/games.json", "r", encoding="utf-8") as file:
        games = json.load(file)
    return render_template('welcome.html', games=games)


@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/about')
def about():
    return 'This is the about page.'


if __name__ == '__main__':
    app.run(debug=True, port=5000)