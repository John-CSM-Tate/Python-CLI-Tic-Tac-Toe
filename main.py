import os

# All the possible winning lines
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

# Clear Termail
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Checks for winner
def finish(grid):
    for l in WIN_LINES:
        a, b, c = l
        if (grid[a] == grid[b] == grid[c]):
            print(f"The winner is {grid[a]}\n")
            return True
    return False

# Prints Grind
def printGrid(grid):
    print(f"{grid[0]} | {grid[1]} | {grid[2]}")
    print("---------")
    print(f"{grid[3]} | {grid[4]} | {grid[5]}")
    print("---------")
    print(f"{grid[6]} | {grid[7]} | {grid[8]}")

# Starting Values
is_playing = True
turn = "X"
turn_number = 0
clear()
printGrid(game_board)

# Game Loop
while is_playing:
    
    print(f"\nIt is {turn}'s turn.")
    player_input = int(input("Please enter the number in the cell you want: "))
    if (player_input < 0) and (player_input > 8): # Checks input is in range
        print("Please enter a number that is beaing displayed\n")
    elif game_board[player_input] != str(player_input): # Checks cell is not already taken
        print("That postion has already been selected\n")
    else: 
        game_board[player_input] = turn
        turn_number += 1
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    
    clear()
    # Checks end game conditions
    if finish(game_board):
        is_playing = False
    elif turn_number > 8:
        print("Draw\n")
        is_playing = False

    printGrid(game_board)