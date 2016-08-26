# objrball.py -- Simulation of a racquet ball game.
#				Illustrates design with objects.

from random import random

class Player:
	# A Player keeps track of service probability and score
	
	def __init__(self, prob):
		# Create a player with this probability
		self.prob = prob
		self.score = 0
		
	def winsServe(self):
		# RETURNS a Boolean that is true with probability self.prob
		return random() <= self.prob
		
	def incScore(self):
		# Add a point to this player's score
		self.score = self.score + 1
		
	def getScore(self):
		# RETURNS this player's current score
		return self.score
		
class RBallGame:
	# A RBallGame represents a game in progress.  A game has two players
	# and keeps track of which one is currently serving.
	
	def __init__(self, probA, probB):
		# Create a new game having players with the given probs.
		self.playerA = Player(probA)
		self.playerB = Player(probB)
		self.server = self.playerA	# Player A always serves first
		
	def play(self):
		# Play the game to completion
		while not self.isOver():
			if self.server.winsServe():
				self.server.incScore()
			else:
				self.changeServer()
				
	def isOver(self):
		# RETURNS game is finished (i.e. one of the players has won).
		a,b = self.getScores()
		return a == 15 or b == 15 or \
				(a == 7 and b == 0) or (b == 7 and a == 0)
				
	