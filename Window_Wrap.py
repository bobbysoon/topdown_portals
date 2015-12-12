class Window_Wrap:
	def getScale(self): return self.window.view.size.y
	def setScale(self, scale): self.window.view.size = float.__div__(*self.window.view.size)*scale,scale
	scale= property(getScale,setScale)

	def getCenter(self): return self.window.view.center
	def setCenter(self, c): self.window.view.center= c
	center= property(getCenter,setCenter)

	def getRotation(self): return self.window.view.rotation
	def setRotation(self, r): self.window.view.rotation= r
	rotation= property(getRotation,setRotation)

	def coord(self, pixel): return self.window.map_pixel_to_coords(pixel)
