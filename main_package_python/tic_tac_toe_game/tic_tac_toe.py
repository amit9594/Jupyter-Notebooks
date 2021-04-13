from IPython.display import clear_output

def display_board(board):
    
    # to clear prevoius outputs i.e if u ask to palyer to dispaly scrren have multiple history of outputs which is no use later so cear prevoius output
    clear_output()
    print(' | |')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' | |')
    print('------')
    print(' | |')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' | |')
    print('------')
    print(' | |')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' | |')
    
##############################################################################

def player_input():
    
    marker = ''  # here jose were take variable as marker instead of choice
    
   
    
    while marker not in ['X' , 'O']:     # u can write here as while choice!='X' and choice!='O'
        
        marker = input('player1 ,Please enter your choice from (X or O): ')
        
        if marker not in ['X',"O"]:
            
            print("sorry , please enter a valid marker : ")
        
    # end of while loop
    
    # assign choice to player1
    
    player1 = marker

    # assign player2 with opposite value of player1
    if marker == "X":            
        player2 = "O"
    else:
        player2 = "X"
        
        
    return (player1,player2)
    
##############################################################################

def place_marker(board ,marker , position):
    
    board[position] = marker
    
##############################################################################

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

##############################################################################

import random

def choose_first():
    
    flip =  random.randint(0,1)
    
    if flip == 0:
        return 'Player 1 goes first'
    else:
        return 'player 2 goes first'
    
##############################################################################

def space_check(board , position):
    
    return board[position] == ' '

##############################################################################

# this will jugde whether match is tie or not

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board , i):   # this means for every i means 0 t0 9 index we check is there any space by calling space_check function an is there that means board is not full so result will be false
            return False
    
    # For FUll we return True
    return True

##############################################################################

def player_choice(board):
    position = 'Wrong'   # give string as u want this is for initial value
    within_range = False # bydefulat ntitialize this with false and then check in if else condition for range us in within or not
    Acceptable_range = range(1,10)
    
    # Two condition to check here
    # within range or digit == false
    
    while position.isdigit() == False or within_range == False:          # bcoz of this if u enter other data types than integer it will aksed again to enter 
        
        position = input("Please choose next position from (1-9): ")
        
        # digit check
        
        
        if position.isdigit() == False:
            print("sorry that is not a digit : ")       # this if is under while and if false it comment like this for user
        
        
        # range check
        
        
        # here we check digit bhi hain aur within range bhi hain to within_range ko true karo otherwise false karo
        if position.isdigit() == True:
            if int(position) in Acceptable_range: 
                within_range = True
            else:
                print("sorry, you are out of acceptable range ")
                within_range = False
    
    return int(position)
    
##############################################################################

def replay():
    choice = ''
    while choice not in ['Yes' , 'No']:
        choice = input("play agian? please choose Yes or No : ")
    
    return choice == 'Yes'
    
##############################################################################

# Now on the game 

print('Welcome to Tic Tac Toe!')

# while loop to keep running the game

while True:
    #play the game
    
    ## Set the game up here (board , whose first , choose_marker X or O)
    
    the_board = [' ']*10                  # at start board will be empty
    
    player1_marker , player2_marker = player_input()  # at second step we have assign X and O to these variables
    
    turn = choose_first()      # we know this return player 1 or 2 so store in turn variable
    print(turn)
    
    
    # ask to players tready or not
    play_game = ''
    
    while play_game not in ['y', 'n']:
        
        play_game = input('Ready to play? y or n ?')
        
        if play_game == 'y':
            game_on = True
        else:
            game_on = False
            
    #play game

    while game_on:
        #Player 1 Turn
        
        if turn =='player 1':
            
            # show the board
            display_board(the_board)
            #choose position
            position = player_choice(the_board)
            # place the marker at that position
            place_marker(the_board,player1_marker,position)
            
            #check if they won
            # or check if there is a tie 
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player1 has won')
                game_on = False
            
            elif full_board_check(the_board):
                display_board(the_board)
                print('Tie game')
                game_on = False
            else:
                turn = 'player 2'
        
        # no won ? no turn? then next player turn
                
        # Player2's turn.
        
        # this else is exactly below of if turn =='player 1' that means now turn will be 'player 2'
        # its all similar as of player 1 so paste all if condtions in else also and change some needed condtions
        else:
             # show the board
            display_board(the_board)
            #choose position
            position = player_choice(the_board)
            # place the marker at that position
            place_marker(the_board,player2_marker,position)
            
            #check if they won
            # or check if there is a tie 
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player2 has won')
                game_on = False
            
            elif full_board_check(the_board):
                display_board(the_board)
                print('Tie game')
                game_on = False
            else:
                turn = 'player 1'
            
        
    if not replay():
        break
   # break out of the while loop on replay  