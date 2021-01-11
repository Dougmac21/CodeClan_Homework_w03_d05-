from app import app
from flask import render_template
from app.models.player import *
from app.models.prs_plus import *


@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/instructions')
def instructions_page():
    return render_template('instructions.html')

@app.route('/stuck')
def stuck_page():
    return render_template('stuck.html')

@app.route('/play', methods=['GET', 'POST'])
def game_page():
    return render_template('play.html')

@app.route('/<player_1_name>/<player_1_game_choice>/<cpu_player_name>')
def cpu_page(player_1_name, player_1_game_choice, cpu_player_name):
    player_1 = Player(player_1_name, player_1_game_choice)
    cpu_player = Player(cpu_player_name, None)
    the_game = PrsPlus()
    game_result = the_game.play_game(player_1, cpu_player)
    return render_template('play.html', result_of_game=game_result)