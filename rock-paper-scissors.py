import random
def main():
    user_wins = 0
    comp_wins = 0
    draw = 0

    options = ["rock","paper","scissors"]

    while True:
        usr_input = input("Rock/Paper/Scissor or Q/q to quit: ").lower()
        if usr_input == "q":
            print("game quit")
            break
        if usr_input not in options:
            continue
        rand_pick = random.randint(0,2)
        comp_input = options[rand_pick]
        print(f"Computer picked:{comp_input}")
        if usr_input == "rock" and comp_input == "scissors":
            print(f"Computer picked: {comp_input}\n You won")
            user_wins+=1
        elif usr_input == "paper" and comp_input == "rock":
            print(f"Computer picked: {comp_input}\n You won")
            user_wins+=1
        elif usr_input =="scissors" and comp_input == "paper":
            print(f"Computer picked: {comp_input}\n You won")
            user_wins+=1
        elif usr_input == comp_input:
            print("Draw")
            draw+=1
        else:
            print(f"Computer picked:{comp_input}\n Computer won")
            comp_wins+=1
    print("-" * 22)
    print(f"You won: {user_wins}")
    print(f"Computer won:{comp_wins}")
    print(f"Game was Draw: {draw}")
    print("-" * 22)


main()


    