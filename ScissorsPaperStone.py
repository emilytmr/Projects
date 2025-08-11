import random

moves = ["scissors", "paper", "stone"]

player = ""
com = ""

while True:
    player = input("Scissors, Paper, Stone or 0 to end:").lower()
    com = random.choice(moves)

    if player == "0":
        break

    print(f"You: {player}")

    if player not in moves:
        print("Invalid")
        continue

    print(f"Computer: {com}")

    if com == player:
        print("Draw")

    else:
        if com == "scissors" and player == "paper":
            print("Lose")
        elif com == "paper" and player == "stone":
            print("Lose")
        elif com == "stone" and player == "scissors":
            print("Lose")
        else:
            print("Win")

