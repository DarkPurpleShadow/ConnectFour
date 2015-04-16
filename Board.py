#!/usr/bin/python3.4

import urwid

GRAPHIC0 = "|_|_|_|_|_|_|_|"
GRAPHIC1 = "| | | | | | | |"
GRAPHIC2 = "| | | | | | | |"
GRAPHIC3 = "| | | | | | | |"
GRAPHIC4 = "| | | | | | | |"
GRAPHIC5 = "| | | | | | | |"
GRAPHIC6 = "               "
FILLGRAPH = "               "

NUM_COLS = 14

class Board(urwid.Widget):
	
	def __init__(self):
		self._selectable = True
		self.basic_graphic = urwid.TextCanvas([bytes("asdf", 'utf-8')])
		self.basic_graphic = urwid.TextCanvas([b"asdf"])
		self.coords = [0,0]
		#(col, row)
	
	def rows(self, size, focus=False):
		#return (size/2)
		return 15
		
	#Returns: None if key was handled by this widget or key (the same value passed) if key was not handled by this widget
	#TODO: Force redrawing
	def keypress(self, size, key):
		if key == 'right':
			if self.coords[0] < 6:
				self.coords[0] += 1
				#self.render
			#print self.coords[0]
			return None
		elif key == 'left':
			if self.coords[0] > 0:
				self.coords[0] -= 1
			#print self.coords[0]
			return None
		else:
			return key
		
	def render(self, size, focus=False):
		self.size_left_margin = int((size[0] - NUM_COLS) / 2)
		self.size_right_margin = int(((size[0] - NUM_COLS) / 2) - ((size[0]-1) % 2))
		self.left_margin = " " * self.size_left_margin
		self.right_margin = " " * self.size_right_margin
		
		#TODO: Add game stones/content in skeleton
		self.graphic6 = GRAPHIC6
		self.graphic6 = self.graphic6[:1+self.coords[0]*2] + 'v' + self.graphic6[2+self.coords[0]*2:]
		# v Does not work :(
		#self.graphic6[1+self.coords[0]*2] = 'v'
		
		self.text = [
			self.left_margin + self.graphic6 + self.right_margin,
			self.left_margin + GRAPHIC1 + self.right_margin,
			self.left_margin + GRAPHIC2 + self.right_margin,
			self.left_margin + GRAPHIC3 + self.right_margin,
			self.left_margin + GRAPHIC4 + self.right_margin,
			self.left_margin + GRAPHIC5 + self.right_margin,
			self.left_margin + GRAPHIC0 + self.right_margin
		]

		for i in range(0, 8):
			self.text.append(self.left_margin + FILLGRAPH + self.right_margin)
		#print size[1]
		
		return urwid.TextCanvas([repr('asdf')], self.text)
		#return self.basic_graphic
	
	def get_cursor_coords(self, size):
		#Return the cursor coordinates (col, row) of a cursor that will appear as part of the canvas rendered by this widget when in focus, or None if no cursor is displayed.
		return tuple(self.coords)
	
	def move_cursor_to_coords(self, size, col, row):
		#Parameters:
		#	size (widget size) - See Widget.render() for details.
		#	col (int) - new column for the cursor, 0 is the left edge of this widget
		#	row (int) - new row for the cursor, 0 it the top row of this widget
		if col == 0:
			return False
		else:
			return False

