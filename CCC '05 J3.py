A = []
turns = 0
rl = ""
name = ""
counter = 2

flag = True
while flag == True:
    n = input()
    A.append(n)
    if n == "SCHOOL":
        flag = False

for i in A:
    if i == "R" or i == "L":
        turns += 1

for i in range(turns):
    rl = ""
    name = ""
    if A[-counter] == "R":
        rl = "LEFT"
    elif A[-counter] == "L":
        rl = "RIGHT"
    if i == turns-1:
        print("Turn {0} into your HOME.".format(rl))
    else:
        name = A[-(counter+1)]
        print("Turn {0} onto {1} street.".format(rl, name))
        counter += 2
    
     
    
