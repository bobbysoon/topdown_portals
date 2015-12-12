from PanThroughPortals import PanThroughPortals
import sfml as sf
from math import *

class MMBPanner(PanThroughPortals):
	def coord(self, p):
		return self.window.map_pixel_to_coords(p)

	def MMBPanner_MouseMoveEvent(self, e):
		mousePos= e.position
		s= self.window.view.size.y / self.window.size.y
		ox,oy= self.mousePos
		x,y= mousePos
		dx,dy= sf.Vector2((ox-x) , (oy-y))*s
		a= radians(self.window.view.rotation)+atan2(dy,dx)
		dx,dy=sf.Vector2(cos(a),sin(a))*sqrt(dx*dx+dy*dy)

		c1=tuple(self.window.view.center)
		self.window.view.move( dx,dy )
		c2=self.window.view.center

		self.PassViewThroughPortal(c1,c2)

		self.mousePos= mousePos

