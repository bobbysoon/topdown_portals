import sfml as sf

from LMBLineTool import LMBLineTool
from MMBPanner import MMBPanner
from WheelZoom import WheelZoom

from PanThroughPortals import PanThroughPortals

class Window_WASD:
	wasd=sf.Vector2(0,0)

	def KeyUp_A(self, e):
		if self.wasd.x<0: self.wasd.x=0
	def KeyUp_D(self, e):
		if self.wasd.x>0: self.wasd.x=0
	def KeyDown_A(self, e):
		self.wasd.x=-self.tDelta*self.window.view.size.y/2
	def KeyDown_D(self, e):
		self.wasd.x= self.tDelta*self.window.view.size.y/2

	def KeyUp_W(self, e):
		if self.wasd.y<0: self.wasd.y=0
	def KeyUp_S(self, e):
		if self.wasd.y>0: self.wasd.y=0
	def KeyDown_W(self, e):
		self.wasd.y=-self.tDelta*self.window.view.size.y/2
	def KeyDown_S(self, e):
		self.wasd.y= self.tDelta*self.window.view.size.y/2



from math import *
class Window_Events(LMBLineTool,MMBPanner,WheelZoom,Window_WASD , PanThroughPortals):
	def EventHandler(self):
		w=self.window

		c1=sf.Vector2(*tuple(w.view.center)) # render a copy

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

		dx,dy=self.wasd
		if dx or dy:
			a=atan2(dx,dy)-radians(w.view.rotation)
			dx,dy=sf.Vector2(sin(a),cos(a))*sqrt(dx*dx+dy*dy)
			w.view.move(dx,dy)

		c2=w.view.center
		self.PassViewThroughPortal(c1,c2)

	eventsIgnored='FocusEvent TextEvent ResizeEvent MouseEvent MouseMoveEvent'.split(' ')

	def CloseEvent(self, e): self.window.close()
	def KeyDown_ESCAPE(self, e): self.window.close()

	def Button2_Down(self, e):
		self.mousePos= e.position
		self.MouseMoveEvent= self.MMBPanner_MouseMoveEvent
	def Button2_Up(self, e):		
		delattr(self,'MouseMoveEvent')

	def Button0_Down(self, e):
		self.LMBLineTool_Button0_Down(e)
	def Button0_Up(self, e):		
		delattr(self,'MouseMoveEvent')
		self.LMBLineTool_Button0_Up(e)

