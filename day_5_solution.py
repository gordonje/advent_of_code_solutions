
import re

def check_old_rules(string):

	result = False

	# can't contain these substrings
	if re.search(r'ab|cd|pq|xy', string) == None:

		# must contain at least three vowels
		num_vowels = re.findall(r'([aeiou]{1})', string)
		if len(num_vowels) >= 3:

			# must contain a letter repeated twice in a row
			if re.search(r'([a-z])\1', string) != None:

				result = True

	return result


def check_new_rules(string):

	result = False

	# Must contain at least one letter which repeats with exactly one letter between them, 
	# e.g., xyx, abcdefeghi (efe), or even aaa.
	if re.search(r'([a-z]).\1', string) != None:
		
		# Must contain a pair of any two letters that appear at least twice in the string 
		# without overlapping
		# e.g., xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

		if re.search(r'([a-z]{2})[a-z]*\1', string) != None:

			result = True

	return result

meets_old_rules = []
meets_new_rules = []

with open('day_5_input.txt', 'r') as f:
	for line in f.readlines():

		string = line.strip()

		if check_old_rules(string):
			meets_old_rules.append(string)

		if check_new_rules(string):
			meets_new_rules.append(string)

print 'According to the old rules, there are {} nice strings.'.format(len(meets_old_rules))
print 'According to the new rules, there are {} nice strings.'.format(len(meets_new_rules))


