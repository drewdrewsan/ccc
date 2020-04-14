n = int(input())
numbers = []
smallest = 1000000001
c1 = 0
c2 = 1
c3 = 2

for i in range(n):
    d = int(input())
    numbers.append(d)

numbers.sort()

for i in range(n-1):
    if ((numbers[c2] - numbers[c1])/2) + ((numbers[c3] - numbers[c2])/2) < smallest:
        smallest = ((numbers[c2] - numbers[c1])/2) + ((numbers[c3] - numbers[c2])/2)
    c1 += 1
    c2 += 1
    c3 += 1
    if c3 >= len(numbers):
        break


print(abs(smallest))
