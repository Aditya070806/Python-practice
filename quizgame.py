def main():

    playing = input("Do you want to play? (yes/no): ").strip().lower() == "yes"
    if not playing:
        print("Maybe next time!")
        return
    
    print("Welcome to the Quiz Game!")
    score = 0

#we will ask the user 5 questions
    answer = input("Whats the full form of GPU? ")
    if answer.lower() == "graphics processing unit":
        score+=1
        print("Correct Answer")
    else:
        print("Incorrect Answer")


    answer = input("Whats the full form of CPU? ")
    if answer.lower() == "central processing unit":
        score+=1
        print("Correct Answer")
    else:
        print("Incorrect Answer")

    answer = input("Whats the full form of RAM? ")
    if answer.lower()=="random access memory":
        score+=1
        print("Correct Answer")
    else:
        print("Incorrect Answer")

    answer = input("Whats he full form of PSU? ")
    if answer.lower()== "power supply":
        score+=1
        print("Correct Answer")
    else:
        print("Incorrect Answer")

    answer = input("Whats the full form of OS? ")
    if answer.lower()== "operating system":
        score+=1
        print("Correct Answer")
    else:
        print("Incorrect Answer")

    print("Quiz is Complete")
    print("Your final score is:"+ str(score))
    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 4) * 100) + "%.")
main()
