import pyglet
from random import choice
#set up windows
window = pyglet.window.Window(width = 400, height= 450, caption="Game")

Im1 = pyglet.image.load('img/chicken.png')
Im2 = pyglet.image.load('img/butterfly.png')
Im3 = pyglet.image.load('img/ant.png')
Im4 = pyglet.image.load('img/bird.png')
Im5 = pyglet.image.load('img/peacock.png')
Im6 = pyglet.image.load('img/parrot.png')






def InitializeGrid(board):
	for i in range(8):
		for j in range(8):
			board[i][j] = choice(['A','B','C','D','E','F'])

def Initialize(board):
	InitializeGrid(board)
	global score
	score = 0 
	global turn
	turn = 0

def ContinueGame(current_score, goal_score = 100):
	if (current_score <= goal_score):
		return True
	else:
		return False 


def SwapPieces(board, move):
	temp = board[move[0]][move[1]]
	board[move[0]][move[1]] = board[move[2]][move[3]]
	board[move[2]][move[3]] = temp
	# board[move[0]][move[1]], board[move[2]][move[3]] = board[move[2]][move[3]], board[move[0]][move[1]]

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
				board[i][j] = choice(['A','B','C','D','E','F'])

def Update(board, move):
	SwapPieces(board, move)
	pieces_eliminated = True
	while pieces_eliminated:
		pieces_eliminated = RemovePieces(board)
		DropPieces(board)
		FillBlanks(board)
	







@window.event
def on_draw():
	window.clear()
	for i in range(7,-1,-1):
		#Draw each row
		y = 50+50*i
		for j in range(8):
			#draw each piece, first getting position
			x=50*j
			if board[i][j] ==  'A':
				Im1.blit(x,y)
			elif board[i][j] == 'B':
				Im2.blit(x,y)
			elif board[i][j] == 'C':
				Im3.blit(x,y)
			elif board[i][j] == 'D':
				Im4.blit(x,y)
			elif board[i][j] == 'E':
				Im5.blit(x,y)
			elif board[i][j] == 'F':
				Im6.blit(x,y)

	label = pyglet.text.Label('Turn: '+str(turn)+'  Score:'+str(score), font_name = "Arial", font_size=18, x=10, y=10)

	label.draw()

@window.event
def on_mouse_press(x,y, button, modifiers):
	global startx
	global starty
	startx = x
	starty = y

@window.event
def on_mouse_release(x,y, button, modifiers):
	startcol = startx//48
	startrow = (starty-48)//48
	endcol = x//48
	endrow = (y-48)//48

	# Check whether ending is adjacent to starting and if so, make move.


	if((startcol == endcol and startrow == endrow - 1) or (startcol == endcol and startrow == endrow+1)
		or (startrow == endrow and startcol==endcol-1) or (startrow == endrow and startcol == endcol+1)):
		
		if (endrow>7):
			endrow=0
			Update(board,[startrow, startcol, endrow, endcol])
		elif(endcol>7):
			endcol=0
			Update(board,[startrow, startcol, endrow, endcol])
		else:
			Update(board,[startrow, startcol, endrow, endcol])

			

		global turn
		turn +=1

		if not ContinueGame(score):
			print("You won in", turn, "turns!")
			
			


			

# score = 0
turn = 0
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
pyglet.app.run()