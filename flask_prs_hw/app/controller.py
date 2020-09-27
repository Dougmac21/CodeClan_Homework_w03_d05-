from app import app
from flask import render_template
from app.models.player import *
from app.models.prs import *

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/<player_1>/<player_1_game_choice>/<player_2>/<player_2_game_choice>')
def game_page():
    return render_template('game_page.html')
