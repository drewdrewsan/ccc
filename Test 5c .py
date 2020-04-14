def prime(x):
    prime = ""
    for i in range(2, x//2):
        if x % i == 0:
            prime = "no"
            return prime
    prime = "yes"
    return prime

n = input()
digits = []
factors = []
random = 0
counter = n

for i in range(len(n)):
    if n[i] in digits:
        random += 1
    else:
        digits.append(n[i])

flag = True
while flag == True:
    for i in range(2, int(counter) //2):
        if int(counter) % i == 0:
            if i in factors:
                random += 1
            elif prime(i) == "yes":
                factors.append(i)
                counter = int(counter) // i
                i = 2
    flag = False

if len(digits) > len(factors):
    print("frugal")
else:
    print("not frugal")

