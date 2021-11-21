import random
p = input("Please enter 'Rock', 'Paper' or 'Scissors': ").lower()
print("Player plays: " + p)
rng = random.randint(0, 2)

player_wins = 0
cpu_wins = 0

while player_wins < 2 and cpu_wins < 2:
    if rng == 0:
        cpu = "rock"
    elif rng == 1:
        cpu = "paper"
    else:
        cpu = "scissors"
    print("Computer plays: " + cpu)

    if p or cpu != "":
        if p == cpu:
            print("Draw!")
        elif p == "rock" and cpu == "scissors":
            print("Player wins!")
            player_wins += 1
        elif p == "paper" and cpu == "rock":
            print("Player wins!")
            player_wins += 1
        elif p == "scissors" and cpu == "paper":
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            cpu_wins += 1
    else:
        print("Something went wrong! Enter 'Rock', 'Paper' or 'Scissors'")