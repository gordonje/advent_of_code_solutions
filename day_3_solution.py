
class Santa:
	def __init__(self):
		# starting position for each santa
		self.position = (0,0)

	def move(self, arrow):
		new_x = self.position[0]
		new_y = self.position[1]

		if arrow == '>':
			new_x += 1
		elif arrow == '<':
			new_x -= 1
		elif arrow == '^':
			new_y += 1
		elif arrow == 'v':
			new_y -= 1

		self.position = (new_x, new_y)

		return self.position

# to keep track of first year santa's coordinates
santa_year1 = Santa()

# to contain each house visited in the first year, starting with the first one which gets a present
houses_year1 = {santa_year1.position: 1}

# to keep track of second year real santa
santa_year2 = Santa()
# to keep track of second year robo-santa
robo_santa_year2 = Santa()

# to keep track of each house visited in the second year, starting with the first house gets to presents
houses_year2 = {santa_year2.position: 2} 

chars = None

with open('day_3_input.txt', 'rU') as f:
	chars = f.read()

counter = 0

for i in chars:

	# handle first year scenario
	new_pos1 = santa_year1.move(i)

	try:
		houses_year1[new_pos1] += 1
	except KeyError:
		houses_year1[new_pos1] = 1

	# handle second year scenario
	counter += 1
	# on even numbers, move robo-santa
	if counter % 2 == 0:
		new_pos2 = robo_santa_year2.move(i)
	# on odd numbers, move real santa
	else:
		new_pos2 = santa_year2.move(i)

	try:
		houses_year2[new_pos2] += 1
	except KeyError:
		houses_year2[new_pos2] = 1

print 'In the first year, {} houses were visited at least once.'.format(len(houses_year1))
print 'In the second year, {} houses were visited at least once.'.format(len(houses_year2))