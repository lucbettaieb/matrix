#!/usr/bin/python3

# Luc Bettaieb

import time
import board
import neopixel

class Matrix:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.pixels = neopixel.NeoPixel(board.D18, width*height)
		self.lut = [[0 for x in range(width)] for y in range(height)]
		i = 0
		for y in range(0, height):
			r = width - 1
			for x in range(0, width):
				if (y % 2 != 0):
					self.lut[y][x] = i + r
					r = r - 2
					i = i + 1
				else:
					self.lut[y][x] = i
					i = i + 1

		for y in range(0, height):
			print(self.lut[y])

	def set(self, x, y, rgb):
		self.pixels[self.lut[x][y]] = rgb

strip = Matrix(32, 8)

ON = (255, 255, 255)
OFF = (0, 0, 0)

for x in range(0, 32):
	for y in range(0, 8):
		if (x == y):
			strip.set(x, y, ON)
			time.sleep(0.1)
			strip.set(x, y, OFF)




#x.set(1, 1, (255, 255, 255))
#time.sleep(1)
#x.set(1, 1, (0, 0, 0))

exit()

naptime = 0.001
pixels = neopixel.NeoPixel(board.D18, 32*8)

while True:
	for i in range(0, 255):
		print(i)
		time.sleep(naptime)
		pixels.fill((i,i,i))

	for i in range(0, 255):
		print(255-i)
		time.sleep(naptime)
		pixels.fill((255-i,255-i,255-i))



