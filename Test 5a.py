number = input()
A = []
for i in range(len(number)):
    A.append(number[i])
maximum = 0
start = 0
counter = 2

#numba = 0

for i in range(1, len(A)-1):
    if i > len(A)-1:
        break
    if A[i] == A[i+1]:
        for j in range(0, len(A) - 1):
            #print(numba)
            #numba +=1
            if i + counter > len(A)-1:
                if counter > maximum:
                    maximum = counter
                    start = i
                counter = 2
            elif A[i] == A[i + counter]:
                counter += 1
            else:
                if counter > maximum:
                    maximum = counter
                    start = i
                counter = 2

print("The start position is {0} and the length of the plateau is {1}".format(start, maximum))
                    
# 234567896666666666668
