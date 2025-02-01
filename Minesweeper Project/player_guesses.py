def guessing_l(length: int):

    gl = input(f"Which column do you want to mine? (Value must be an integer, and in range from 1 [Left side] to {length} [Right side])\n")

    try:

        gl = int(gl)
    
        if 1 > gl or gl > length:

            print("Value not in range.")

        else:

            print(f"Column guess set to {gl}")

            gl -= 1

            return gl

    except ValueError:

        print("Value must be an integer.")

def guessing_h(height: int):
    gh = input(f"Which row do you want to mine? (Value must be an integer, and in range from 1 [Top] to {height} [Bottom])\n")

    try:

        gh = int(gh)
    
        if 1 > gh or gh > height:

            print("Value not in range.")

        else:

            print(f"Row guess set to {gh}")

            gh -= 1

            return gh

    except ValueError:

        print("Value must be an integer.")
