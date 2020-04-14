for i in range (1, 5001):
    sum1 = i
    for x in range(1, i//2 + 1):
        if i % x == 0:
            sum1 += x
    sum2 = sum1
    for y in range(1, sum1//2 + 1):
        if sum1 % y == 0:
            sum2 += y
    if sum2 / i == 2:
        print(i)
