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
            print("User won the game")
            user_wins+=1
        elif usr_input == "paper" and comp_input == "rock":
            print("User won the game")
            user_wins+=1
        elif usr_input =="scissors" and comp_input == "paper":
            print("User won the game")
            user_wins+=1
        elif usr_input == comp_input:
            print("Draw")
            draw+=1
        else:
            print("you lost")
            comp_wins+=1
    print(f"You won the game{user_wins} times")
    print(f"Computer won the game{comp_wins} times")
    print(f"Game was Draw for {draw} times")
main()


    