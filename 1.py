for row in input:
	row = row.split("\t")
	seats = int(row[0]) * int(row[1])
	taken = int(row[2])
	free = seats - taken
	print(free)