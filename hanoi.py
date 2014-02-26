import re
class HanoiGame(object):
	"""Hanoi Game object."""
	def __init__(self):
		"""Initalization. Creates the variables."""
		self.towers = [[], [], []]
		self.validtower = []

	def buildgame(self, towersize):
		"""Builds the game with the specified tower size."""
		self.maxsize = towersize
		self.towers = [range(towersize,0,-1), [], []]
		self.validtower = range(towersize,0,-1)
		
	def drawstuff(self):
		"""Draws the current towers."""
		for i in range(self.maxsize-1, -1, -1):
			for j in range(0, 3):
				if i > (len(self.towers[j])-1):
					print "\t|\t", # print the blank spot
				else:
					print "\t%r\t" % self.towers[j][i], # print the value
				
			print " "
		return 1

	def isdone(self):
		"""Returns True if the initial tower has been moved to another peg."""
		return self.validtower in self.towers[1:]
	
	def validmove(self, towerone, towertwo):
		"""Returns True if moving from towerone to towertwo is valid."""
		if len(self.towers[towertwo]) == 0: #if destination is empty, yes
			return True
		if len(self.towers[towerone]) == 0: #if source empty, no
			return False
		if self.towers[towertwo][-1] > self.towers[towerone][-1]: #is the destination a greater value than the source
			return True
		return False #otherwise fail
	
	def move(self, towerone, towertwo):
		"""Moves the top block of towerone to towertwo."""
		# error check first
		if towerone == towertwo: # are the numbers the same
			print "Same tower."
			return 0
		if towerone > 2 or towerone < 0 or towertwo > 2 or towertwo < 0:
			print "Invalid tower. Use 1-3."
			return 0
		if self.validmove(towerone, towertwo): # is the destination tower a valid target for the move
			# do the move
			self.towers[towertwo].append(self.towers[towerone].pop())
			return 1
		else:
			print "Invalid move."
			return 0 # invalid move

		
thegame = HanoiGame()	
thegame.buildgame(5)
prompt = '> '
while thegame.isdone() == False:
	thegame.drawstuff()
	print "Tower to move from:"
	cont = raw_input(prompt);
	while not re.match('\d+$', cont): # some regex to catch non-numbers
		print "Input a number.";
		cont = raw_input(prompt);
	movefrom = int(cont);
	print "Tower to move to:"
	cont = raw_input(prompt);
	while not re.match('\d+$', cont): # some regex to catch non-numbers
		print "Input a number.";
		cont = raw_input(prompt);
	moveto = int(cont);
	thegame.move(movefrom-1, moveto-1) # move from tower x to y
# exit the game when done.
thegame.drawstuff()
print "Complete."