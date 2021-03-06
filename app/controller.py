from app import app
from flask import render_template, request, redirect
from app.models.player import *
from app.models.prs_plus import *


@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'POST':

        req = request.form
        print(req)

        player_1_name = request.form.get("player_1")
        player_1_game_choice = request.form.get("player_1_weapon")
        cpu_player_name = request.form.get("cpu-player")

        player_1 = Player(player_1_name, player_1_game_choice)
        cpu_player = Player(cpu_player_name, None)
        the_game = PrsPlus()
        game_result = the_game.play_game(player_1, cpu_player)
        
        return render_template('index.html', result_of_game=game_result)

    return render_template('index.html')

@app.route('/stuck')
def stuck_page():
    return render_template('stuck.html')


@app.route('/<player_1_name>/<player_1_game_choice>/<cpu_player_name>')
def cpu_page(player_1_name, player_1_game_choice, cpu_player_name):
    player_1 = Player(player_1_name, player_1_game_choice)
    cpu_player = Player(cpu_player_name, None)
    the_game = PrsPlus()
    game_result = the_game.play_game(player_1, cpu_player)
    return render_template('index.html', result_of_game=game_result)