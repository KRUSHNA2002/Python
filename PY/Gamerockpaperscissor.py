import random
def choose_choices():
    options=["Rock","Paper","Scissor"]

    Player= input("Enter your Choice [Rock,Paper,Scissor]")

    if Player not in options:
     print("Please Enter Valid Choice")
     return choose_choices()


    Computer = random.choice(options)

    global choices
    choices = {"player":Player,"Computer":Computer}

    return choices

def check_win(Player, Computer):

    if Player == Computer:
        print("Both Choices are Same")
        print("Match Tied")

    elif Player == "Rock" and Computer == "Scissor":
        print("Your Choices Rock And Computer choose Scissor")
        print("You Win")

    elif Player == "Paper" and Computer == "Rock":
        print("Your Choices Paper And Computer choose Rock")
        print("You Win")

    elif Player == "Scissor" and Computer == "Paper":
        print("Your choose Scissor And Computer choose Paper")
        print("You Win")

    else:
        print(f"Your choose {Player} And Computer choose {Computer}")
        print("Computer Wins")

choices=choose_choices()

check_win(choices["player"],choices["Computer"])