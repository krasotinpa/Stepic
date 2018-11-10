def z(x,y):
    return x**3 + 4 * y**3 - 3*x - 3*y

def dz2xx(x, y):
    return 6*x

def dz2xy(x, y):
    return 0

def dz2yy(x, y):
    return 24*y

ans = [(1, 0.5), (1, -0.5), (-1, 0.5), (-1, -0.5)]

for a in ans:
    print(a, z(*a))