class PrsBasic():


    def play_game(self, player_1, player_2):

# Game logic follows.

        # Automatic capitalisation of input strings.
        player_1.name = player_1.name.capitalize()


        # Declaration of game choice parameters.
        permitted_choices = ("Paper", "Rock", "Scissors")
        cpu_player_paul_choices = ("Paper", "Rock", "Scissors")
        cpu_players = ("Paul", "Drew", "Murray", "Steve")


        # Import random number generator.
        import random


        # Define CPU game choice according to CPU player name.
        if player_2.name == "Paul":
            player_2.game_choice = random.choice(cpu_player_paul_choices)
        elif player_2.name == "Drew":
            player_2.game_choice = "Rock"
        elif player_2.name == "Murray":
            player_2.game_choice = "Scissors"
        elif player_2.name == "Steve":
            player_2.game_choice = "Paper"


        # Ensure that player selects from valid options.
        if player_1.game_choice not in permitted_choices:
            return f"{player_1.name} must pick from the permitted choices."
        

# Logic for handling of who wins given game choice combinations follows.

        # (Tie if same choice made)
        if player_1.game_choice == player_2.game_choice:
            return f"Both {player_1.name} and {player_2.name} have chosen {player_1.game_choice}. It's a tie!"


        # (else comparitive logic)
        elif player_1.game_choice == "Paper":
            if player_2.game_choice == "Rock":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Paper wraps Rock. {player_1.name} wins!"
            elif player_2.game_choice == "Scissors":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Scissors cut Paper. {player_2.name} wins!"

        
        elif player_1.game_choice == "Rock":
            if player_2.game_choice == "Scissors":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Rock crushes Scissors. {player_1.name} wins!"
            elif player_2.game_choice == "Paper":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Paper wraps Rock. {player_2.name} wins!"
                               
        
        elif player_1.game_choice == "Scissors":
            if player_2.game_choice == "Paper":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Scissors cut Paper. {player_1.name} wins!"
            elif player_2.game_choice == "Rock":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Rock crushes Scissors. {player_2.name} wins!"