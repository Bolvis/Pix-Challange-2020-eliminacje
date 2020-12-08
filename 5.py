for row in input:
    row = row.split("\t")
    num1 = int(row[0])
    num2 = int(row[1])
    is_divisible = row[0] + " is divisible by " + row[1] if num1 % num2 == 0 else row[0] + " is not divisible by " + \
                                                                                  row[1]
    print(is_divisible)
