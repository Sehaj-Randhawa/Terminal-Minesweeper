import numpy as np
import map_setup
import player_guesses

# Checks the tiles above, below, to the left, and right along with diagonals for a bomb.

def count_bombs(map, fy: int, fx: int):
    count = 0
    for cy in range(-1, 2):
        for cx in range(-1, 2):
            try:
                if map[fy + cy, fx + cx] == 9 and fy + cy != -1 and fx + cx != -1:
                    count += 1
            except IndexError:
                pass
    return count

# Both of these force their functions to reload if no input is given.

def guess_col(length: int):
    while True:
        gu_l = player_guesses.guessing_l(length)
        if gu_l != None:
            return gu_l

def guess_row(height: int):
    while True:
        gu_h = player_guesses.guessing_h(height)
        if gu_h != None:
            return gu_h

def main():

    game_active = False

    print("Let's play minesweeper! Customize the board along with the number of mines you would like to play with.\nAll tiles that have [*] are unmined and tiles that have [-] means there are 0 bombs nearby.\nYour first guess will mine out a 3x3 area whilst avoiding any bombs.")

    minemap_length = map_setup.set_mm_length()

    minemap_height = map_setup.set_mm_height()

    minemap_mines = map_setup.set_mm_mines(minemap_length, minemap_height)

    print("Preview:")
    map_setup.print_map(np.full(( minemap_height, minemap_length), 0, dtype=int), minemap_height, minemap_length)
            
    guess_l = guess_col(minemap_length)
    guess_h = guess_row(minemap_height)

    mine_coordinates = map_setup.place_mm_mines(minemap_height, minemap_length, guess_h, guess_l)

    minemap = np.zeros((minemap_height, minemap_length), dtype=int)

    # Converts the tuples from the list into two seperate variables for the numpy array.

    for i in range(minemap_mines):
        mine_y, mine_x = mine_coordinates[i]
        minemap[mine_y, mine_x] = 9

    turngoal = (minemap_length * minemap_height) - minemap_mines

    player_map = np.full(( minemap_height, minemap_length), 10, dtype=int)

    # The 'minemap' array contains only 9s and 0s. 9s are bombs and 0s are empty spaces. This is the array that contains all bomb locations.
    # The 'player_map' array contains only 10s at the beginning of the game, these are unmined tiles. This is the array that the players see during the game.

    turn_count = 0

    # Repeat the 'count_bombs' function for tiles surrounding the initial guess.

    for my in range(-1, 2):
        for mx in range(-1, 2):
            try:
                if minemap[guess_h + my, guess_l + mx] == 0 and guess_h + my != -1 and guess_l + mx != -1:
                    player_map[guess_h + my, guess_l + mx] = count_bombs(minemap, guess_h + my, guess_l + mx)
                    turn_count += 1
            except IndexError:
                pass
            
    map_setup.print_map(player_map, minemap_height, minemap_length)

    game_active = True

    while game_active == True:
        guess_l = guess_col(minemap_length)
        guess_h = guess_row(minemap_height)
        if minemap[guess_h, guess_l] == 9:
            print("Game Over!")
            map_setup.print_map(minemap, minemap_height, minemap_length)
            return
        elif player_map[guess_h, guess_l] == 10:
            player_map[guess_h, guess_l] = count_bombs(minemap, guess_h, guess_l)
            turn_count +=1
        
        if turn_count == turngoal:
            print("You win!")
            map_setup.print_map(minemap, minemap_height, minemap_length)
            return
        map_setup.print_map(player_map, minemap_height, minemap_length)

main()