def reset(grid):
    for key, value in grid:
        grid[key] = " "

def finish(grid):
    lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
    for l in lines:
        a, b, c = l
        if (grid[a] == grid[b] == grid[c]) and (grid[a] != " "):
            return grid[a]

def printGrid():
    print("  1   2   3")
    print(f"1 {grid[0]} | {grid[1]} | {grid[2]}")
    print("  ---------")
    print(f"2 {grid[3]} | {grid[4]} | {grid[5]}")
    print("---------")
    print(f"3 {grid[6]} | {grid[7]} | {grid[8]}")


grid = {
    0: " ",
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
}




# loop
# ask user for a cell
# check cell is empty
# change players
# check answer
is_playing = True
while is_playing:
    printGrid()
    is_playing = False



    if finish(grid):
       is_playing = False 
print(finish(grid))