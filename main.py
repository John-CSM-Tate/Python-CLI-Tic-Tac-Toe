WIN_LINES = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
game_board = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
}

def finish(grid):
    for l in WIN_LINES:
        a, b, c = l
        if (grid[a] == grid[b] == grid[c]):
            print(f"The winner is {grid[a]}")
            return True
    return False

def printGrid(grid):
    print(f"{grid[0]} | {grid[1]} | {grid[2]}")
    print("---------")
    print(f"{grid[3]} | {grid[4]} | {grid[5]}")
    print("---------")
    print(f"{grid[6]} | {grid[7]} | {grid[8]}")

# ask user for a cell
# check cell is empty
# change players
# check answer
is_playing = True
turn = "X"
turn_number = 0
printGrid(game_board)
while is_playing:    
    print(f"It is {turn}'s turn.")
    player_input = int(input("please enter cell wanted: "))
    if (player_input < 0) and (player_input > 8):
        print("Please enter a number that is beaing displayed")
    elif game_board[player_input] != str(player_input):
        print("that postion has already been selected")
    else:
        game_board[player_input] = turn
        turn_number += 1
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    # Checks end game conditions
    if finish(game_board):
        is_playing = False
    elif turn_number > 8:
        print("Draw")
        is_playing = False
    
    printGrid(game_board)