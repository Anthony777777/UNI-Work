grid = {
      9: " ",
      8: " ",
      7: " ",
      6: " ",
      5: " ",
      4: " ",
      3: " ",
      2: " ",
      1: " "
}
boardseperator = '-------------'
boardseperatorvertical = '|'
def inputboard():
      print(
            "|", "7", "|", "8", "|", "9", "|",
            "\n", "-------------",
            "\n", "|", "4", "|", "5", "|", "6", "|",
            "\n", "-------------",
            "\n", "|", "3", "|", "2", "|", "1", "|",
      )
print("hello and welcome to tic tac toe. human vs computer the grid below represents your input functions")
inputboard()
print("To play you will choose either first (x) or second (o) then enter the corresponding number for your move")
player1=""
player2=""
turncount = 0
if input("would you like to be player 1? (y/n): ") == "y":
      player1 = "Human"
      player2 = "CPU"
else:
      player1 = "CPU"
      player2 = "Human"
turncount = 0
def board():
      print("\n",boardseperatorvertical,grid[7],boardseperatorvertical,grid[8],boardseperatorvertical,grid[9],boardseperatorvertical,
      "\n",boardseperator,
      "\n",boardseperatorvertical,grid[4],boardseperatorvertical,grid[5],boardseperatorvertical,grid[6],boardseperatorvertical,
      "\n",boardseperator,
      "\n",boardseperatorvertical,grid[3],boardseperatorvertical,grid[2],boardseperatorvertical,grid[1],boardseperatorvertical)
def move_entry():
      move = int(input("Please enter a number where you would like to place your mark "))
      if move in grid and grid.get(move) == " ":
            global turncount
            if turncount % 2 == 0:
                  grid[move] = "x"
                  turncount+=1
            else:
                  grid[move] = "y"
                  turncount+=1
      else:
            print("invalid entry please enter a number corresponding to a blank space")
            # recalls itself to loop unit criteria satisfied
            move_entry()

import random
def opponent():
      choice = random.randrange(0,9)
      if choice in grid and grid.get(choice) == " ":
            global turncount
            if turncount % 2 == 0:
                  grid[choice] = "x"
                  turncount+=1
            else:
                  grid[choice] = "y"
                  turncount+=1
      else:
            opponent()

winner = "no"
while winner == "no" or turncount <=8:
      if player1 == "Human" and turncount % 2 == 0:
            print("Humans turn")
            board()
            move_entry()
            board()
            opponent()
            print(turncount)
      else:
            print("CPU Turn")
            board()
            opponent()
            board()
            move_entry()
            print(turncount)
      if grid[1] == "x" and grid[2] == "x" and grid[3] == "x" or\
      grid[4] == "x" and grid[5] == "x" and grid [6] == "x" or\
      grid[7] == "x" and grid [8] =="x" and grid[9] == "x" or\
      grid[1] =="x" and grid [4]== "x" and grid[7] == "x" or\
      grid[2] == "x" and grid[5] == "x" and grid[8] == "x" or\
      grid[3] =="x" and grid[6] == "x" and grid[9]=="x"or\
      grid[3] =="x" and grid[5] =="x" and grid[9] == "x" or\
      grid[7] == "x" and grid[5] == "x" and grid[2] == "x":
            winner = "yes"
            print("winner player 1")
            break
      elif grid[1] == "y" and grid[2] == "y" and grid[3] == "y" or\
      grid[4] == "y" and grid[5] == "y" and grid [6] == "y" or\
      grid[7] == "y" and grid [8] =="y" and grid[9] == "y" or\
      grid[1] =="y" and grid [4]== "y" and grid[7] == "y" or\
      grid[2] == "y" and grid[5] == "y" and grid[8] == "y" or\
      grid[3] =="y" and grid[6] == "y" and grid[9]=="y"or\
      grid[3] =="y" and grid[5] =="y" and grid[9] == "y" or\
      grid[7] == "y" and grid[5] == "y" and grid[2] == "y":
            winner = "yes"
            print("winner player 2")
      else:
            print("the game continues")
if winner == "yes" and player1 == "Human":
            print("congratulations human on winning")
            board()
elif winner == "yes" and player1 == "CPU":
      print("you lose")
      board()
else:
      print("the game is over")
      board()

      test