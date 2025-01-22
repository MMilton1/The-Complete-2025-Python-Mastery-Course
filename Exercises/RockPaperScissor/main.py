import random
import game_art

game_image = game_art.game_images

print("Let's play RockPaperScissors.")
for images in game_image:
    print(images)

computer_choice = random.choice(game_image)
try:
    user_pick = int(
        input("Enter your choice:\n0 - for Rock\n1 - for Paper\n2 - for Scissors")
    )
    user_choice = game_image[user_pick]
    if computer_choice == "rock" and user_choice == "paper":
        print(f"Computer Wins! with\n{computer_choice}.\nYou chose:\n{user_choice}")
    elif computer_choice == "paper" and user_choice == "rock":
        print(f"Computer Wins! with\n{computer_choice}.\nYou chose:\n{user_choice}")
    elif computer_choice == "scissors" and user_choice == "paper":
        print(f"Computer Wins! with\n{computer_choice}.\nYou chose:\n{user_choice}")
    elif computer_choice == user_choice:
        print("No winner! There is draw")
        print(f"Computer:\n{computer_choice}.\nYou:\n{user_choice}")
    else:
        print(f"You win! with:\n{user_choice}. Computer chose: \n{computer_choice}")
except IndexError:
    print("Out of range of 0 - 2. Game Over.")
except ValueError:
    print("Invalid input. Game Over.")
