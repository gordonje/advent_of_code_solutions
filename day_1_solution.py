
chars = None

floor = 0

with open('day_1_input.txt', 'rU') as f:
	chars = f.read()

pos = 0

for i in chars:

	pos += 1

	if i == '(':
		floor += 1
		# print '  Going to {}'.format(floor)
	elif i == ')':
		floor -= 1
		# print '  Going to {}'.format(floor)

	if floor == -1:
		print pos

print 'Finished on {}'.format(floor)