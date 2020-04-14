y = int(input())
A = []

flag = True
while flag == True:
    A = []
    y += 1
    for i in str(y):
        A += i
    if len(A) == 5:
        if A[0] != A[1] and A[0] != A[2] and A[0] != A[3] and A[0] != A[4] and A[1] != A[2] and A[1] != A[3] and A[1] != A[4] and A[2] != A[3] and A[2] != A[4] and A[3] != A[4]:
            flag = False
    if len(A) == 4:
        if A[0] != A[1] and A[0] != A[2] and A[0] != A[3] and A[1] != A[2] and A[1] != A[3] and A[2] != A[3]: 
            flag = False
    if len(A) == 3:
        if A[0] != A[1] and A[0] != A[2] and A[1] != A[2]:
            flag = False
    if len(A) == 2:
        if A[0] != A[1]:
            flag = False
    if len(A) == 1:
        flag = False
print(y)
