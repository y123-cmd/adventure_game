import random

def print_line():
    print("-" * 50)


player = {
    "health": 100,
    "strength": 10,
    "inventory": []
}

def display_stats():
    print(f"Health: {player['health']}, Strength: {player['strength']}")
    print(f"Inventory: {', '.join(player['inventory']) if player['inventory'] else 'Empty'}")
    print_line()

def forest_path():
    print("You venture into the dark forest. Strange sounds echo around you.")
    print("Suddenly, a wild beast appears!")
    print("1. Fight it.")
    print("2. Run away.")
    choice = input("Choose an action (1 or 2): ")
    
    if choice == "1":
        if "sword" in player["inventory"]:
            print("You draw your sword and slay the beast!")
            player["strength"] += 5
        else:
            print("You fight bare-handed but get injured. The beast escapes.")
            player["health"] -= 30
    elif choice == "2":
        print("You run back to the safety of the clearing.")
    else:
        print("Invalid choice! The beast attacks you!")
        player["health"] -= 20
    
    display_stats()

def cave_path():
    print("You find a mysterious cave. It's dark and eerie.")
    print("1. Explore the cave.")
    print("2. Stay outside.")
    choice = input("Choose an action (1 or 2): ")
    
    if choice == "1":
        event = random.choice(["treasure", "trap", "nothing"])
        if event == "treasure":
            print("You find a shining sword! It increases your strength.")
            player["inventory"].append("sword")
            player["strength"] += 10
        elif event == "trap":
            print("It's a trap! A boulder falls, and you barely escape.")
            player["health"] -= 40
        else:
            print("The cave is empty. You leave disappointed.")
    elif choice == "2":
        print("You stay outside and feel safer.")
    else:
        print("Invalid choice! A rockslide occurs, and you get injured.")
        player["health"] -= 20
    
    display_stats()

def final_choice():
    print("After your journey, you arrive at a massive castle gate.")
    print("1. Enter the castle.")
    print("2. Walk away and return home.")
    choice = input("Choose an action (1 or 2): ")
    
    if choice == "1":
        if player["strength"] > 15:
            print("You defeat the guards with your strength and claim the treasure inside!")
            print("Congratulations, you won!")
        else:
            print("The guards overpower you. You lose.")
    elif choice == "2":
        print("You walk away, choosing safety over adventure. The end.")
    else:
        print("Invalid choice! The guards notice you and attack!")
        player["health"] -= 30
        if player["health"] <= 0:
            print("You succumb to your injuries. Game Over.")
        else:
            print("You escape barely alive.")
    display_stats()


def start_game():
    print("Welcome to the Text Adventure Game!")
    display_stats()
    print("You find yourself at a crossroads.")
    print("1. Take the forest path.")
    print("2. Take the cave path.")
    choice = input("Choose a path (1 or 2): ")

    if choice == "1":
        forest_path()
    elif choice == "2":
        cave_path()
    else:
        print("Invalid choice! You wander aimlessly and lose health.")
        player["health"] -= 10

    if player["health"] > 0:
        final_choice()
    else:
        print("You collapse from exhaustion. Game Over.")


start_game()

