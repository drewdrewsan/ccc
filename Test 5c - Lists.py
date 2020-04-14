n = int(input())
A = []
counter = 1
new = []

for i in range(1, n+1):
    if i % 2 != 0:
        A.append(i)
print(A)

while True:
    if A[counter] > len(A):
        break
    for i in range(1, len(A)+1):
        if i % A[counter] != 0:
            new.append(A[i-1])
    print(new)
    print(counter)
    counter += 1
    A = new
    new = []







"""
while True:
    for i in range(0, len(A)+1):
       if i == len(A)+1:
           if i % int(A[counter]) != 0:
               new.append(A[i])
               counter += 1
               A = new
               print(A)
           else:
               counter +=1
               A = new
       elif i % int(A[counter]) != 0:
           new.append(A[i])
           print(A)


print(A)
"""
