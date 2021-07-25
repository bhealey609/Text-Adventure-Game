## ACTIONS ##

def you_died(why):
    print(f"{why} Game over!")
    exit(0)

## END ACTIONS ##

## CHARACTERS ##

def guard():

    actions_dict = {
        "check": "It appears the guard is still sleeping. You need to get to that door behind him. What are you waiting for?",
        "sneak": "You approach the guard, careful not to wake him. You slowly ease the door open and slip out.",
        "attack": "You run towards the sleeping guard and knock him on the head with the hilt of your sword. Unfortunately, it wasn't hard enough."}

    while True:
        print("What do you do to the guard? You can [attack], [check], or [sneak] past.")
        action = input("> ").lower()
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "sneak":
                print("You are now outside, home free! Huzzah!\n")
                return
            elif action == "attack":
                you_died("The guard wakes with a startled grunt, swiftly produces a dagger, and plunges it into your heart.")
                return

    ## END CHARACTERS ##

    ## ROOMS ##

def blue_door_room():
    chest = ["diamonds", "gold", "silver", "sword"]
    print("You're in a room with a wooden treasure chest on the left and a sleeping guard in front of a door on the right.")
    action = input("Do you go [left] or [right]? > ")

    if action.lower() in ["left", "l"]:
        print("Ooh, treasure!")
        print("[Open] the chest or [leave] it alone?")

        choice = input("> ")
        if choice.lower() == "open":
            print("The chest creaks open, but thankfully the guard doesn't wake.")
            print("You find:")
            for treasure in chest:
                print(treasure)
            num_items = len(chest)
            print(f"Enter [1] to take {num_items} item(s) from chest, or press [2] to leave it alone.")

            treasure_choice = input("> ")
            if treasure_choice == "1":
                chest.remove("sword")
                print("\tYou take the newer, shinier sword from the treasure chest.")
                print("\tYou drop your old crappy sword in the empty treasure chest.")

                temp_treasure_list = chest[:]
                treasure_contents = ", ".join(chest)
                print(f"\tYou also receive {treasure_contents}.")

                for treasure in temp_treasure_list:
                    chest.remove(treasure)
                chest.append("crappy sword")
                print(f"You slowly close the lid of the chest, now containing {chest}.")
                print("Now onward past the sleeping guard and the door to freedom.")
                guard()

            elif treasure_choice == "2":
                print("Who needs treasure?")
                blue_door_room()
            else:
                blue_door_room()

        elif choice.lower() == "leave":
            print("Who needs treasure?")
            blue_door_room()
        else:
            print("You must choose [open] or [leave]")
            blue_door_room()

    elif action.lower() in ["right", "r"]:
        print("The guard seems more interesting. Let's go that way!")
        guard()
    else:
        print("You must choose [left] or [right].")
        blue_door_room()

def red_door_room():
    print("You encounter a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you [run] for your life or [stay] and fight?")

    next_move = input("> ")
    if next_move.lower() == "run":
        start_adventure()
    elif next_move.lower() == "stay":
        you_died("The dragon devours you.")
    else:
        print("Sorry, you must choose [run] or [stay]")
        red_door_room()

## END ROOMS ##

def get_player_name():
    name = input("What's your name? > ")
    alt_name = "Rainbow Unicorn"
    answer = input(f"Your name is {alt_name.upper()}, is that correct? [Y|N] > ")

    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print(f"You're fun, {name.upper()}. Let's begin the adventure!")
    elif answer.lower() in ["n", "no"]:
        print(f"Ok, fine. {name.upper()} it is. Let's begin the adventure!")
    else:
        print(f"Answer not recognized, so {alt_name.upper()} it is.")
        name = alt_name
    return name

def start_adventure():
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you go through the [red] door or [blue] door? > ")

    # Pick door to a room
    if door_picked.lower() == "red":
        print("You chose the red door.")
        red_door_room()
    elif door_picked.lower() == "blue":
        print("You chose the blue door.")
        blue_door_room()
    else:
        print("Sorry, you must choose [red] or [blue].")
        start_adventure()

def main():

    player_name = get_player_name()

    start_adventure()

    print("\nTHE END\n")
    print(f"Thanks for playing, {player_name.upper()}")

    # print(f"Your name is {name.upper()}.")
    # start_adventure()

if __name__ == '__main__':
    main()
