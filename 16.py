for row in input:
	row = row.split("\t")
	row[1] = row[1].split(" ")
	word = ""
	for index in range(len(row[0])):
		word = word + row[0][index] if index != int(row[1][0]) else word + row[1][2]
	print(word)