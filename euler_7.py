def sieve_of_eratosthenes(n):
    sieve = [True for i in range(n + 1)]
    primes = []
    p = 2
    while (p * p <= n):
        if sieve[p] == True:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
    print(primes[10001 - 1])

sieve_of_eratosthenes(1000000)