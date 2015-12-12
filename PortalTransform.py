import sfml as sf
import Box2D as b2
from math import *

class PortalTransform(sf.Transform):
	def __init__(self, line):
		sf.Transform.__init__(self)
		p1,p2 = line[0].position,line[1].position
		dx,dy = p2-p1
		length= sqrt(dx*dx+dy*dy)
		self.translate( p1 )
		self.rotation=degrees(atan2(-dx,dy))
		self.rotate( self.rotation )
		self.scale((length,length))

		self.drawable= sf.VertexArray(sf.PrimitiveType.TRIANGLES_FAN,4)
		self.drawable[0].color= sf.Color(32,64,128,64) ;	self.drawable[0].position= 0,1
		self.drawable[1].color= sf.Color(128,64,32,32) ;	self.drawable[1].position= .5,.0
		self.drawable[2].color= sf.Color(64,128,32,32) ;	self.drawable[2].position= .25,.0
		self.drawable[3].color= sf.Color(64,64,64,16) ;	self.drawable[3].position= 0,-1

	def Draw(self,window):
		window.draw(self.drawable,sf.RenderStates(transform=self))

