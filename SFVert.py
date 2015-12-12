import sfml as sf

class SFVert(sf.Drawable):
	def __init__(self, pos=(0,0) , rot=0 , radius=3 , col=sf.Color(128,255,128) , point_count=16 ):
		self.radius=radius
		sf.Drawable.__init__(self)
		self.drawable= sf.CircleShape()
		self.drawable.position= pos
		self.drawable.rotation= rot
		self.drawable.outline_color= col
		self.drawable.fill_color= sf.Color.TRANSPARENT
		self.drawable.point_count= point_count

	def draw(self,target,states):
		scale=target.view.size.y/target.size.y
		r=self.radius*scale
		self.drawable.radius= r
		self.drawable.origin= r,r
		self.drawable.outline_thickness= scale
		target.draw(self.drawable,states)

