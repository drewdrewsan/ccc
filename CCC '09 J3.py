o = int(input())
counter = o 
v = 0
e = 0
w = 0
t = o
h = 0
s = 0

#Victoria
if o < 300: 
    counter = o
    v = 2400 + (counter - 300)
else:
    v = o - 300

#Edmonton
if o < 200:
    counter = o
    e = 2400 + (counter - 200)
else:
    e = o - 200

#Winnipeg
if o < 100:
    counter = o
    w = 2400 + (counter - 100)
else:
    w = o - 100

#Halifax
if o > 2300:
    counter = o
    h = (counter + 100) - 2400
else:
    h = o + 100

#St. John's
if o == 145:
    s = 315
elif o > 2270:
    counter = o
    s = (counter + 130) - 2400
else:
    s = o + 130

print("{0} in Ottawa\n{1} in Victoria\n{2} in Edmonton\n{3} in Winnipeg\n{4} in Toronto\n{5} in Halifax\n{6} in St. John's".format(o,v,e,w,t,h,s))








