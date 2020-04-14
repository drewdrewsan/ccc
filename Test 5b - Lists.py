def listPrimes(n):
    A = []
    p = 2
    counter = 1
    for i in range(2, n+1):
        A.append(i)
    flag = True
    while flag == True:
        for i in A:
            if i != p and i % p == 0:
                A.remove(i)
        if counter < len(A):
            p = A[counter]
            counter += 1
        elif i == A[-1]:
            if i != p and i % p == 0:
                A.remove(i)
            if counter < len(A):
                p = A[counter]
                counter += 1
            return(A)

def find2Primes(n):
    counter = 0
    A = listPrimes(n)
    final = []
    flag = True
    while flag == True:
        for i in range(len(A)):
            if A[counter] + A[i] == n:
                final.append(A[counter])
                final.append(A[i])
                return(final)
            elif A[counter] + A[i] != n and i+1 == len(A):
                counter +=1


def twolines(n):
    counter = 0
    A = listPrimes(n)
    A.pop(0)
    final = []
    flag = True
    while flag == True:
        for i in range(len(A)):
            for j in range(len(A)):
                if A[counter] + A[i] + A[j] == n:
                    final.append(A[counter])
                    final.append(A[i])
                    final.append(A[j])
                    return(final)
        if A[counter] + A[i] + A[j] != n and i+1 == len(A):
            counter +=1






def find3Primes(n):
    return(3, find2Primes(n-3))

    

n = int(input())
print(listPrimes(n))
if n % 2 == 0:
    print(find2Primes(n))
else:  
    print(find3Primes(n))

