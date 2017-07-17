A console game of Battleship (Python)

#python 2.7

# Importing from the random library
from random import randint

# - GAME BOARD

board = []

# -- A function that seeds the board with Os

def seed_board(board):
    for i in range (10):
        board.append(["O "]*10)

# -- It's not enough to define a function (you obviously have to call it)
seed_board(board)

# -- defining a function called "print_board", which we then can use like so : print_board(board) with board as an argument for instance

def print_board(board):

    print ("")
    i = -1
    while i < 8:
        # -- horizontal numbers
        #-- as long as i different from 9 just print the numbers in line ("",) but if it reaches 9 (9 + 1 = 10) then return a new line ("")
        print str(i+1) + " ",
        i += 1
    else:
        print str(i+1) + "  x" + ""
        print "-------------------------------"

    # -- horizontal numbers MISSING


    for i in board:
        # -- print i would have been enough but " ".join cleans up commas with spaces
        print " ".join(i)

# - NOW LET'S HIDE OUR BATTLESHIP IN A RANDOM LOCATION

# -- defining a function
def random_row(board):
    return randint(0, len(board)-1)
    # -- minus 1 because the index of len(gth) starts at 1, whereas board at 0
def random_col(board):
    return randint(0, len(board)-1)

# -- now we call each function on the board. Let's store coordinates for the ship in the variables ship_row and ship_col
ship_row = random_row(board)
ship_col = random_col(board)

print_board(board)
print ("")

# - ALLOW THE PLAYER TO GUESS WHERE IT IS

# -- Python doesn't have do while loops (which is something that became needed out of the flow of the development of the app),
# but there is a similar construct :
# -- while True:
# --    do_something()
# --    if condition()
# --        break

while True:

    # -- If a user enters a letter for instance, the console throws back an error ("invalid literal for int() with base 10: 'b')
    # -- If you add a measure for catching errors (try), it will in this case print the message we want but still throw back the error after.
    # -- Then I added the guess_row stuff again under the print message...
    user_inputs_numbers = False
    while user_inputs_numbers == False:
        try:
            guess_row = int(raw_input("Guess Row: "))
            guess_col = int(raw_input("Guess Column: "))
            print ""
            user_inputs_numbers = True
        except:
            print "Please enter numerical values only.\n"

# -- Now we've got our input, but we haven't done anything with it yet.

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations, you sank the battleship!\n"
        # -- requirement : a succesful hit is saved as -1 in the array
        board[guess_row][guess_col]="-1"

        print_board(board)

        print "Reseeding...\n"

        board = []
        seed_board(board)

    else:
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print "Coordinates should be of values 0 to 9."
            # -- to do : in the multiple ship version it should take into account "-1"
        elif board[guess_row][guess_col] == "-2":
            print "You guessed this already.\n"
        else:
            # -- unused feature
            # -- print "Try again. The ship was here: " + str(ship_col) + " [row], " + str(ship_row) + " [column]"
            # -- you have to specify str() because otherwise it will return that it can't concatenate str and int.
            # There are better ways like % interpolation but not sure it works in python2
            print "Try again."
            # -- requirement : a hit that landed in the water is saved as -2
            board[guess_row][guess_col]="-2"
            # -- unused feature
            # -- X is for where the ship actually was
            # -- board[ship_row][ship_col]="X "

            print_board(board)
            print ""

            # -- otherwise the game goes on
            continue_game = str(raw_input("Do you want to continue? (y / n): "))
            if continue_game == "n":
                break
            elif continue_game == "y":
                print ""
            else:
                print "\nType in 'y' followed by enter to quit, or 'n' to resume the game.\n"

            # -- a = [] is how you create a list, but it's also one way to clear a list.
            # -- This was another requirement (I thought): that the board be cleared.
            # Update : but in the one ship version, it could be used and should be used when the ship is found
            # -- board = []
            # -- seed_board(board)






# - SHIPS
# -- (I haven't done anything with that yet)

maxNumberOfShips = 10

# -- this creates a class with various properties
class ship(object):
    def __init__(self, ship_length, ship_name, sunk):
        self.shipLength = ship_length
        self.shipName = ship_name
        self.sunk = sunk

# -- this creates instances of ship
ships = {
    ship(2, "Uboot", False),
    ship(3, "Destroyer", False),
    ship(4, "Cruser", False),
    ship(5, "Battleship", False),
}

numberOfUboot = 4
numberOfDestroyer = 3
numberOfCruser = 2
numberOfBattleship = 1

# - COLORS
'''

colors = {
    "green":"\033[92m",
    "blue":"\033[94m",
    "red":"\033[91m",
    "reset":"\033[00m",
}

# Order matters! If you're going to use ressources, they need to be available before.
class bcolors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'

'''

