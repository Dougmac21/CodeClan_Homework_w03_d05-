class PrsPlus():


    # def __init__(self, player_1, player_2):
    #     self.player_1 = player_1
    #     self.player_2 = player_2
        

    def play_game(self, player_1, player_2):

# Game logic follows.

        # Automatic capitalisation of input strings.
        player_1.name = player_1.name.capitalize()
        player_1.game_choice = player_1.game_choice.capitalize()


        # Declaration of game choice parameters.
        permitted_choices = ("Paper", "Rock", "Scissors", "Lizard", "Spock", "Shotgun")
        cpu_player_malcolm_choices = ("Paper", "Rock", "Scissors", "Lizard", "Spock")
        cpu_player_hannah_choices = ("Scissors", "Rock")    # Spock always beats Hannah
        cpu_player_chris_choices = ("Paper", "Lizard")      # Scissors always beats Chris
        cpu_players = ("Hal", "Morag", "Chris", "Hannah", "Zsolt", "Malcolm", "Harrison")

        # Fixing of winning game choices given player choice.
        if player_1.game_choice == "Paper":
            winning_choice = "Scissors"
        elif player_1.game_choice == "Rock":
            winning_choice = "Paper"
        elif player_1.game_choice == "Scissors":
            winning_choice = "Spock"
        elif player_1.game_choice == "Lizard":
            winning_choice = "Rock"
        elif player_1.game_choice == "Spock":
            winning_choice = "Lizard"
        elif player_1.game_choice == "Shotgun":
            winning_choice = "Surrender"

        # Import random number generator.
        import random

        # Select randon CPU player.
        if player_2.name == "Cpu":
            player_2.name = random.choice(cpu_players)
        
        # Define CPU game choice according to CPU player name.
        if player_2.name == "Emily":
            player_2.game_choice = "Paper"
        elif player_2.name == "Eugene":
            player_2.game_choice = "Rock"
        elif player_2.name == "Chris":
            player_2.game_choice = random.choice(cpu_player_chris_choices)
        elif player_2.name == "Hannah":
            player_2.game_choice = random.choice(cpu_player_hannah_choices)
        elif player_2.name == "Zsolt":
            player_2.game_choice = "Spock"
        elif player_2.name == "Malcolm":
            player_2.game_choice = random.choice(cpu_player_malcolm_choices)
        elif player_2.name == "Harrison":
            player_2.game_choice = winning_choice


        # Ensure that player selects from valid options.
        elif player_1.game_choice not in permitted_choices:
            return f"{player_1.name} must pick from the permitted choices!"
        


# Logic for handling of who wins given game choice combinations follows.

        # (Tie if same choice made)
        if player_1.game_choice == player_2.game_choice:
            return f"Both {player_1.name} and {player_2.name} have chosen {player_1.game_choice}. It's a tie!"

        elif player_1.game_choice == "Paper":
            if player_2.game_choice == "Rock":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Paper wraps Rock. {player_1.name} wins!"
            elif player_2.game_choice == "Scissors":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Scissors cut Paper. {player_2.name} wins!"
            elif player_2.game_choice == "Lizard":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Lizard eats Paper. {player_2.name} Wins!"
            elif player_2.game_choice == "Spock":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Spock is disproved by Paper. {player_1.name} Wins!"
            elif player_2.game_choice == "Shotgun":
                return f"{player_2.name} must pick from the permitted choices!"
            elif player_2.game_choice == "Surrender":
                return f"{player_2.name} must pick from the permitted choices!"
        
        elif player_1.game_choice == "Rock":
            if player_2.game_choice == "Scissors":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Rock crushes Scissors. {player_1.name} wins!"
            elif player_2.game_choice == "Paper":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Paper wraps Rock. {player_2.name} wins!"
            elif player_2.game_choice == "Lizard":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Rock crushes Lizard. {player_1.name} wins!"
            elif player_2.game_choice == "Spock":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Spock vaporises Rock. {player_2.name} wins!"
            elif player_2.game_choice == "Shotgun":
                return f"{player_2.name} must pick from the permitted choices!"
            elif player_2.game_choice == "Surrender":
                return f"{player_2.name} must pick from the permitted choices!"                                
        
        elif player_1.game_choice == "Scissors":
            if player_2.game_choice == "Paper":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Scissors cut Paper. {player_1.name} wins!"
            elif player_2.game_choice == "Rock":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Rock crushes Scissors. {player_2.name} wins!"
            elif player_2.game_choice == "Lizard":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Lizard is decapitated by Scissors. {player_1.name} wins!"
            elif player_2.game_choice == "Spock":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Spock smashes Scissors. {player_2.name} wins!"
            elif player_2.game_choice == "Shotgun":
                return f"{player_2.name} must pick from the permitted choices!"
            elif player_2.game_choice == "Surrender":
                return f"{player_2.name} must pick from the permitted choices!"

        elif player_1.game_choice == "Lizard":
            if player_2.game_choice == "Paper":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Lizard eats Paper. {player_1.name} wins!"
            elif player_2.game_choice == "Rock":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Rock crushes Lizard. {player_2.name} wins!"
            elif player_2.game_choice == "Scissors":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Scissors decapitate Lizard. {player_2.name} wins!"
            elif player_2.game_choice == "Spock":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Lizard poisons Spock. {player_1.name} wins!"
            elif player_2.game_choice == "Shotgun":
                return f"{player_2.name} must pick from the permitted choices!"
            elif player_2.game_choice == "Surrender":
                return f"{player_2.name} must pick from the permitted choices!"

        elif player_1.game_choice == "Spock":
            if player_2.game_choice == "Paper":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Paper disproves Spock. {player_2.name} wins!"
            elif player_2.game_choice == "Rock":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Spock vaporises Rock. {player_1.name} wins!"
            elif player_2.game_choice == "Scissors":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Spock smashes Scissors. {player_1.name} wins!"
            elif player_2.game_choice == "Lizard":
                return f"{player_1.name} chose {player_1.game_choice}. {player_2.name} chose {player_2.game_choice}. Lizard poisons Spock. {player_2.name} wins!"
            elif player_2.game_choice == "Shotgun":
                return f"{player_2.name} must pick from the permitted choices!"
            elif player_2.game_choice == "Surrender":
                return f"{player_2.name} must pick from the permitted choices!"

        elif player_1.game_choice == "Shotgun":
            if player_2.name == "Harrison":
                return f"{player_1.name} chose {player_1.game_choice} because {player_2.name} is cheating. {player_2.name} chose {player_2.game_choice}. {player_1.name} wins!"
            elif player_2.name != "Harrison":
                return f"{player_1.name} must pick from the permitted choices!"