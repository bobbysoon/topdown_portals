from sfml import Vector2

def _SegSegIntersect( s1p1,s1p2 , s2p1,s2p2 ):
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

def SegSegIntersect(p1,p2,p3,p4):
	x1,y1 = p1;x2,y2 = p2
	x3,y3 = p3;x4,y4 = p4
	dx21 = x2-x1 ; dy21 = y2-y1
	dx43 = x4-x3 ; dy43 = y4-y3

	d = dx21*dy43 - dy21*dx43
	if d:
		dx13 , dy13 = x1-x3 , y1-y3
		r = ( dy13*dx43 - dx13*dy43) / d
		s = ( dy13*dx21 - dx13*dy21) / d
		if r >= 0 and r <= 1 and s >= 0 and s <= 1:
			return Vector2( dx21 , dy21 )*r+p1
