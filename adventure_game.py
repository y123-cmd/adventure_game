import random

def start_game():
    print("Welcome to the Adventure Game!")
    print("You wake up in a dark forest. There are two paths ahead.")
    print("1. Take the left path.")
    print("2. Take the right path.")
    
    choice = input("What do you choose? (1 or 2): ")
    
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice! Try again.")
        start_game()

def left_path():
    print("\nYou walk along the left path and encounter a river.")
    print("1. Try to swim across.")
    print("2. Look for a bridge.")
    
    choice = input("What do you choose? (1 or 2): ")
    
    if choice == "1":
        print("\nYou try to swim but the current is too strong. You drown. Game Over!")
        replay_game()
    elif choice == "2":
        print("\nYou find a bridge and safely cross the river. You win!")
        replay_game()
    else:
        print("Invalid choice! Try again.")
        left_path()

def right_path():
    print("\nYou walk along the right path and see a cave.")
    print("1. Enter the cave.")
    print("2. Avoid the cave and keep walking.")
    
    choice = input("What do you choose? (1 or 2): ")
    
    if choice == "1":
        print("\nYou enter the cave and find a treasure chest. You win!")
        replay_game()
    elif choice == "2":
        print("\nYou keep walking and fall into a hidden pit. Game Over!")
        replay_game()
    else:
        print("Invalid choice! Try again.")
        right_path()

def replay_game():
    choice = input("\nDo you want to play again? (yes or no): ").lower()
    if choice == "yes":
        start_game()
    elif choice == "no":
        print("Thanks for playing! Goodbye!")
    else:
        print("Invalid choice! Try again.")
        replay_game()

if __name__ == "__main__":
    start_game()

