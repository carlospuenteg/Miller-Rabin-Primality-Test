import random

'''
Miller's Rabin Primality Test
n is the number to check
k is the number of tests to run
'''
def isPrime(n, k=128):
    # 2 and 3 are primes
    if n == 2 or n == 3: 
        return True

    # if n <= 1 or n is not divisible by 2, then n is not prime
    if n <= 1 or n % 2 == 0:
        return False

    # initialize s and r
    s = 0
    r = n - 1

    # while r is even
    while ( r & 1 ) == 0:
        s += 1
        r //= 2 # r is floor divided by 2

    # do k tests
    for _ in range(k):
        a = random.randrange(2, n-1) # a = Random number between 2 and n-1
        x = pow(a, r, n) # x = a^r mod n

        if x != 1 and x != n-1:
            j = 1
            while j < s and x != n-1:
                x = pow(x, 2, n) # x = x^2 mod n
                if x == 1: # if x = 1, then n is not prime
                    return False
                j += 1
            if x != n-1: # if x is not n-1, then n is not prime
                return False
    return True

'''
>>> print(isPrime(43143988327398957279342419750374600193))
True
>>> print(isPrime(4))
False
'''
