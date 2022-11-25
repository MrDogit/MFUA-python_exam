from math import sqrt
d = {'x':[ 0, 0.5, 2 ], 'y':[ 0, -0.5, 3 ]}
x1 = d['x'][0]
y1 = d['y'][0]
x2 = d['x'][1]
y2 = d['y'][1]
x3 = d['x'][2]
y3 = d['y'][2]

# a - 12 b - 23 c - 31
a = sqrt((x2-x1)**2+(y2-y1)**2)
b = sqrt((x3-x2)**2+(y3-y2)**2)
c = sqrt((x3-x1)**2+(y3-y1)**2)
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)