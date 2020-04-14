def sumDivisors(n):
    s = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            s += i
    return s

def perfect(n):
    sd = sumDivisors(n)
    if sd == n:
        return True
    else:
        return False

def sumSquares(n):
    A = [i for i in str(n)]
    x = 0
    for i in A:
        x += int(i) * int(i)
    return x
    

def happy(n):
    sums = int(n)
    s = ""
    for i in range(14):
        s = sumSquares(sums)
        if s == 1:
            return True
            break
        else:
            sums = s
    return False

def practical(n):
    if happy(n) == False and perfect(n) == False:
        return True
    else:
        return False
        

test1 = practical(int(input()))
print(test1)
        

        
