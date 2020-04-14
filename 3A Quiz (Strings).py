s = input()

for i in range(len(s)):
    if s[i] == "1" or s[i] == "2" or s[i] == "3" or s[i] == "4" or s[i] == "5" or s[i] == "6" or s[i] == "7" or s[i] == "8" or s[i] == "9":
        z = int(s[i])
        print((s[i-1])*z, end="")
    
    

