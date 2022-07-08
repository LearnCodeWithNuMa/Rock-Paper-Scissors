from random import *

def game():
    print("""                                                                                                                                                                                                            
     /$$$$$$$      /$$$$$$$   /$$$$$$ 
    | $$__  $$    | $$__  $$ /$$__  $$
    | $$  \ $$    | $$  \ $$| $$  \__/
    | $$$$$$$/    | $$$$$$$/| $$      
    | $$__  $$    | $$____/ | $$      
    | $$  \ $$    | $$      | $$    $$
    | $$  | $$ /$$| $$ /$$  |  $$$$$$/
    |__/  |__/|__/|__/|__/   \______/                                
    """)

    rule = [
        [2, 0, 1],
        [1, 2, 0],
        [0, 1, 2]
    ]

    option = ["Rock", "Paper", "Scissors"]
    for i in range(len(option)):
        print("{}. {}".format(i + 1, option[i]))

    player = None
    while player not in [i for i in range(len(option))]:
        try:
            player = int(input("\nPlayer: ")) - 1
        except ValueError:
            print("Error: This is not one of the possible choices !")
    bot = option.index(choice(option))
    print("Bot: {}".format(option[bot]))

    result = {
        0: "Loose",
        1: "Win",
        2: "Equality"
    }
    print("\n{}".format(result[rule[player][bot]]))

game()
