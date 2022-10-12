import pygame
from settings import *
from handTracking import HandTracking


class Player:
	def __init__(self):
		self.rect = pygame.Rect(32, 32, 16, 16)
	
	def move(self, dx, dy):
		if dx != 0:
			self.move_single_axis(dx, 0)
		if dy != 0:
			self.move_single_axis(0, dy)
	def move_single_axis(self, dx, dy):
		self.rect.x += dx
		self.rect.y += dy
		
		for wall in walls:
			if self.rect.colliderect(wall.rect):
				if dx > 0:
					self.rect.right = wall.rect.left
				if dx < 0:
					self.rect.left = wall.rect.right
				if dy > 0:
					self.rect.bottom = wall.rect.top
				if dy < 0:
					self.rect.top = wall.rect.bottom



class Wall(object):
	def __init__(self, pos):
		walls.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 20, 20)

class drawSquare():
	def __init__(self, pos):
		self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
	
	def move_finger(self, dx, dy):
		self.rect.x += dx
		self.rect.y += dy
		

walls = []
player = Player()
handTracking = HandTracking()
drawSquare = drawSquare((x1, y1))

level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                              W",
    "W         WWWWWW                                               W",
    "W   WWWW       W                                               W",
    "W   W        WWWW                                              W",
    "W WWW  WWWW                                                    W",
    "W   W     W W                                                  W",
    "W   W     W   WWW W                                            W",
    "W   WWW WWW   W W                                              W",
    "W     W   W   W W                                              W",
    "WWW   W   WWWWW W                                              W",
    "W W      WW                                                    W",
    "W W   WWWW   WWW                                               W",
    "W     W    E   W                                               W",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

#Parse the level string above, W = wall, E = exit
x = y = 0
for row in level:
	for col in row:
		if col == "W":
			Wall((x, y))
		if col == "E":
			end_rect = pygame.Rect(x, y, 16, 16)
		x += 20
	y += 20
	x = 0


def runEverything(screen):
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		player.move(-2, 0)
	if key[pygame.K_RIGHT]:
		player.move(2, 0)
	if key[pygame.K_UP]:
		player.move(0, -2)
	if key[pygame.K_DOWN]:
		player.move(0, 2)
	
	if player.rect.colliderect(end_rect):
		pygame.quit()
		sys.exit()
	(x1, y1) = handTracking.get_index_point()

	drawSquare.move_finger((x1, y1))
	
	screen.fill((0, 0, 0))
	for wall in walls:
		pygame.draw.rect(screen, (255, 255, 255), wall.rect)
	pygame.draw.rect(screen, (255, 0, 0), end_rect)
	pygame.draw.rect(screen, (255 ,200, 0), player.rect)

