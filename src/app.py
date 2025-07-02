import json
from flask import Flask, render_template

app = Flask(__name__)

games = [
    {
        "name": "Minecraft",
        "slug": "minecraft",
        "image": "static/Minecraft.jpg",
        "description": "Host modded or vanilla servers with full plugin support.",
        "status": "available",
    },
    {
        "name": "Counter-Strike 2",
        "slug": "cs2",
        "image": "static/Counter-Strike.jpg",
        "description": "Competitive FPS server with custom map support.",
        "status": "available",
    },
    {
        "name": "Valheim",
        "slug": "valheim",
        "image": "static/Valheim.jpg",
        "description": "Viking co-op survival in a procedurally generated world.",
        "status": "available",
    },
    {
        "name": "More Games",
        "image": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=800",
        "description": "We're working on supporting even more titles. Stay tuned!",
        "status": "coming_soon",
    }
]



@app.route('/')
def index():
    with open("templates/index.json", "r", encoding="utf-8") as file:
        index_data = json.load(file)
    return render_template('index.html', data=index_data)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html', games=games)


@app.route('/about')
def about():
    return 'This is the about page.'


if __name__ == '__main__':
    app.run(debug=True, port=5000)