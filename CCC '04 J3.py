n = int(input())
m = int(input())
noun = []
adj = []

for i in range(n):
    w = input()
    noun.append(w)

for j in range(m):
    w = input()
    adj.append(w)

for i in range(len(noun)):
    for j in range(len(adj)):
        print("{0} as {1}".format(noun[i],adj[j]))
