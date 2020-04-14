a = ""
A = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
new = ""

flag = True
while flag == True:
    a = input()
    new = ""
    if a == "quit!":
        flag = False
    elif len(a) > 4 and a[-3] in A and a[-2] == "o" and a[-1] == "r":
        for i in range(len(a)):
            new += a[i]
            if a[i] == "o" and a[i+1] == "r":
                new += "u"
        print(new)
    else:
        print(a)
            
