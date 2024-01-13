import random
colors = ["white", "black", "red", "blue", "green", "yellow", "purple", "gray"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("I'm thinking about a color, can you guess it: ")

    while True:
        if (color == guess.lower()):
            break
        else:
            guess = input("Nope. Try again: ")

    print("You guessed it! I was thinking about", color, "color")

    play_again = input("let's play again? Type 'no' to  quit.")

    if play_again.lower() == 'no':
        break

print("I was fun,  thanks for playing!")
