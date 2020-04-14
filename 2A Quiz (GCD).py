a = int(input("First number: "))
b = int(input("Second number: "))


small = b if b < a else a
big = a if a > b else b
gcd = 1

for i in range(2, small // 2 + 1):
    if small % i == 0 and big % i == 0:
        gcd = i
if big % small == 0:
    gcd = small


print("The GCD of your numbers is {0}".format(gcd))


gcd = small if big % small == 0 else 1
