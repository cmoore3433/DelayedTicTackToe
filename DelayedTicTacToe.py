import queue
import platform
import os

class DelayedTicTacToe:
  def __init__(self):
    self.movesQueue=queue.Queue(9)
    self.usedmovesQueue=queue.Queue(9)
    self.usedMovesList=[]
    self.board=[["-","-","-"],
                ["-","-","-"],
                ["-","-","-"]]
    self.winner=None
  
  def clearScreen(self):
    if platform.system()=="Windows":
      os.system('cls')
    else:
      os.system('clear')
    return

  def runGame(self):
    while self.winner is None:
      self.playerInput()
      self.processInput()
      self.printBoard()
      self.decideWinner()
      input("Press enter to continue to the next round.  Caution, you will not be able to see the board until the next round is over.")
    print("The winner is "+self.winner+"!")


  def playerInput(self):
    print("""Rules of the Game:
    1. This isn't your usual game of tictactoe.  Choices for where to put your X or O will all be made before any are displayed on the board.  Depending on if you choose to play by allowing the two players to see each other's inputs or not, this makes it into a game of memorization or luck, respectively.  Things can become harder if the game progresses past the first round as both players must remember the board while choosing their new input.
    2. Enter your input in the following format(x is the row number and y is the column number): (x,y)
    3. Player 1 is X while Player 2 is O.
    
    1|2|3
    -----
    2| | 
    -----
    3| | """)
    input("Press enter to continue.")
    self.clearScreen()
    while self.movesQueue.full()!=True:
      pInput=input("Player 1, choose a grid square: ").strip('()').split(',')
      for i in range(len(pInput)):
        pInput[i]=int(pInput[i])
      tuple(pInput)
      test=False
      while test==False:
        for i in pInput:
          if i>3 or i<=0 or len(pInput)!=2:
            pInput=input("Error: Choice out of range, choose a valid grid square(1-3): ").strip('()').split(',')
            for i in range(len(pInput)):
              pInput[i]=int(pInput[i])
            tuple(pInput)
            continue
        test=True
      test=False
      self.movesQueue.put(pInput)
      self.clearScreen()
      if self.movesQueue.full(): #Checking to see if Player 2 can make a move
        break
      pInput=input("Player 2, choose a grid square: ").strip('()').split(',')
      for i in range(len(pInput)):
        pInput[i]=int(pInput[i])
      tuple(pInput)
      test=False
      while test==False:
        for i in pInput:
          if i>3 or len(pInput)!=2:
            pInput=input("Error: Choice out of range, choose a valid grid square(1-3): ").strip('()').split(',')
            for i in range(len(pInput)):
              pInput[i]=int(pInput[i])
            tuple(pInput)
            continue
        test=True
      self.movesQueue.put(pInput)
      self.clearScreen()
    return

  def processInput(self):
    self.clearScreen()
    while self.movesQueue.empty()!=True:
      move=self.movesQueue.get()
      if move in self.usedMovesList:
        print("Move wasted! "+str(move)+" already on the board!")
      else:
        self.usedMovesList.append(move)
        self.board[move[0]-1][move[1]-1]="X"
      if self.movesQueue.empty(): #Checking to see if Player 2 can make a move
        break
      move=self.movesQueue.get()
      if move in self.usedMovesList:
        print("Move wasted! "+str(move)+" already on the board!")
      else:
        self.usedMovesList.append(move)
        self.board[move[0]-1][move[1]-1]="O"

  def printBoard(self):
    for i in game.board:
      print(i)

  def decideWinner(self):
    for i in self.board:
      if i[0]==i[1]==i[2]: #Horizontal victory
        self.winner=i[1]
        return
    
    if self.board[0][0]==self.board[1][1]==self.board[2][2]: #Diagonal victoy
      self.winner=self.board[1][1]
      return
    elif self.board[0][2]==self.board[1][1]==self.board[2][0]:
      self.winner=self.board[1][1]
      return

    for i in range(3): #Vertical victory
      if self.board[0][i]==self.board[1][i]==self.board[2][i]:
        self.winner=self.board[1][i]
        return
    if len(self.usedMovesList)==9:
      self.winner="nobody. The board is full"
    print("No winner this round!")

game=DelayedTicTacToe()
game.runGame()