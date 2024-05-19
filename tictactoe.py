board = ["-", "-", "-",
         "-","-", "-",
         "-","-","-"]
currentPlayer = "X"
winner = None
gameRunning = True
startmessage = str(input(" WELCOME TO TIC TAC TOE! | Insert any keys to start the game: "))

# for syntech tech recruitment by nur aleeya khalisya

# printing the game board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("==========")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("==========")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input

def playerInput(board):
    inp =input("Enter a number from 1 to 9: ")
    if(inp.isdigit()):
      userInput = int(inp)
      print('Number entered')
      if (userInput >= 1 and userInput <= 9):
        print('Valid Number Entered')
        # print(board[inp-1])
        if (board[userInput-1] == '-'):
          board[userInput-1] = currentPlayer
        else:
          print('A player is already chosen a spot')
      else:
        print('Invalid number entered')
    else:
      print('Invalid input. Please enter a number between 1 and 9')

# check for win or tie

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkRow(board): 
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiagonal(board): 
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    

def checkTie(board):
    if "-" not in board:
        print("TIE!")
        play_again = input("Game has ended. Enter any keys to restart: ")
        tic_tac_toe()
        
def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"{winner} has won the game! Congratulations!")
        play_again = input("Game has ended. Enter any keys to restart: ")
        tic_tac_toe()
    
# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def tic_tac_toe():
    board[0] = "-"
    board[1] = "-"
    board[2] = "-"
    board[3] = "-"
    board[4] = "-"
    board[5] = "-"
    board[6] = "-"
    board[7] = "-"
    board[8] = "-"
    currentPlayer = "X"


# restart

while gameRunning:
    startmessage
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()