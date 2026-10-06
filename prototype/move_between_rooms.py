"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# TODO: Set the player's starting room for the simplified prototype.
current_room = "Great Hall"

print("Welcome to the SImplified Dragon Text Game!")
print("Valid command: go north, go, south, go east, go west, exit.")
print("There are no items in this simplified version. \n")


# TODO: Create the gameplay loop required by the milestone.
while current_room != "exit":

# Within the loop, complete the required behavior in small steps:
#   1. Display the current room.
    print(f"You are currently in: {current_room}")
#   2. Prompt for a movement command or "exit".
    command = input("Enter yout command: ").strip().lower()

#   3. Branch for a valid move, exit, or invalid input.
if command == "exit":
    current_room = "exit"
    print("\nThanks for playing the game. Hope you enjoyed it!")
    break


elif command.startswith("go "):
    direction = command.replace("go ", "")

    if direction not in ["north", "south", "east", "west"]:
        print("Invalid direction. Try north, south, east, or west. \n")
        continue
    if direction in rooms[current_room]:

#   4. Update the room only after a valid movement command.
        next_room = rooms[current_room][direction]
        current_room = next_room
        print(f" You move to the {current_room}.\n")
    else:
        print("you can't go that way.\n")

else:
    print("Invalid command. Try: go north/south/east/west or exit

#   5. Continue until the required exit condition is reached.

# TODO: Run and de'"bug all milestone cases in prototype/README.md.
if___name == "main
