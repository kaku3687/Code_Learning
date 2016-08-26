# dieview.py
from graphics import*
class DieView:
	""" DieView is a widget that displays a graphical representation
	of a standard six-sided die."""
	def __init__(self, win, center, size):
		"""Create a view of a die, e.g.:
		d1 = GDie(myWin, Point(40, 50), 20)
		creates a die centered at (40, 50) having sides
		of length 20."""
		self.win = win 			# save this for drawing points later
		self.background = "white" 	# color of die face
		self.foreground = "black"	# color of the points
		self.psize = 0.1 * size 	# radius of each point
		hsize = size / 2.0 		# half the size of the die
		offset = 0.6 * hsize 		# distance from center to outer points
		# create a square for the face
		cx, cy = center.getX(), center.getY()
		p1 = Point(cx-hsize, cy-hsize)
		p2 = Point(cx+hsize, cy+hsize)
		rect = Rectangle(p1, p2)
		rect.draw(win)
		rect.setFill(self.background)
		# create 7 circles for standard point locations
		self.pt1 = self.__makePt(cx-offset, cy-offset)
		self.pt2 = self.__makePt(cx-offset, cy)
		self.pt3 = self.__makePt(cx-offset, cy+offset)
		self.pt4 = self.__makePt(cx, cy)
		self.pt5 = self.__makePt(cx+offset, cy-offset)
		self.pt6 = self.__makePt(cx+offset, cy)
		self.pt7 = self.__makePt(cx+offset, cy+offset)
		# draw an initial value
		self.setValue(1)
	def __makePt(self, x, y):
		"Internal helper method to draw a point at (x, y)"
		point = Circle(Point(x, y), self.psize)
		point.setFill(self.background)
		point.setOutline(self.background)
		point.draw(self.win)
		return point
	def setValue(self, value):
		"Set this die to display value."
		# turn all points off
		self.pt1.setFill(self.background)
		self.pt2.setFill(self.background)
		self.pt3.setFill(self.background)
		self.pt4.setFill(self.background)
		self.pt5.setFill(self.background)
		self.pt6.setFill(self.background)
		self.pt7.setFill(self.background)
		# turn correct points on
		if value == 1:
			self.pt4.setFill(self.foreground)
		elif value == 2:
			self.pt1.setFill(self.foreground)
			self.pt7.setFill(self.foreground)
		elif value == 3:
			self.pt1.setFill(self.foreground)
			self.pt7.setFill(self.foreground)
			self.pt4.setFill(self.foreground)
		elif value == 4:
			self.pt1.setFill(self.foreground)
			self.pt7.setFill(self.foreground)
			self.pt5.setFill(self.foreground)
			self.pt3.setFill(self.foreground)
		elif value == 5:
			self.pt1.setFill(self.foreground)
			self.pt7.setFill(self.foreground)
			self.pt5.setFill(self.foreground)
			self.pt3.setFill(self.foreground)
			self.pt4.setFill(self.foreground)
		else:
			self.pt1.setFill(self.foreground)
			self.pt7.setFill(self.foreground)
			self.pt5.setFill(self.foreground)
			self.pt3.setFill(self.foreground)
			self.pt4.setFill(self.foreground)
			self.pt6.setFill(self.foreground)