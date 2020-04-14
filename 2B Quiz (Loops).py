number = int(input("Input number: "))
sum1 = number
sum2 = None

for i in range(1, number//2 + 1):
    if number % i == 0:
        sum1 += i
sum2 = sum1

for i in range(1, sum1//2 + 1):
    if sum1 % i == 0:
        sum2 += i
if sum2 / number == 2:
    print("Your number IS superperfect.")
else:
    print("Your number is NOT superperfect.")
    



             
  
