import pygame, sys, time, os
'''
https://upload.wikimedia.org/wikipedia/commons/f/fd/Draughts_Notation.svg



Blue is top, red is bottom

0: empty square
1: red piece
2: red king
3: blue piece
4: blue king
'''

class Square(object):
	def __init__(self):
		#0: empty square || 1: red piece || 2: red king || 3: blue piece || 4: blue king
		self.Value = 0
		#neighbors, starting at top left and moving clockwise
		#0: top left || 1: top right || 2: bottom left || 3: bottom right
		self.Neighbors = [None for x in range(4)]

class gameBoard(object):
	"""Member boardArray is the main array, and this object has functions to manipulate it."""
	def __init__(self):
		#super(gameBoard, self).__init__()
		
		#creates an array of size 32 populated by Square objects
		self.boardArray = [Square() for x in range(32)]
		self.initializeBoard()

	#populates each Square's neighbors array
	def generateNeighbors(self, index):
		#left column
		if (index in (5, 13, 21, 29)):
			self.boardArray[index].Neighbors[1] = index - 4
			if (index != 29):
				self.boardArray[index].Neighbors[2] = index + 4
		#right column
		elif (index in (4, 12, 20, 28)):
			self.boardArray[index].Neighbors[3] = index + 4
			if (index != 4):
				self.boardArray[index].Neighbors[0] = index - 4
		#middle upper aligned columns
		elif (index in (1, 9, 17, 25, 2, 19, 18, 26, 3, 11, 19, 27)):
			self.boardArray[index].Neighbors[2] = index + 5
			self.boardArray[index].Neighbors[3] = index + 4
			#if not in top row
			if (index > 3):
				self.boardArray[index].Neighbors[0] = index - 4
				self.boardArray[index].Neighbors[1] = index - 3
		#middle bottom aligned columns
		elif (index in (6, 14, 22, 30, 7, 15, 23, 31, 8, 16, 24, 32)):
			self.boardArray[index].Neighbors[0] = index - 5
			self.boardArray[index].Neighbors[1] = index - 4
			#if not in bottom row
			if (index < 30):
				self.boardArray[index].Neighbors[2] = index + 4
				self.boardArray[index].Neighbors[3] = index + 3





	
	#populates boardArray
	def initializeBoard(self):
		#self.generateNeighbors()
		#for each row

		for y in range(32):
			if (y <= 12):
				#top 3 rows have blue pieces
				self.boardArray[y].Value = 3
			elif (y >= 21):
				#bottom 3 rows have red
				self.boardArray[y].Value = 1
			self.generateNeighbors(y)

			#if right aligned


	