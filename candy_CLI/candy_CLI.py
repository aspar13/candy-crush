from random import choice

def InitializeGrid(board):
	for i in range(8):
		for j in range(8):
			board[i][j] = choice(['Q','R','S','T','U'])

def Initialize(board):
	InitializeGrid(board)
	global score
	score = 0 
	global turn
	turn = 1

def ContinueGame(current_score, goal_score = 100):
	if (current_score >= goal_score):
		return False
	else:
		return True 


def DrawBoard(board):
	line=""
	print("\n\n\n")
	print("------------------------------------")
	for i in range(7,-1,-1):
		line=""
		for j in range(8):
			line += ' | ' + board[i][j]
		line+= ' |'
		print(i+1,line)
	print("------------------------------------")
	print("     a   b   c   d   e   f   g   h")
	global score
	print("current_score: ", score)



def GetMove():
	move = input("Enter move: ")
	return move 

def ConvertLetterToCol(Col):
	if Col == 'a':
		return 0
	elif Col == 'b':
		return 1
	elif Col == 'c':
		return 2
	elif Col == 'd':
		return 3
	elif Col == 'e':
		return 4
	elif Col == 'f':
		return 5
	elif Col == 'g':
		return 6
	elif Col == 'h':
		return 7
	else:
		return -1
 

def SwapPieces(board, move):
	origrow = int(move[1])-1
	origcol = ConvertLetterToCol(move[0])
	if move[2] == 'u':
		newrow = origrow + 1
		newcol = origcol
	elif move[2] == 'd':
		newrow = origrow - 1
		newcol = origcol
	elif move[2] == 'l':
		newrow = origrow
		newcol = origcol-1 
	elif move[2] == 'r':
		newrow = origrow
		newcol = origcol + 1


	temp = board[origrow][origcol]
	board[origrow][origcol] = board[newrow][newcol]
	board[newrow][newcol] = temp

def RemovePieces(board):
	remove = [[0,0,0,0,0,0,0,0],
	  		 [0,0,0,0,0,0,0,0],
      		 [0,0,0,0,0,0,0,0],
	  		 [0,0,0,0,0,0,0,0],
	  		 [0,0,0,0,0,0,0,0],
	  		 [0,0,0,0,0,0,0,0],
	  		 [0,0,0,0,0,0,0,0],
	  		 [0,0,0,0,0,0,0,0]]

	for i in range(8):
		for j in range(6):
			if (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j+2]):
				remove[i][j] = 1
				remove[i][j+1] = 1
				remove[i][j+2] = 1 

	for j in range(8):
		for i in range(6):
			if (board[i][j] == board[i+1][j]) and (board[i][j] == board[i+2][j]):
				remove[i][j] = 1
				remove[i+1][j] = 1
				remove[i+2][j] = 1 

	global score
	removed_any = False
	for i in range(8):
		for j in range(8):
			if remove[i][j] == 1:
				board[i][j]=0
				score += 1
				removed_any = True
	return removed_any

def DropPieces(board):
	for j in range(8):
		listofpieces = []
		for i in range(8):
			if board[i][j] != 0:
				listofpieces.append(board[i][j])
		for i in range(len(listofpieces)):
			board[i][j] = listofpieces[i]
		for i in range(len(listofpieces),8):
			board[i][j] = 0 

def FillBlanks(board):
	for i in range(8):
		for j in range(8):
			if(board[i][j] == 0):
				board[i][j] = choice(['Q','R','S','T','U'])

def Update(board, move):
	SwapPieces(board, move)
	pieces_eliminated = True
	while pieces_eliminated:
		pieces_eliminated = RemovePieces(board)
		DropPieces(board)
		FillBlanks(board)
	

def DoRound(board):
	DrawBoard(board)
	move = GetMove()
	Update(board, move)
	global turn
	turn +=1

score = 100
turn = 100
goalscore = 100
board=[[0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0],
	  [0,0,0,0,0,0,0,0]]

Initialize(board)

while ContinueGame(score, goalscore):
	DoRound(board)

