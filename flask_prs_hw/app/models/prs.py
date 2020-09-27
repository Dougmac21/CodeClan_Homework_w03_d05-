class Prs():

    # def __init__(self, player_1, player_2):
    #     self.player_1 = player_1
    #     self.player_2 = player_2
        

    def play_game(self, player_1, player_2):

        permitted_choices = ("Paper", "Rock", "Scissors", "Lizard", "Spock")


        if player_1.game_choice not in permitted_choices and player_2.game_choice not in permitted_choices:
            return f"Both {player_1.name} and {player_2.name} must pick from the permitted choices!"
        elif player_1.game_choice not in permitted_choices:
            return f"{player_1.name} must pick from the permitted choices!"
        elif player_2.game_choice not in permitted_choices:
            return f"{player_2.name} must pick from the permitted choices!"
        
        if player_1.game_choice == player_2.game_choice:
            return f"Both {player_1.name} and {player_2.name} have chosen the same thing so it's a tie!"

        elif player_1.game_choice == "Paper":
            if player_2.game_choice == "Rock":
                return "Paper wraps Rock. Player 1 wins!"
            elif player_2.game_choice == "Scissors":
                return "Scissors cut Paper. Player 2 wins!"
            elif player_2.game_choice == "Lizard":
                return "Lizard eats Paper. Player 2 Wins!"
            elif player_2.game_choice == "Spock":
                return "Spock is disproved by Paper. Player 1 Wins!"
        
        elif player_1.game_choice == "Rock":
            if player_2.game_choice == "Scissors":
                return "Rock crushes Scissors. Player 1 wins!"
            elif player_2.game_choice == "Paper":
                return "Paper wraps Rock. Player 2 wins!"
            elif player_2.game_choice == "Lizard":
                return "Rock crushes Lizard. Player 1 wins!"
            elif player_2.game_choice == "Spock":
                return "Spock vaporises Rock. Player 2 wins!"                
        
        elif player_1.game_choice == "Scissors":
            if player_2.game_choice == "Paper":
                return "Scissors cut Paper. Player 1 wins!"
            elif player_2.game_choice == "Rock":
                return "Rock crushes Scissors. Player 2 wins!"
            elif player_2.game_choice == "Lizard":
                return "Lizard is decapitated by Scissors. Player 1 wins!"
            elif player_2.game_choice == "Spock":
                return "Spock smashes Scissors. Player 2 wins!"

        elif player_1.game_choice == "Lizard":
            if player_2.game_choice == "Paper":
                return "Lizard eats Paper. Player 1 wins!"
            elif player_2.game_choice == "Rock":
                return "Rock crushes Lizard. Player 2 wins!"
            elif player_2.game_choice == "Scissors":
                return "Scissors decapitate Lizard. Player 2 wins!"
            elif player_2.game_choice == "Spock":
                return "Lizard poisons Spock. Player 1 wins!"

        elif player_1.game_choice == "Spock":
            if player_2.game_choice == "Paper":
                return "Paper disproves Spock. Player 2 wins!"
            elif player_2.game_choice == "Rock":
                return "Spock vaporises Rock. Player 1 wins!"
            elif player_2.game_choice == "Scissors":
                return "Spock smashes Scissors. Player 1 wins!"
            elif player_2.game_choice == "Lizard":
                return "Lizard poisons Spock. Player 2 wins!"

