n = int(input())
k = int(input())

s = n
for i in range(1,k+1):
    s += n * (10**i)

print(s)
