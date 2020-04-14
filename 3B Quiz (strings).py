word = input()
A = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
A2 = ["a", "e", "i", "o", "u"]

a = 0
e = 4
i = 8
o = 14
u = 20

"""
a's position = 0
e's position = 4
i's position = 8
o's position = 14
u's position = 20
"""

for i in range(len(word)):
    if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
        print(word[i],end="")
    else:
        print(word[i],end="")
        bigger1 = A.index(word[i]) if A.index(word[i]) > a else a
        smaller1 = a if A.index(word[i]) > a else A.index(word[i])
        sum1 = bigger1 - smaller1
        
        bigger2 = A.index(word[i]) if A.index(word[i]) > e else e
        smaller2 = e if A.index(word[i]) > e else A.index(word[i])
        sum2 = bigger2 - smaller2
        
        bigger3 = A.index(word[i]) if A.index(word[i]) > i else i
        smaller3 = i if A.index(word[i]) > i else A.index(word[i])
        sum3 = bigger3 - smaller3

        bigger4 = A.index(word[i]) if A.index(word[i]) > o else o
        smaller4 = o if A.index(word[i]) > o else A.index(word[i])
        sum4 = bigger4 - smaller4

        bigger5 = A.index(word[i]) if A.index(word[i]) > u else u
        smaller5 = u if A.index(word[i]) > u else A.index(word[i])
        sum5 = bigger5 - smaller5

        if sum1 == sum2:
            print("a",end="")
        elif sum2 == sum3:
            print("e",end="")
        elif sum3 == sum4:
            print("i",end="")
        elif sum4 == sum5:
            print("u",end="")
        
        elif sum1 < sum2 and sum1 < sum3 and sum1 < sum4 and sum1 < sum5:
            print("a",end="")
        elif sum2 < sum1 and sum2 < sum3 and sum2 < sum4 and sum2 < sum5:
            print("e",end="")
        elif sum3 < sum1 and sum3 < sum2 and sum3 < sum4 and sum3 < sum5:
            print("i",end="")
        elif sum4 < sum1 and sum4 < sum3 and sum4 < sum2 and sum4 < sum5:
            print("o",end="")
        elif sum5 < sum1 and sum5 < sum3 and sum5 < sum2 and sum5 < sum4:
            print("u",end="")
        
        if A[A.index(word[i])] == "z":
            print("z",end="")
        elif (A[A.index(word[i])+1]) in A2:
            print(A[A.index(word[i])+2],end="")
        else:
            print(A[A.index(word[i])+1],end="")
      
