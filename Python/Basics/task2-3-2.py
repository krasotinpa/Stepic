import itertools

def primes():
    p = 2
    fuctorial = 1
    while True:
        if (fuctorial+1) % p == 0:
            yield p
        fuctorial *= p
        p += 1

print(list(itertools.takewhile(lambda x : x <= 10, primes())))
