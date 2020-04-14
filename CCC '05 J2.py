a = int(input())
b = int(input())
A = []
div = []
counter = 0

for i in range(a, b+1):
    A.append(i)

for i in A:
    div = []
    for j in range(1, i):
        if i % j == 0:
            div.append(j)
    if len(div) == 3:
        counter += 1

print("The number of RSA numbers between {0} and {1} is {2}".format(a, b, counter))
