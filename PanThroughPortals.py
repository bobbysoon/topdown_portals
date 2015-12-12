import sfml as sf

from math import *
from SegSegTest import SegSegTest

def Dot(u,v):	return (u.x*v.x + u.y*v.y)
def Norm(v):	return sqrt(v.x*v.x + v.y*v.y)     # norm = length of vector

#	VecSegDist(): get the distance of a point to a segment
def VecSegDist( p, s1,s2):
	v = s2-s1
	w = p - s1

	c1 = Dot(w,v)
	if ( c1 <= 0 ):		return Norm( p-s1 )

	c2 = Dot(v,v)
	if ( c2 <= c1 ):	return Norm( p-s2 )

	b = c1 / c2
	Pb = s1 + v*b
	return Norm( p-Pb )


def passingInto( m1,m2 , p1,p2 ):
	s1= copysign(1,(p2[0] - p1[0]) * (m1[1] - p1[1]) - (p2[1] - p1[1]) * (m1[0] - p1[0]))
	s2= copysign(1,(p2[0] - p1[0]) * (m2[1] - p1[1]) - (p2[1] - p1[1]) * (m2[0] - p1[0]))
	return s1==-1 and s2==1

class PanThroughPortals:
	def PassViewThroughPortal(self, c1,c2): # previous view center, current view center
		if len(self.lines)==2: # doPortal
			l1p1,l1p2 = self.lines[0][0].position,self.lines[0][1].position
			l2p1,l2p2 = self.lines[1][0].position,self.lines[1][1].position
			lt1,lt2 = self.lineTransforms
			for p1,p2,p3,p4,t1,t2 in [(l1p1,l1p2 , l2p1,l2p2 , lt1,lt2),(l2p1,l2p2 , l1p1,l1p2 , lt2,lt1)]:
				if passingInto(c1,c2,p1,p2):
					# path has crossed over a portal's line
					ip= SegSegTest(c1,c2,p1,p2).intersectPoint
					if not ip:
						pixelSize= 2.0 * self.window.view.size.y/self.window.size.y
						d1,d2=VecSegDist( c1, l1p1,l1p2),VecSegDist( c2, l1p1,l1p2)
						if d1<pixelSize or d2<pixelSize: ip=c1

					if ip:
						self.ApplyPortalTransformToCurrentViw(ip,p1,p2,p3,p4,t1,t2)
					else:
						print d1,d2,'\t',pixelSize

	def ApplyPortalTransformToCurrentViw(self, ip, p1,p2,p3,p4,t1,t2 ):
		d21,d43=p2-p1,p4-p3
		scale=d21/d43
		c=self.window.view.center
		rotation= t2.rotation - t1.rotation
		self.window.view.rotation+= rotation+180

		l21,l43=length(d21),length(d43)
		print ip,p1
		li1=length(ip-p1)
		ip2= p4 - d43 * li1/l21

		cip=c-ip
		cip2=ip2-SinCos(rotation+angle(cip))*length(cip)*scale
		self.window.view.center= cip2

		self.window.view.zoom(length(d43)/length(d21))




def SinCos(a):
	a=radians(a)
	return sf.Vector2(sin(a),cos(a))
def angle(v):
	return degrees(atan2(*v))

def length(v):
	dx,dy=v
	return sqrt(dx*dx+dy*dy)

