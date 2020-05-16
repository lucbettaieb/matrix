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

		self.ON = (40, 40, 40)
		self.OFF = (0, 0, 0)

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

	def clear(self):
		self.pixels.fill(self.OFF)

	def set(self, x, y, rgb):
		if (x >= self.width):
			return
		if (y >= self.height):
			return
		self.pixels[self.lut[y][x]] = rgb

	def set_high(self, x, y):
		self.set(x, y, self.ON)

	def set_low(self, x, y):
		self.set(x, y, self.OFF)

#strip = Matrix(32, 8)

#for x in range(0, 32):
#	for y in range(0, 8):
#		if (x == y):
#			strip.set_high(x, y)
#			time.sleep(0.1)
#			strip.set_low(x, y)
#



