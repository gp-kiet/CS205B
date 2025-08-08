import numpy
#My initial Setup of the Game
board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']]) # Board is 3x3
p1s='X' # Symbol for Player 1
p2s='O' # Symbol for Player 2
def place(symbol): # 3. or 7. Place the symbol on the board
    print(numpy.matrix(board)) # 3.1 print the board
    while(1): # 3.2 Take input until the inputs are correct
        row = int(input('Enter row - 1 or 2 or 3: ')) # 3.3 Take row input
        col = int(input('Enter Column - 1 or 2 or 3: ')) # 3.4 Take col input

        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-': # 3.5 row and col must lie between 0 to 3 and the board should be empty
            break # 3.6 if everything is correct then break the loop
        else: # 3.7 Otherwise ask user to input again 
            print("Invalid Input please enter again...") 
    board[row-1][col-1]=symbol # 3.8 if row and cols are correct then placethe symbol at the desired palce
    print(numpy.matrix(board)) # 3.9 print the board with the placed symbol

def check_rows(symbol):# 4.1a Check the symbol is in three consecutive rows or not
    for r in range(3): # 4.1a.1 Check all three rows, start from 0 until row 2
        count=0 # 4.1a.2 set counter to 0, to test whether it is a winning move
        for c in range(3): # 4.1a.3 Iterate through all the cols (0..2)
            if board[r][c] == symbol: # 4.1a.4 if the symbol on the board is the one that is supplied by user then
                count=count+1 # 4.1a.5 increase the counter
        if count==3: # 4.1a.6 If the counter is 3 then it means it is a winning move by the player with the symbol
            print(symbol, ' won') # 4.1a.7 Place the symbol X won or O won
            return True # 4.1a.8 Return True if the player has won
    return False # 4.1a.9 Return Flase in all the other cases

def check_cols(symbol): # 4.1b Check the symbol is in three consecutive cols or not. The logic is same first we start with col 0 and all rows
    for c in range(3): # 4.1b.1 Check the symbol is in three consecutive cols or not
            count=0 # 4.1b.2 set counter to 0, to test whether it is a winning move
            for r in range(3): # 4.1b.3 Iterate through all the rows (0..2)
                if board[r][c] == symbol: # 4.1b.4 if the symbol on the board is the one that is supplied by user then
                    count=count+1 # 4.1b.5 increase the counter
            if count==3: # 4.1b.6 If the counter is 3 then it means it is a winning move by the player with the symbol
                print(symbol, ' won') # 4.1b.7 Place the symbol X won or O won
                return True # 4.1b.8 Return True if the player has won
    return False # 4.1b.9 Return Flase in all the other cases

def check_diagonals(symbol):  # 4.1c Check the symbol is in three diagonal places
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol: # 4.1c.1 First winning diagonal move 
        print(symbol, " won") # 4.1c.2 Place the symbol X won or O won
        return True # 4.1c.3 Return True if the player has won
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]==symbol: # 4.1c.4 Second winning digonal move
        print(symbol, " won")  # 4.1c.5 Place the symbol X won or O won
        return True # 4.1c.6 Return True if the player has won
    return False # 4.1c.7 Return Flase in all the other cases

def won(symbol): # 4 or 8. check the winning move 
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol) # 4.1 Winning move can be either three consecutive rows or cols or any diagonal
    #these functions return True in case it is a winning move otherwise False

def play():
    for turn in range(9): # 1. Number of total turns as the size of board is 3x3
        if turn%2==0:  # 2. All even chances 0,2,4 are of X's and odd chances 1,3,5 are of O's 
            print('X Trun') # 2.1 Print it is an X's Turn
            place(p1s) # 3. Place the X's symbol on the board
            if won(p1s): # 4. After placing the symbol check whether this move is winning move or not
                break   # 5. If X's move is winning then come of the the game
            else: # 6. Else check if it is O's turn
                print('O Trun') # 6.1 Print is is an O's Turn
                place(p2s) # 7. Place the O's symbol on the  board
                if won(p2s): # 8. After placing the symbol check whether this move is winning move or not
                    break  # 9. If O's move is winning then come of the the game
    if not(won(p1s)) and not(won(p2s)): # 10. if there is no move that it is a winning move
        print('Draw') # 11. then it is a draw

if __name__ == "__main__":
    play()