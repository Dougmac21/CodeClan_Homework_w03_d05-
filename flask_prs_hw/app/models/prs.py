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
                return f"Paper wraps Rock. {player_1.name} wins!"
            elif player_2.game_choice == "Scissors":
                return f"Scissors cut Paper. {player_2.name} wins!"
            elif player_2.game_choice == "Lizard":
                return f"Lizard eats Paper. {player_2.name} Wins!"
            elif player_2.game_choice == "Spock":
                return f"Spock is disproved by Paper. {player_1.name} Wins!"
        
        elif player_1.game_choice == "Rock":
            if player_2.game_choice == "Scissors":
                return f"Rock crushes Scissors. {player_1.name} wins!"
            elif player_2.game_choice == "Paper":
                return f"Paper wraps Rock. {player_2.name} wins!"
            elif player_2.game_choice == "Lizard":
                return f"Rock crushes Lizard. {player_1.name} wins!"
            elif player_2.game_choice == "Spock":
                return f"Spock vaporises Rock. {player_2.name} wins!"                
        
        elif player_1.game_choice == "Scissors":
            if player_2.game_choice == "Paper":
                return f"Scissors cut Paper. {player_1.name} wins!"
            elif player_2.game_choice == "Rock":
                return f"Rock crushes Scissors. {player_2.name} wins!"
            elif player_2.game_choice == "Lizard":
                return f"Lizard is decapitated by Scissors. {player_1.name} wins!"
            elif player_2.game_choice == "Spock":
                return f"Spock smashes Scissors. {player_2.name} wins!"

        elif player_1.game_choice == "Lizard":
            if player_2.game_choice == "Paper":
                return f"Lizard eats Paper. {player_1.name} wins!"
            elif player_2.game_choice == "Rock":
                return f"Rock crushes Lizard. {player_2.name} wins!"
            elif player_2.game_choice == "Scissors":
                return f"Scissors decapitate Lizard. {player_2.name} wins!"
            elif player_2.game_choice == "Spock":
                return f"Lizard poisons Spock. {player_1.name} wins!"

        elif player_1.game_choice == "Spock":
            if player_2.game_choice == "Paper":
                return f"Paper disproves Spock. {player_2.name} wins!"
            elif player_2.game_choice == "Rock":
                return f"Spock vaporises Rock. {player_1.name} wins!"
            elif player_2.game_choice == "Scissors":
                return f"Spock smashes Scissors. {player_1.name} wins!"
            elif player_2.game_choice == "Lizard":
                return f"Lizard poisons Spock. {player_2.name} wins!"

