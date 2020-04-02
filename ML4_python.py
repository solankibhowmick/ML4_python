# set player to 1
player = 1

# set the initial state
state = 21  # number of objects
print("The number of objects is now ", state)
while True:
    # get valid move
    print("Player", player)
    while True:
        move = int(input("What is your move? "))
        if move in [1, 2, 3] and move < state:
            break
        print("Illegal move.")

    # update the state
    state = state-move

    # show the state
    print("The number of objects is now ", state)

    # check win status - win lose, stalemates
    if (state == 1):
        print("Player ", player, "wins!")
        break

    # switch players 2->1, 1->2 go back to the valid move line
    if (player == 1):
        player = 2
    else:
        player = 1
print("Game is Over.")
