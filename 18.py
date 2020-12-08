for row in input:
	row = row.split("\t")
	if int(row[1]) % 2 == 0 and row[2].find("a") != -1:
		print(row[0])