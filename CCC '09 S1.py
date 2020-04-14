minimum = int(input())
maximum = int(input())
cubes = []
squares = []
total = 0

for i in range(1, maximum+1):
    counter = i*i*i
    if counter <= maximum and counter >= minimum:
        cubes.append(i*i*i)
    elif counter > maximum:
        break

for i in range(1, maximum+1):
    counter = i*i
    if counter <= maximum and counter >= minimum:
        squares.append(i*i)
    elif counter > maximum:
        break

for i in cubes:
    if i in squares:
        total += 1

print(total)
    


