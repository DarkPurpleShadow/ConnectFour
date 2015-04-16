#!/usr/bin/python3.4

import urwid
from Board import Board

def start_game(button):
	connectFour.gameName.set_text("Game Started")

def exit_game(button):
	raise urwid.ExitMainLoop()


class ConnectFour(object):
	def __init__(self):
		self.gameName = urwid.Text(('banner', u" Connect Four "), align='center')
		self.startGameButton = urwid.Button(u'Start Game')
		self.exitButton = urwid.Button(u'Exit')
		self.gameBoard = Board()
		
		urwid.connect_signal(self.startGameButton, 'click', start_game)
		urwid.connect_signal(self.exitButton, 'click', exit_game)
		
		#self.menu_content = urwid.Frame(header = self.gameName, body = urwid.Pile([self.gameName, self.startGameButton]))
		self.menu_content = urwid.Pile([self.gameName, self.gameBoard, self.startGameButton, self.exitButton])
		self.menu = urwid.Filler(body = self.menu_content, valign = 'top')



if __name__ == '__main__':
	connectFour = ConnectFour()
	loop = urwid.MainLoop(connectFour.menu, palette=[('reversed', 'standout', '')])
	loop.run()

#class MainMenu(urwid.Pile):
#	def __init__(self):
#		super(Pile, self).__init__("")