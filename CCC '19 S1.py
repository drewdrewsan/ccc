motion = input()
a = [[1, 2],
     [3, 4]]

if motion.count("H") % 2 == 1:
    a = [a[1], a[0]]
if motion.count("V") % 2 == 1:
    a = [[ a[0][1], a[0][0] ], [a[1][1],a[1][0]]]

print(a[0][0], a[0][1])
print(a[1][0], a[1][1])
        
