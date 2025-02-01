from random import shuffle

def set_mm_length():
    while True:
        mm_length = input('How long do you want the minemap to be? (Value must be above 3 and below 17) \n')
    
        try:

            mm_length = int(mm_length)

            if 4 <= mm_length <= 16:

                print(f"Minemap length set to {mm_length}.")

                return mm_length

            else:

                print("Try again. (Number not in range)")


        except ValueError:

            print("Try again. (Input must be an integer)")  

def set_mm_height():
    while True:
    
        mm_height = input('How tall do you want the minemap to be? (Value must be above 3 and below 17) \n')
    
        try:

            mm_height = int(mm_height)

            if 4 <= mm_height <= 16:

                print(f"Minemap length set to {mm_height}.")

                return mm_height

            else:

                print("Try again. (Number not in range)")


        except ValueError:

            print("Try again. (Input must be an integer)")

def set_mm_mines(l: int, h: int):
    while True:
    
        mm_mines = input('How many mines do you want to fill the map with? (Cannot be greater than/equal to the number of tiles on the map)\n')
        
        try:

            mm_mines = int(mm_mines)

            if 0 < mm_mines < (l * h):

                print(f"Mines set to {mm_mines}.")

                return mm_mines
            
            else:

                print("Try again. (Number doesn't fit correct range)")


        except ValueError:

            print("Try again. (Input must be an integer)")

def place_mm_mines(mh: int, ml: int, gh: int, gl: int):
    mine_placer = [
    (y, x) for y in range(mh) for x in range(ml)
    if (y, x) != (gh, gl)
    ]
    shuffle(mine_placer)
    return mine_placer

def print_map(map, h: int, l: int):
        for rows in range(0, h):
            for cols in range(0, l):
                if map[rows, cols] == 9:
                    print(f"[x]", end="")
                elif map[rows, cols] == 0:
                    print(f"[-]", end="")
                elif map[rows, cols] == 10:
                    print(f"[*]", end="")
                else:
                    print(f"[{map[rows, cols]}]", end="")
            print("")

