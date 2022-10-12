import pygame
import sys
import os
from settings import *
from game import *
from handTracking import HandTracking
import cv2


os.environ['SDL_VIDEO_WINDOWS_POS'] = "%d, %d" % (100, 32)

pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

mainClock = pygame.time.Clock()

fps_font = font = pygame.font.SysFont("coopbl", 22)

hand_tracking = HandTracking()


def user_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

def update():
	pygame.display.update()
	mainClock.tick(FPS)


while True:
	user_events()
	runEverything(SCREEN)
	cap = cv2.VideoCapture(4)
	_, frame = cap.read()
	print(type(frame))
	frame = hand_tracking.scan_hands(frame)
	cv2.imshow("Frame", frame)
	update()
	
	
	if DRAW_FPS:
		fps_label = fps_font.render(f"FPS: { int (mainClock.get_fps())}", 1, (255, 200, 20))
		SCREEN.blit(fps_label, (5, 5))
