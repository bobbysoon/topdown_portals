import sfml as sf
from PortalTransform import PortalTransform

class LMBLineTool:
	lines=[]
	lineTransforms=[]
	def UpdateShader(self):
		doPortal= 1 if len(self.lines)==2 else 0
		self.background.shader.set_parameter("doPortal", doPortal)
		if self.lines:
			l1p1,l1p2=self.lines[0][0].position,self.lines[0][1].position
			self.background.shader.set_parameter("l1p1", l1p1 )
			self.background.shader.set_parameter("l1p2", l1p2 )
			if doPortal:
				l2p1,l2p2=self.lines[1][0].position,self.lines[1][1].position
				self.background.shader.set_parameter("l2p1", l2p1 )
				self.background.shader.set_parameter("l2p2", l2p2 )
			self.lineTransforms= [PortalTransform(line) for line in self.lines]

	def LMBLineTool_Button0_Down(self, e):
		mousePos= self.window.map_pixel_to_coords(e.position)
		self.line= sf.VertexArray(sf.PrimitiveType.LINES,2)
		self.line[0].color= sf.Color(0,255,255);self.line[0].position=mousePos
		self.line[1].color= sf.Color(255,128,0);self.line[1].position=mousePos
		if len(self.lines)==2:self.lines.pop()
		self.lines.insert(0,self.line)
		self.UpdateShader()
		self.MouseMoveEvent= self.LMBLineTool_MouseMoveEvent

	def LMBLineTool_MouseMoveEvent(self, e):
		self.line[1].position=self.window.map_pixel_to_coords(e.position)
		self.UpdateShader()

	def LMBLineTool_Button0_Up(self, e):
		mousePos= self.window.map_pixel_to_coords(e.position)
		self.line[1].color= sf.Color(0,255,255);self.line[1].position=mousePos
		self.UpdateShader()

