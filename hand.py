import pygame
import image
from settings import *
from hand_tracking import HandTracking
import cv2

class Hand:
	def __init(self):
		self.left_click = False
	
	def follow_mediapipe_hand(self, x, y):
		self.rect.center = (x, y)
		
