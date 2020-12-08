for row in input:
	sum = 1
	row = row.split("\t")
	for num in row:
		sum *= int(num)
	print(round(pow(sum,float(1)/float(len(row))),2))