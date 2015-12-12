import sfml as sf

from Quad import *

class Background(sf.Drawable):
	def __init__(self):
		sf.Drawable.__init__(self)
		self.quad=		Quad()
		self.shader=	sf.Shader.from_file(fragment='portal.frag')
		self.states=	sf.RenderStates(shader=self.shader)

	def draw(self, target,states=None):
		self.quad.align(target)
		target.draw(self.quad,self.states)
		self.shader.set_parameter("iResolution", target.view.size )
		self.shader.set_parameter("view_center", target.view.center )

	def corners(self):
		return self.quad.corners()

