import pygame, sys, time, os
from pygame.locals import *

class displayObject(object):
	def __init__(self, _gameObj):
			#screen initialization
			self.screen = pygame.display.set_mode((720, 720))
			pygame.display.set_caption('checkers, yo')

			#background initialization
			self.background = pygame.Surface(self.screen.get_size()).convert()

			#game object
			self.gameObject = _gameObj

			self.initializeDisplay()



	def initializeDisplay(self):
		#load the board .bmp
		#blit the background to the screen
		self.screen.blit(pygame.image.load('resources/board.bmp'), (0, 0))
		pygame.display.flip()

		time.sleep(2)
		
		
	#def updateDisplay(self):
