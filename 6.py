smallest = float("inf")
biggest = float("-inf")
for num in input:
	num = int(num)
	smallest = num if num < smallest else smallest
	biggest = num if num > biggest else biggest
print(smallest - biggest)