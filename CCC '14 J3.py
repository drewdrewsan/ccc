n = int(input())
a = 100
d = 100
A = []
rando = ""

for i in range(n):
    rando = input()
    A = rando.split()
    if A[0] > A[1]:
        d = d - int(A[0])
    elif A[0] < A[1]:
        a = a - int(A[1])

print(a)
print(d)

