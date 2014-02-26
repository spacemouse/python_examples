import re
class HanoiGame(object):
	"""Hanoi Game object."""
	def __init__(self):
		"""Initalization. Creates the variables."""
		self.towers = [[], [], []]
		self.valid_tower = []

	def build_game(self, tower_size):
		"""Builds the game with the specified tower size."""
		self.maxsize = tower_size
		self.towers = [range(tower_size,0,-1), [], []]
		self.valid_tower = range(tower_size,0,-1)
		
	def draw_stuff(self):
		"""Draws the current towers."""
		for i in range(self.maxsize-1, -1, -1):
			for j in range(0, 3):
				if i > (len(self.towers[j])-1):
					print "\t|\t", # print the blank spot
				else:
					print "\t%r\t" % self.towers[j][i], # print the value
				
			print " "
		return 1

	def is_done(self):
		"""Returns True if the initial tower has been moved to another peg."""
		return self.valid_tower in self.towers[1:]
	
	def valid_move(self, tower_one, tower_two):
		"""Returns True if moving from tower_one to tower_two is valid."""
		if len(self.towers[tower_two]) == 0: #if destination is empty, yes
			return True
		if len(self.towers[tower_one]) == 0: #if source empty, no
			return False
		if self.towers[tower_two][-1] > self.towers[tower_one][-1]: #is the destination a greater value than the source
			return True
		return False #otherwise fail
	
	def move(self, tower_one, tower_two):
		"""Moves the top block of tower_one to tower_two."""
		# error check first
		if tower_one == tower_two: # are the numbers the same
			print "Same tower."
			return 0
		if tower_one > 2 or tower_one < 0 or tower_two > 2 or tower_two < 0:
			print "Invalid tower. Use 1-3."
			return 0
		if self.valid_move(tower_one, tower_two): # is the destination tower a valid target for the move
			# do the move
			self.towers[tower_two].append(self.towers[tower_one].pop())
			return 1
		else:
			print "Invalid move."
			return 0 # invalid move

		
thegame = HanoiGame()	
thegame.build_game(5)
prompt = '> '
while thegame.is_done() == False:
	thegame.draw_stuff()
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
thegame.draw_stuff()
print "Complete."