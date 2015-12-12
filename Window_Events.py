import sfml as sf

from LMBLineTool import LMBLineTool
from MMBPanner import MMBPanner
from WheelZoom import WheelZoom

class Window_Events(LMBLineTool,MMBPanner,WheelZoom):
	def EventHandler(self):
		w=self.window
		for e in w.events:	#	Event Handler
			t=type(e).__name__
			if t=='KeyEvent':
				d= sf.Keyboard.__dict__
				k= d.keys()[d.values().index(e.code)]
				t='%s_%s'%('KeyDown' if e.pressed else 'KeyUp',k)
			elif t=='MouseButtonEvent':
				t='Button'+str(e.button)+('_Down' if e.pressed else '_Up')

			f= getattr(self,t,None)
			if f: f(e)
			elif not t in self.eventsIgnored: print t

	eventsIgnored='FocusEvent TextEvent ResizeEvent MouseEvent MouseMoveEvent'.split(' ')

	def CloseEvent(self, e): self.window.close()
	def KeyDown_ESCAPE(self, e): self.window.close()

	def Button2_Down(self, e):
		self.mousePos= e.position
		self.MouseMoveEvent= self.MMBPanner_MouseMoveEvent
	def Button2_Up(self, e):		
		delattr(self,'MouseMoveEvent')

	def Button0_Down(self, e):
		self.MouseMoveEvent= self.LMBLineTool_MouseMoveEvent
		self.LMBLineTool_Button0_Down(e)
	def Button0_Up(self, e):		
		delattr(self,'MouseMoveEvent')
		self.LMBLineTool_Button0_Up(e)

	def KeyDown_Q(self, e): self.window.view.rotate(-180.0*self.tDelta)
	def KeyDown_E(self, e): self.window.view.rotate( 180.0*self.tDelta)
