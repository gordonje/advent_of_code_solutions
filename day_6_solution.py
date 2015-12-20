import re

# grid for the first problem
grid_1 = [[False for x in range(1000)] for x in range(1000)]

# grid for the second problem
grid_2 = [[0 for x in range(1000)] for x in range(1000)]


# pattern for parsing the instructions into key, value pairs
instruct_pattern = re.compile(r'^(?P<act>\w+(?:\s\w+)?)\s(?P<x1>\d+),(?P<y1>\d+)\sthrough\s(?P<x2>\d+),(?P<y2>\d+)$')

with open('day_6_input.txt', 'r') as f:
	for line in f.readlines():

		string = line.strip()

		# parse the line into instruction components
		instruct = re.match(instruct_pattern, string).groupdict()

		# convert appropriate instruct values to ints
		for k, v in instruct.iteritems():
			try:
				instruct[k] = int(v)
			except ValueError:
				pass

		# fixing x range upper limit
		instruct['x2'] += 1
		# fixing y range upper limit 
		instruct['y2'] += 1

		# for each row within the x range
		for row in range(instruct['x1'], instruct['x2']):
			# for each number in the y range
			for col in range(instruct['y1'], instruct['y2']):
				# use num as the index position within the row
				if instruct['act'] == 'turn on':
					grid_1[row][col] = True
					grid_2[row][col] += 1
				elif instruct['act'] == 'turn off':
					grid_1[row][col] = False
					# min brightness is 0, otherwise leave it
					if grid_2[row][col] > 0:
						grid_2[row][col] -= 1
				elif instruct['act'] == 'toggle':
					grid_1[row][col] = not grid_1[row][col]
					grid_2[row][col] += 2
					
total_lit = 0
total_brightness = 0

# for each row, add the count of on lights to the total lit
for row in grid_1:
	total_lit += row.count(True)

print 'There are {} lights turned on.'.format(total_lit)

# for each row, add the count of on lights to the total lit
for row in grid_2:
	print row
	total_brightness += sum(row)

print 'There the brightness level is {}.'.format(total_brightness)