import sfml as sf

from SegSegIntersect import SegSegIntersect
from SFLine import SFLine
from SFVert import SFVert

class SegSegTest(sf.Drawable): # as in debug
	instance=None
	def __init__(self, s1p1,s1p2 , s2p1,s2p2 ):
		SegSegTest.instance=self

		self.intersectPoint = SegSegIntersect( s1p1,s1p2 , s2p1,s2p2 )

		if self.intersectPoint:
			s1c1,s1c2,s2c1,s2c2=sf.Color(0,0,255),sf.Color(255,0,0),sf.Color(255,255,0),sf.Color(255,0,255)
		else:
			s1c1,s1c2,s2c1,s2c2=sf.Color(0,0,128),sf.Color(128,0,0),sf.Color(128,128,0),sf.Color(128,0,128)
		self.sfSeg1,self.sfSeg2 = SFLine(s1p1,s1p2,s1c1,s1c2),SFLine(s2p1,s2p2,s2c1,s2c2)

		self.intersect= SFVert( self.intersectPoint , col=sf.Color.GREEN ) if self.intersectPoint else None

	def __repr__(self): return self.intersectPoint
	def __str__(self): return str(self.intersectPoint)

	def Draw(self, window):
		window.draw(self.sfSeg1)
		window.draw(self.sfSeg2)
		if self.intersect:
			window.draw(self.intersect)

