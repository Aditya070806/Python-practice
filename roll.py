import random

def main():
    def roll_dice():
        min_val = 1
        max_val = 6
        roll= random.randint(min_val, max_val)
        return roll

    while True:
        players = input("How many players you want to play with(2-4)")
        if players.isdigit():
            players = int(players)
            if 2 <= players <=4:
                break
            else:
                print("Must be 2-4 players")
        else:
            print("Enter a valid number")

    max_score = 30
    ply_scores =[0 for i in range (players)]

    while max(ply_scores) < max_score:
        for player_idx in range(players):
            print("\nPlayer number", player_idx + 1, "turn has just started!")
            print("Your total score is:", ply_scores[player_idx], "\n")
            current_score = 0

            while True:
                rolling = input("Roll again y/n: ")
                if rolling.lower().strip()!="y":
                    break

                value = roll_dice()
                if value == 1:
                    print("You rolled a 1, That's a turn done")
                    current_score = 0
                    break
                else:
                    
                    current_score+=value
                    print(f"You rolled a {value}")

                print(f"Your total score is {current_score}")

            ply_scores[player_idx] += current_score
            print(f"Your total score is {ply_scores[player_idx]}")

        max_score = max(ply_scores)
        winning_idx = ply_scores.index(max_score)
        print(f"Player number {winning_idx + 1} is the winner with a score of: {max_score}")

main()