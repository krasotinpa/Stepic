arr = ((0, -0.5), (1, 0), (0, 0.5), (0, 1.5), (1, 2.5), (2,3))

def sqerr(a, b):
  return (a - b)**2

def abserr(a, b):
  return abs(a - b)

def errsum(err_fun):
  return sum(list(map(lambda pair: err_fun(pair[0], pair[1]), arr)))

print(str(max(errsum(abserr), errsum(sqerr))))