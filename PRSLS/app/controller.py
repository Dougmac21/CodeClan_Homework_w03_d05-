from app import app
from flask import render_template
from app.models.player import *
from app.models.prs import *


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/<player_1_name>/<player_1_game_choice>/<player_2_name>/<player_2_game_choice>')
def play_page(player_1_name, player_1_game_choice, player_2_name, player_2_game_choice):
    player_1 = Player(player_1_name, player_1_game_choice)
    player_2 = Player(player_2_name, player_2_game_choice)
    the_game = Prs()
    game_result = the_game.play_game(player_1, player_2)
    return render_template('play.html', result_of_game=game_result)

@app.route('/<player_1_name>/<player_1_game_choice>/<cpu_player_name>')
def cpu_page(player_1_name, player_1_game_choice, cpu_player_name):
    player_1 = Player(player_1_name, player_1_game_choice)
    cpu_player = Player(cpu_player_name, None)
    the_game = Prs()
    game_result = the_game.play_game(player_1, cpu_player)
    return render_template('play.html', result_of_game=game_result)

@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')

@app.route('/hint')
def hint_page():
    return render_template('hint.html')

@app.route('/extra-hint')
def extra_hint_page():
    return render_template('extra-hint.html')

@app.route('/play', methods=['POST'])
def game_page():
    return render_template('play.html')