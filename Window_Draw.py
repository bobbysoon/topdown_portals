from SegSegTest import SegSegTest
from SFVert import SFVert
import sfml as sf
class Window_Draw:
	sfvCenter=SFVert( radius=16 , col=sf.Color(32,16,4) , point_count=8 )
	def Draw(self):
		self.window.clear()
		self.background.draw(self.window)

		for line in self.lines:
			self.window.draw(line)

		#for t in self.lineTransforms:
		#	t.Draw(self.window)

		#if SegSegTest.instance:
		#	SegSegTest.instance.Draw(self.window)

		self.sfvCenter.drawable.position=self.window.view.center
		self.window.draw(self.sfvCenter)

		self.window.display()

