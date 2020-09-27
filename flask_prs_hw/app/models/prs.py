class Prs():

    # def __init__(self, player_1, player_2):
    #     self.player_1 = player_1
    #     self.player_2 = player_2
        

    def play_game(self, player_1, player_2):

        player_1.name.capitalize
        if player_2.name == "cpu" or "CPU" or "CPu" or "cPU" or "cPu" or "cpU":
            player_2.name.upper
        else:
            player_2.name.capitalize
        player_1.game_choice.capitalize
        if player_2.game_choice == None:
            pass
        else:
            player_2.game_choice.capitalize
        permitted_choices = ("Paper", "Rock", "Scissors", "Lizard", "Spock")
        cpu_player_data_choices = ("Lizard", "Rock")
        cpu_players = ("Hal", "Morag", "Chris", "Hannah", "Zsolt", "Malcolm", "Harrison", "CPU")

        winning_choice = "Shotgun"
        if player_1.game_choice == "Paper":
            winning_choice == "Scissors"
        elif player_1.game_choice == "Rock":
            winning_choice == "Paper"
        elif player_1.game_choice == "Scissors":
            winning_choice == "Spock"
        elif player_1.game_choice == "Lizard":
            winning_choice == "Rock"
        elif player_1.game_choice == "Spock":
            winning_choice == "Lizard"

        import random
        if player_2.name == "CPU":
            player_2.name = random.choice(cpu_players)
        elif player_2.name == "Hal":
            player_2.game_choice = "Paper"
        elif player_2.name == "Morag":
            player_2.game_choice = "Rock"
        elif player_2.name == "Chris":
            player_2.game_choice = "Scissors"
        elif player_2.name == "Hannah":
            player_2.game_choice = random.choice(cpu_player_data_choices)
        elif player_2.name == "Zsolt":
            player_2.game_choice = "Spock"
        elif player_2.name == "Malcolm":
            player_2.game_choice = random.choice(permitted_choices)
        elif player_2.name == "Harrison":
            player_2.game_choice = winning_choice

        if player_1.game_choice not in permitted_choices and player_2.game_choice not in permitted_choices:
            return f"Both {player_1.name} and {player_2.name} must pick from the permitted choices!"
        elif player_1.game_choice not in permitted_choices:
            return f"{player_1.name} must pick from the permitted choices!"
        elif player_2.game_choice not in permitted_choices:
            return f"{player_2.name} must pick from the permitted choices!"
        
        if player_1.game_choice == player_2.game_choice:
            return f"Both {player_1.name} and {player_2.name} have chosen {player_1.game_choice} so it's a tie!"

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

