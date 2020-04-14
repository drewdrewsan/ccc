length = int(input())
numbers = []
total = 0

for i in range(length):
    new = int(input())
    if new == 0:
        numbers.pop(-1)
    else:
        numbers.append(new)

for i in range(len(numbers)):
    total += numbers[i]

print(total)
