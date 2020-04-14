n = int(input())
counter = 1

for i in range(n):
    boop = input()
    j = 0
    while j < len(boop):
        if j+counter >= len(boop):
            print("{0} {1} ".format(counter, boop[j]))
            j += counter
            counter = 1
        elif boop[j] == boop[j+counter]:
            counter += 1
        else:
            print("{0} {1} ".format(counter, boop[j]),end="")
            j += counter
            counter = 1


