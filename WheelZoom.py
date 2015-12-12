class WheelZoom:
	def MouseWheelEvent(self, e):
		z= 11./10. if e.delta<0 else 10./11. if e.delta>0 else 1.0
		p= self.window.map_pixel_to_coords(e.position)
		self.window.view.center= p+(self.window.view.center-p)*z
		self.window.view.zoom(z)

