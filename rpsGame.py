import random, sys

print("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input()
        if player_move == "q":
            sys.exit()
        if player_move == "r" or player_move == "p" or player_move == "s":
            break
        print("Type one of r, p, s, or q.")

    if player_move == "r":
        print("ROCK versus...")
    elif player_move == "p":
        print("PAPER versus...")
    elif player_move == "s":
        print("SCISSORS versus...")

    random_number = random.randint(1, 3)
    if random_number == 1:
        computerMove = "r"
        print("ROCK")
    elif random_number == 2:
        computerMove = "p"
        print("PAPER")
    elif random_number == 3:
        computerMove = "s"
        print("SCISSORS")

    if player_move == computerMove:
        print("It is a tie!")
        ties += 1
    elif player_move == "r" and computerMove == "s":
        print("You win!")
        wins += 1
    elif player_move == "p" and computerMove == "r":
        print("You win!")
        wins += 1
    elif player_move == "s" and computerMove == "p":
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1
