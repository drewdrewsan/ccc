n = int(input())
y = ""

for i in range(n):
    y = input()
    A = y.split()
    print(A[1]*int(A[0]))
