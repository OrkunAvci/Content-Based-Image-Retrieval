import numpy as np
import cv2 as cv

def get_rgb(img):
	shape = np.shape(img)
	size = shape[0] * shape[1]
	rgb = [0, 0, 0]
	for row in img:
		for cell in row:
			for color in range(3):
				rgb[color] = rgb[color] + (cell[color]/255)
	rgb = [color/size for color in rgb]
	return rgb

def get_hsv(img):
	shape = np.shape(img)
	size = shape[0] * shape[1]
	hsv = [0, 0, 0]
	img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
	for row in img:
		for cell in row:
			for color in range(3):
				hsv[color] = hsv[color] + (cell[color] / 255)
	hsv = [color / size for color in hsv]
	return hsv