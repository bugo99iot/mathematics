#this programs asks the user to input an even integer greater than 2 and expresses it as the sum of two primes
#the program gives all possible combinations of primes
#if you like to know how you can go from working in Subway aged 40 to solving one of the most important theorems in number theory read here: https://www.quantamagazine.org/yitang-zhang-and-the-mystery-of-numbers-20150402/


#this function returns true if its input is a prime, false otherwise

from datetime import datetime
from eratosthenes import prime_sieve

#prime_sieve generates a list of primes between 2 and n using a prime sieve

def is_prime(numba):
    if numba < 2:
        return False
    else:
        for k in range(2,numba-1):
            if numba % k == 0:
                return False
        else:
            return True

#if n-x = prime (call this y), then n = x + y !

def prime_sum(n):
    list = []
    for i in prime_sieve(n):
        if is_prime(n - i) == True and (n-i) >= i:
            list.append(str(i) + "+" + str(n-i))
    return list

#modify function above to return list of ways, prime_sum(28) returns ["5+23","7+21", etc...]

print "This code takes an even integer n greater than 2 and expresses all even numbers between 2 and n as a sum of two primes."

n = int(input("Enter n: "))

while n % 2 != 0 or n<2:
    print "You must enter an even number greater than 2."
    n = int(input("Enter n: "))
else:
    print "OK, ", n, "is a good number. Here is your decomposition: "
    start=datetime.now()
    evens = []
    for i in range(4, n+1, 2):
        evens.append(i)
    for i in evens:
        print i, " = ", " = ".join(prime_sum(i))


print "Time taken: ", datetime.now()-start



