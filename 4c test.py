def encryptLetter(ltr, k):
    pos = 0
    newletter = ""
    if ord(ltr) + k > 122:
        pos = ((ord(ltr)+k) - 122) + 96
        newLetter = chr(pos)
        return newLetter
    else:
        newLetter = chr(ord(ltr) + k)
        return newLetter

def encryptWord(w, k):
    word = ""
    for i in range(len(w)):
        word += encryptLetter(w[i], k)
    return word

def encryptSentence(s, k):
    sentence = ""
    A = s.split()
    for i in range(len(A)):
        sentence += encryptWord(A[i], k)
        sentence += " "
    return sentence

def decryptLetter(ltr, k):
    pos = 0
    letter = ""
    if ord(ltr) - k < 97:
        pos = 123 - (97 - (ord(ltr)-k))
        letter = chr(pos)
        return letter
    else: 
        letter = chr(ord(ltr)-k)
        return letter

def decryptWord(w, k):
    word = ""
    for i in range(len(w)):
        word += decryptLetter(w[i], k)
    return word

def decryptSentence(s, k):
    sentence = ""
    A = s.split()
    for i in range(len(A)):
        sentence += decryptWord(A[i], k)
        sentence += " "
    return sentence

#a = 97
#z = 122

l = input()
n = int(input())
hi = encryptSentence(l, n)
lol = decryptSentence(encryptSentence(l, n), n)
print(hi)
print(lol)

