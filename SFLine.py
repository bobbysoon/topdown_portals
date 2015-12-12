import sfml as sf

def SFLine(p1,p2, c1=sf.Color.RED,c2=sf.Color.BLUE):
		drawable= sf.VertexArray(sf.PrimitiveType.LINES,2)
		drawable[0].position= p1 ; drawable[0].color=c1
		drawable[1].position= p2 ; drawable[0].color=c2
		return drawable

