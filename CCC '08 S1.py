coldcity = ""
coldtemp = 0

flag = True
while flag == True:
    city = input()
    A = city.split()
    if A[0] == "Waterloo":
        if int(A[1]) < int(coldtemp):
            coldtemp = A[1]
            coldcity = A[0]
        flag = False
    else:
         if int(A[1]) < int(coldtemp):
            coldtemp = A[1]
            coldcity = A[0]
        
print(coldcity)

