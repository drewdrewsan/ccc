n = int(input())
s = 0
t = 0

for i in range(n):
    sentence = input()
    for j in range(len(sentence)):
        if sentence[j] == "t" or sentence[j] == "T":
            t += 1
        elif sentence[j] == "s" or sentence[j] == "S":
            s += 1

if s > t:
    print("French")
elif t > s:
    print("English")
elif t == s:
    print("French")
