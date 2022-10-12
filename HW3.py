# separator	Main.py_0_false.txt
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()


try:  

# separator	Main.py_1_true.txt
    board = [[['-' for i in range(board_size)] for j in range(10)] for k in range(2)]
    dict_imp = {"Destroyer": 2, "Cruiser": 3, "Submarine": 3, "Battleship": 4, "Carrier": 5}
    #This dict matches ships with their length
    list_orientation = ["h", "v"]
    #I used this list in order to control orientation of entered input
    list_ships_copy = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    confirm_list = ["y", "n"]
    print_3d_list(board)
    player = 0
    while player < 2:
    # This while loop is used to complete placement phase of each player
        ship_placed = 0
        while ship_placed < 5:
        #This while loop is used to complete placemnt of each ship of each player
            print_ships_to_be_placed()
            print_single_element(' '.join(list_ships_copy))
            print_empty_line()
            print_player_turn_to_place(player + 1)
            print_to_place_ships()
            x = input()
            y = x.split()
            if len(y) < 4:
                print_incorrect_input_format()
                print_3d_list(board)
            #I checked if the input is long enough
                continue
            try:
                y[0] = y[0].capitalize()
                y[1] = int(y[1])
                y[2] = int(y[2])
                y[3] = y[3].lower()
                #I checked the correctness of elements of input format
            except:
                print_incorrect_input_format()
                print_3d_list(board)
                continue
            if y[1] < 1 or y[1] > 10 or y[2] > 10 or y[2] < 1:
                print_incorrect_coordinates()
                print_3d_list(board)
            #It is impossible that x and y is bigger than 10 or smaller than 1. I checked this condition by this if statemnet
                continue
            if y[0] not in dict_imp.keys():
                print_incorrect_ship_name()
                print_3d_list(board)
            #If the first element of entered input is not in dict.keys. It can be  said this ship does not exist.So this if statemen checked the name of ship
                continue
            if y[3] not in list_orientation:
                print_incorrect_orientation()
                print_3d_list(board)
                #This code block check orientation of entered input
                continue
            if y[0] not in list_ships_copy:
                print_ship_is_already_placed(y[0])
                print_3d_list(board)
                #This code block control if the entered input has already been placed or not
                continue
            if y[3] == "h" and y[1] + dict_imp[y[0]] > 11:
                print_ship_cannot_be_placed_outside(y[0])
                print_3d_list(board)
                #This code block check that the ship wanted to place can be placed for horizontal
                continue
            if y[3] == "v" and y[2] + dict_imp[y[0]] > 11:
                print_ship_cannot_be_placed_outside(y[0])
                print_3d_list(board)
                #This code block check that the ship wanted to place can be placed for vertical
                continue
            if y[3] == "h":
                flag = False
                for i in range(dict_imp[y[0]]):
                    if board[player][y[2] - 1][y[1] - 1 + i] == "#":
                        flag = True
                if flag == True:
                    print_ship_cannot_be_placed_occupied(y[0])
                    print_3d_list(board)
                    # I used the flag here because it needs to return to the beginning of the 2 nested loops in the occupied error
                    continue
                else:
                    for i in range(dict_imp[y[0]]):
                        board[player][y[2] - 1][y[1] - 1 + i] = "#"
                    print_3d_list(board)
                    ship_placed += 1
                    list_ships_copy.remove(y[0])
                #After controlled all possible bug, I printed ship entered here
            if y[3] == "v":
                flag = False
                for i in range(dict_imp[y[0]]):
                    if board[player][y[2] - 1 + i][y[1] - 1] == "#":
                        flag = True
                if flag == True:
                    print_ship_cannot_be_placed_occupied(y[0])
                    print_3d_list(board)
                #The same thing as horizontal
                    continue
                else:
                    for i in range(dict_imp[y[0]]):
                        board[player][y[2] - 1 + i][y[1] - 1] = "#"
                    print_3d_list(board)
                    ship_placed += 1
                    list_ships_copy.remove(y[0])
        while ship_placed == 5:
            print_confirm_placement()
            a = input()
            confirm_input = a.lower()
            if confirm_input not in confirm_list:
            #In order to confirm input is not y or n
                continue
            if confirm_input == "y":
                ship_placed = 0
                list_ships_copy = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                if player == 0:
                    a_board = board.copy()
                    #I copied the confirmed board because player 2 should not see the board player 1 has
                    board = [[['-' for i in range(board_size)] for j in range(10)] for k in range(2)]
                    #Refresh the board for Player 2 replacement
                    print_3d_list(board)
                if player == 1:
                    ship_placed = 6324234234
                    #In order to quit while loop
                    b_board = board.copy()
                    board = [[['-' for i in range(board_size)] for j in range(10)] for k in range(2)]
                player += 1
            if confirm_input == "n":
                ship_placed = 0
                list_ships_copy = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                board = [[['-' for i in range(board_size)] for j in range(10)] for k in range(2)]
                print_3d_list(board)
                #In order to restart placement phase of players
                continue
    a_hit = 0
    b_hit = 0
    player_hit = 0
    previous_hit = []
    previous_hit_b = []
    while player_hit < 2:
        if player_hit == 0:
            print_3d_list(a_board)
            print_player_turn_to_strike(player_hit + 1)
            print_choose_target_coordinates()
            target = input().split()
            try:
                target[0] = int(target[0])
                target[1] = int(target[1])
                #I check correctness of input  format
            except:
                print_incorrect_input_format()
                print(target)
                continue
            target[0] -= 1
            target[1] -= 1
            #I do this because the range of board starting from 0
            if target[1] < 0 or target[1] >= 10 or target[0] < 0 or target[0] >= 10:
                print_incorrect_coordinates()
                #Inputs would be inside of the board
                continue
            if target in previous_hit:
                print_tile_already_struck()
                #I add previous hits on previous_hit list and if input is in list code returns to input section.
                continue
            if b_board[1][target[1]][target[0]] == "#":
                print_hit()
                a_board[1][target[1]][target[0]] = "!"
                b_board[1][target[1]][target[0]] = "!"
                a_hit += 1
                previous_hit.append(target)
            #If input is correct, I place inputs on board
            if b_board[1][target[1]][target[0]] == "-":
                print_miss()
                a_board[1][target[1]][target[0]] = "O"
                b_board[1][target[1]][target[0]] = "O"
                print_type_done_to_yield(2)
                previous_hit.append(target)
                done_input = input().capitalize()
                while done_input != "Done":
                    print_type_done_to_yield(2)
                    done_input = input().capitalize()
                if done_input == "Done":
                    player_hit += 1
            if a_hit == 17:
            #Total lenght of the ships is 17 so 17 hit means the game is over
                print_3d_list(a_board)
                print_player_won(1)
                print_thanks_for_playing()
                break
        if player_hit == 1:
            print_3d_list(b_board)
            print_player_turn_to_strike(player_hit + 1)
            print_choose_target_coordinates()
            target_b = input().split()
        #I did the same thing as player=0
            try:
                target_b[0] = int(target_b[0])
                target_b[1] = int(target_b[1])
            except:
                print_incorrect_input_format()
                continue
            target_b[0] -= 1
            target_b[1] -= 1
            if target_b[1] < 0 or target_b[1] >= 10 or target_b[0] < 0 or target_b[0] >= 10:
                print_incorrect_coordinates()
                continue
            if target_b in previous_hit_b:
                print_tile_already_struck()
                continue
            if a_board[0][target_b[1]][target_b[0]] == "#":
                print_hit()
                b_board[0][target_b[1]][target_b[0]] = "!"
                a_board[0][target_b[1]][target_b[0]] = "!"
                previous_hit_b.append(target_b)
                b_hit += 1
            if a_board[0][target_b[1]][target_b[0]] == "-":
                print_miss()
                b_board[0][target_b[1]][target_b[0]] = "O"
                a_board[0][target_b[1]][target_b[0]] = "O"
                previous_hit_b.append(target_b)
                print_type_done_to_yield(1)
                done_input = input().capitalize()
                while done_input != "Done":
                    print_type_done_to_yield(1)
                    done_input = input().capitalize()
                if done_input == "Done":
                    player_hit -= 1
            if b_hit == 17:
                print_3d_list(b_board)
                print_player_won(2)
                print_thanks_for_playing()
                break


    
except:
    f.close()

