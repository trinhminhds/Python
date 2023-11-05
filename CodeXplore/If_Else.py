import random as r


def get_choice(choices):
    if choices == "R":
        return "Rock"
    elif choices == "P":
        return "Paper"
    elif choices == "S":
        return "Scissor"
    else:
        return "Not a valid choice"


def main():
    print("Welcome to Rock, Paper, Scissor Game")
    print("[R]=Rock ,[P]=Paper ,[S]=Scissor and [Q]=Quit Game ")

    choices = ["R", "P", "S"]
    counter = 1
    game_on = True

    while game_on:
        user_choices = input(f"Game #{counter}. Pleas enter your choice: ")
        user_choices = user_choices.upper()
        if user_choices == "Q":
            print("Thank for joining! Have a nice day.")
            game_on = False
        else:
            random_index = r.randint(0, 2)
            computer_choices = choices[random_index]
            print(
                f"You select {get_choice(user_choices)} vs Computer choice is {get_choice(computer_choices)}"
            )

            if user_choices == "R" and computer_choices == "S":
                print("Congrats, you win. Rock beats Scissor")
            elif user_choices == "P" and computer_choices == "R":
                print("Congrats, you win. Paper covers Rock")
            elif user_choices == "S" and computer_choices == "P":
                print("Congrats, you win. Scissor cuts Paper")
            elif user_choices == "S" and computer_choices == "R":
                print("So sorry, computer wins. Rock beats Scissor")
            elif user_choices == "R" and computer_choices == "P":
                print("So sorry, computer wins. Paper covers Rock")
            elif user_choices == "P" and computer_choices == "S":
                print("So sorry, computer wins. Scissor beats Paper")
            elif user_choices == computer_choices:
                print(
                    f"Wow! It't a Draw. Both you and computer selected {get_choice(user_choices)}"
                )
            else:
                print("Invalid option: Please enter [R,P,S or Q] only")

            counter += 1
            print("-" * 40)


if __name__ == "__main__":
    main()
