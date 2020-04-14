n = ""
A = [ ]
a = 0
b = 0

flag = True
while flag == True:
    n = input()
    A = n.split()
    if A[0] == "7":
        flag = False
    elif A[0] == "1":
        if A[1] == "A":
            a = A[2]
        else:
            b = A[2]
    elif A[0] == "2":
        if A[1] == "A":
            print(a)
        else:
            print(b)

    
    elif A[0] == "3":
        if A[1] == "A" and A[2] == "B":
            a = int(a) + int(b)
        elif A[1] == "A" and A[2] == "A":
            a = int(a) + int(a)
        elif A[1] == "B" and A[2] == "A":
            b = int(b) + int(a)
        else:
            b = int(b) + int(b)
    elif A[0] == "4":
        if A[1] == "A" and A[2] == "B":
            a = int(a) * int(b)
        elif A[1] == "A" and A[2] == "A":
            a = int(a) * int(a)
        elif A[1] == "B" and A[2] == "A":
            b = int(b) * int(a)
        else:
            b = int(b) * int(b)
    elif A[0] == "5":
        if A[1] == "A" and A[2] == "B":
            a = int(a) - int(b)
        elif A[1] == "A" and A[2] == "A":
            a = int(a) - int(a)
        elif A[1] == "B" and A[2] == "A":
            b = int(b) - int(a)
        else:
            b = int(b) - int(b)
    elif A[0] == "6":
        if A[1] == "A" and A[2] == "B":
            a = int(a) // int(b)
        elif A[1] == "A" and A[2] == "A":
            a = int(a) // int(a)
        elif A[1] == "B" and A[2] == "A":
            b = int(b) // int(a)
        else:
            b = int(b) // int(b)

            
    
