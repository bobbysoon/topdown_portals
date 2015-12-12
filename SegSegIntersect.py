from sfml import Vector2
from sys import exit

def SegSegIntersect( s1p1,s1p2 , s2p1,s2p2 ):
	x21,y21 = s1p2-s1p1
	x43,y43 = s2p2-s2p1
	if x21 and x43:
		if y21/x21 != y43/x43 :
			d = x21*y43 - y21*x43
			if d:
				x13,y13 = s1p1-s2p1
				r = (y13*x43 - x13*y43) / d
				s = (y13*x21 - x13*y21) / d
				if r>=0. and r<=1. and s>=0. and s<=1. :
					x,y = s1p1[0]+x21*r , s1p1[1]+y21*r
					return Vector2(x21,y21)*r + s1p1
