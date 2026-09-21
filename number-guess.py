import random
def main():
    #prompting user for a number
    top = input("Enter top range number: ")

    if top.isdigit():
        top = int(top)

        if top <= 0:
            print("Enter a new number greater than 0")
            quit()

    else:
        print("Enter a number")
        quit()

    #prompting user to guess
    random_num = random.randint(0,top)
    guess = 0

    while True:
        guess+=1
        usr_input = input("Enter a guess: ")
        if usr_input.isdigit():
            usr_input = int(usr_input)
        else:
            print("Type a number")
            continue

        if usr_input == random_num:
            print("Correct Guess")
            break
        elif usr_input < random_num:
            print("Smaller Guess")
        else:
            print("Larger Guess")

    print(f"You guessed in {guess} guesses ")

main()


        