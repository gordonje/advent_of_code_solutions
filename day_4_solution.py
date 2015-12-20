import hashlib
import re

num = 0

solution_1 = None

solution_2 = None

while solution_1 == None or solution_2 == None:

	my_input = 'ckczppom{}'.format(num)

	m = hashlib.md5()

	m.update(my_input)

	cur_hex = m.hexdigest()
	print cur_hex

	if solution_1 == None:
		if re.match(r'^0{5}.+$', cur_hex) != None:
			solution_1 = num
		else:
			num += 1
	if solution_2 == None:
		if re.match(r'^0{6}.+$', cur_hex) != None:
			solution_2 = num
		else:
			num += 1

print 'Solution 1 is {}'.format(solution_1)
print 'Solution 2 is {}'.format(solution_2)