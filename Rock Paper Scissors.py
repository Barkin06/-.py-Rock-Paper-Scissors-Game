import random
while True:
    choices = ["rock","paper","scissors"]

    PC = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock,paper or scissors? ").lower()

    if PC == player:
        print("PC: ",str(PC))
        print("player: ",player)
        print("TIE!")
    elif player == "rock":
        if PC == "paper":
            print("PC: ", str(PC))
            print("player: ", player)
            print("YOU LOSE!")
        if PC == "scissors":
            print("PC: ", str(PC))
            print("player: ", player)
            print("YOU WIN!")
    elif player == "scissors":
        if PC == "rock":
            print("PC: ", str(PC))
            print("player: ", player)
            print("YOU LOSE!")
        if PC == "paper":
            print("PC: ", str(PC))
            print("player: ", player)
            print("YOU WIN!")
    elif player == "paper":
        if PC == "scissors":
            print("PC: ", str(PC))
            print("player: ", player)
            print("YOU LOSE!")
        if PC == "rock":
            print("PC: ", str(PC))
            print("player: ", player)
            print("YOU WIN!")

    play_again = input("Play again? (yes/no) ").lower()
    if play_again != "yes":
        break
print("BYE!")
