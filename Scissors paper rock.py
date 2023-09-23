import random

def play_game():
    choices = ["scissors","paper","rock"]
    you_win_count = 0
    computer_win_count = 0

    while you_win_count < 2 and computer_win_count < 2:
        computer_choice = random.choice(choices)
        player_choice = input("Enter your choice (scissors/paper/rock): ").lower()

        if player_choice not in choices:
           print("Invalid choice. Please try again.")
           continue

        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
           print("It's a draw! Let's play that round again.")
           continue

        if (player_choice == "rock" and computer_choice == "scissors") or \
           (player_choice == "paper" and computer_choice == "rock") or \
           (player_choice == "scissors" and computer_choice == "paper"):
           print("You win this round!")
           you_win_count += 1
    
        elif (player_choice == "scissors" and computer_choice == "rock") or \
           (player_choice == "rock" and computer_choice == "paper") or \
           (player_choice == "paper" and computer_choice == "scissors"):
           print("Computer wins this round.")
           computer_win_count += 1

    if you_win_count == 2:
         print("You win!")
    elif computer_win_count == 2:
         print("Sorry, you lost")

play_game()