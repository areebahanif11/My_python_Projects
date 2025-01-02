import numpy as np
import random
from time import sleep

# creating an empty tic tac toe board
def empty_board():
  board = np.array([
      [0,0,0],
      [0,0,0],
      [0,0,0]
  ])
  return board
# check for empty places for a tic tac toe board
def empty_places(board):
  l = []
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == 0:
        l.append((i,j))
  return l

#select a random place for the player on board
def random_place(board,player):
  select = empty_places(board)
  current_location = random.choice(select)
  board[current_location] = player
  return board
#check the horizontal rows for a winner
def row_winner(board,player):
  for x in range(len(board)):
    win = True
    for y in range(len(board)):
      if board[x,y] != player:
        win = False
        break
    if win == True:
      return True
  return False
board = np.array([
      [0,0,1],
      [0,0,1],
      [0,0,1]
  ])
#check the vertical columns for a winner
def col_winner(board,player):
  for x in range(len(board)):
    win = True
    for y in range(len(board)):
      if board[y,x] != player:
        win = False
        continue
    if win == True:
      return True
  return False
#check the diagonal rows for a winne
def diag_left_winner(board,player):
  win = True
  y = 0
  for x in range(len(board)):
    if board[x,x] != player:
      win = False
  return win

def diag_right_winner(board,player):
  win = True
  for i in range(len(board)):
    y = len(board) - 1 - i
    if board[i,y] != player:
      win = False
      break
  return win

def evaluate_game(board):
  # winner[0=indecisive, 1=player1, 2=player2, -1=tie]
  winner = 0
  for player in [1,2]:
    if(row_winner(board,player) or col_winner(board,player) or diag_left_winner(board,player) or diag_right_winner(board, player)):
      return player
    
  if np.all(board != 0):
      return -1
    
  return 0

def player_move(board, player):
    # Prompt the player for input
    row = int(input("Enter the row (0, 1, or 2): "))
    col = int(input("Enter the column (0, 1, or 2): "))

    # Check if the input is within the valid range
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid input! Please enter a row and column between 0 and 2.")

    # Check if the selected spot is empty
    if board[row, col] != 0:
        print("This spot is already taken! Please choose another one.")
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

    # Place the player's marker on the board
    board[row, col] = player
    return board


# choose marker 
def choose_marker():
  player_marker = int(input("Choose your marker (1,2):  "))
  if player_marker not in [1,2]:
    print("Invalid choice. Please choose 1 or 2.")
  elif player_marker == 1:
    computer_marker = 2
  else:
    computer_marker = 1
  return player_marker, computer_marker


print("Welcome to TIC_TAC_TOE Game")
print('''        1. Computer vs. Computer
         2. Player vs. Computer''')
choice = int(input("Enter your choice:  "))

if choice == 1:
  print("Here two computers players playing together!")
  def tic_tac_toe():
    board = empty_board()
    winner = 0 
    counter = 1
    print(board)
    while winner == 0:
        for player in range(1,3):
            brd = random_place(board,player)
            print(f"Board after {counter} move")
            print(brd)
            sleep(1)
            counter += 1
            winner = evaluate_game(brd)

            if winner != 0:
                break
    return winner

  result = tic_tac_toe()
  if result == -1:
    print("The game is tie")
  else:
    print(f"The winner is player {result}")

elif choice == 2:
  print("You are playing against computer. Lets start!")
  def tic_tac_toe():
    board = empty_board()
    winner = 0 
    # counter = 1
    print(board)

    player_marker, computer_marker = choose_marker()

    while winner == 0:
        print("Your turn")
        board = player_move(board,player_marker)
        print(board)
        winner = evaluate_game(board)
        if winner!=0:
            break
        print("Computer turn")
        sleep(3)
        brd = random_place(board,computer_marker)
        print(brd)
        winner = evaluate_game(brd)
        if winner != 0:
            break
    return winner, player_marker,computer_marker

  result, human, computer = tic_tac_toe()
  if result == -1:
    print("The game is tie")
  elif result == human:
   print("Congratulations! You won.")
  else:
    print("The computer won. Better luck next time!")
else:
  print("Invalid choice. Enter 1,2, or 3")