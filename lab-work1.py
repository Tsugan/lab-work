ar = []
while True:
    a = input()
    if a == "":
        break
    else:
        ar.append(a)

array = [int(x) for x in ar]
array.sort()

x = array[-1]
y = array[-2]
z = array[-3]

def f(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        p = (x+y+z)/2
        s = (p*(p-x) * (p - y) * (p - z))**0.5
        print(s)
    else:
        print('Треугольника не существует')
f(x, y, z)