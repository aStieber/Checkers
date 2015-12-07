import pygame, sys, time

class display(object):
	def __init__(self):
			self.screen = None
			self.background = None

			self.initializeDisplay()

	def initializeDisplay(self):
		self.screen = pygame.display.set_mode((720, 720))
		pygame.display.set_caption('checkers, yo')

		self.background = pygame.Surface(self.screen.get_size())
		RED = pygame.Surface((90, 90))

	
		pygame.draw.circle(RED, (0, 0, 255), (44, 44), 40)
		RED.set_colorkey((255, 255, 255))
		

		self.screen.blit(RED, (0,0))
		pygame.display.flip()
		pygame.image.save(RED, 'blue.bmp')
		time.sleep(3)


x = display()
x.initializeDisplay()

