import random



def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def user_choice():
    print("--------------------")
    print(f"{user_name}, choose any one of your choice \n ---> Rock \n ---> Paper \n ---> Scissors")
    print("--------------------")
    user_input = input("Enter any one of your choice---> ").lower()

    while user_input not in ['rock', 'paper', 'scissors']:
        print(f"{user_name} Invalid choice. Please choose any one of your choice \n Rock \n Paper \n Scissors")
        user_input = input("Enter any one of your choice---> ").lower()
    return user_input

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "Rock smashes scissors. You win :)"
    elif user_choice == "paper" and computer_choice == "rock":
        return "Paper covers rock. You win :)"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "Scissors cuts paper. You win :)"
    else:
        return "Computer Wins :("
    
"""def play_game()
    while True:
        user_choice = user_choice()
        computer_choice = computer_choice()
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
        print(winner(user_choice, computer_choice))"""

while True:
    print("-----------------------------------------")
    print("...Welcome to Rock Paper Scissors Game...")
    print("-----------------------------------------")
    user_name = input("Enter your name---> ").capitalize()
    if user_name is None:
        print("Invalid input, Please enter your name")
    else:
        if len(user_name) == 0:
            print("Invalid input, Please enter your name")
        elif not user_name.isalpha():
            print("Error: name must be in alpahbets")
        else:
            print(f"{user_name}, you are welcome to the Rock Paper Scissors Game")

            user_choice = user_choice()
            computer_choice = computer_choice()
            print(f"\nYou chose---> {user_choice}, computer chose---> {computer_choice}.\n")
            print(winner(user_choice, computer_choice))
    print("-----------------------------")
    cont = input(f"{user_name}, Please do you want to continue the game (yes/no)---> ").lower()
    if cont != "no":
        continue
    else:
        print("-----------------------------")
        print(f"Thank you for playing {user_name}. Goodbye, Have a nice day :)")
        break


