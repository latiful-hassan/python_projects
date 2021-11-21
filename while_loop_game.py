print("Guess the Code Word")
print()

secret = "yami"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        print()
        print("You have no attempts left.")

while guess == secret:
    print()
    print("You guessed correctly, have a cookie!")
    break
