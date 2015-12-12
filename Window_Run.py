class Window_Run:
	def Run(self):
		self.setScale(.25)
		while self.window.is_open:
			self.tDelta= self.clock.restart().seconds
			self.EventHandler()
			self.Draw()

