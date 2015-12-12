import sfml as sf
from sys import argv,exit

from Background import Background

from Window_Events import Window_Events
from Window_Wrap import Window_Wrap
from Window_Run import Window_Run
from Window_Draw import Window_Draw


class Window(Window_Events,Window_Wrap,Window_Run,Window_Draw):
	def __init__(self):
		fullscreen=False
		FPS=15
		size=(800,600)
		antialiasing=0
		if fullscreen: size,bpp = sf.VideoMode.get_desktop_mode()
		self.window= sf.RenderWindow(
				mode=sf.VideoMode(*size,bpp=bpp) if fullscreen else sf.VideoMode(*size),
				style=sf.Style.FULLSCREEN if fullscreen else sf.Style.DEFAULT,
				title=argv[0],
				settings=sf.ContextSettings(antialiasing=antialiasing)
			)
		self.window.framerate_limit= FPS
		self.clock= sf.Clock()

		self.background=Background()

