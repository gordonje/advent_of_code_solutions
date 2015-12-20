
paper_needed = 0
ribbon_needed = 0

with open('day_2_input.txt', 'r') as f:
	for line in f.readlines():
		dims = []

		for num in line.strip().split('x'):
			dims.append(int(num))
		
		total_area = 2 * dims[0] * dims[1] + 2 * dims[1] * dims[2] + 2 * dims[0] * dims[2]

		small_side_area = sorted(dims)[0] * sorted(dims)[1]

		print '  Gift total area = {}.'.format(total_area)
		print '  Gift small side area = {}.'.format(small_side_area)
		print '  Gift needs {} ft of wrapping paper.'.format(total_area + small_side_area)

		paper_needed += total_area + small_side_area
		
		print '-----------'

		small_side_perimeter = sorted(dims)[0] + sorted(dims)[0] + sorted(dims)[1] + sorted(dims)[1]
		volume = dims[0] * dims[1] * dims[2]

		print '  Gift small side perimeter = {}.'.format(small_side_perimeter)
		print '  Gift volume = {}.'.format(volume)
		print '  Gift needs {} ft of ribbon.'.format(small_side_perimeter + volume)

		ribbon_needed += small_side_perimeter + volume

		print '==========='


print 'Total wrapping paper needed is {} sq ft.'.format(paper_needed)
print 'Total needed needed is {} ft.'.format(ribbon_needed)