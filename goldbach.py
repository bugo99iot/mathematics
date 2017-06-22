#this programs asks the user to input an even integer greater than 2 and expresses it as the sum of two primes
#the program gives all possible combinations of primes
#if you like to know how you can go from working in Subway aged 40 to solving one of the most important theorems in number theory read here: https://www.quantamagazine.org/yitang-zhang-and-the-mystery-of-numbers-20150402/


#this function returns true if its input is a prime, false otherwise

from datetime import datetime


def is_prime(numba):
    if numba < 2:
        return False
    else:
        for k in range(2,numba-1):
            if numba % k == 0:
                return False
        else:
            return True

#gen_primes generates a list of primes between 3 and n using a recursive method

def gen_primes(n):
    primes = []
    for numba in range(2,n):
        if is_prime(numba) == True:
            primes.append(numba)
    return primes

#if n-x = prime (call this y), then n = x + y !

def prime_sum(n):  
    list = []
    for i in gen_primes(n):
        if is_prime(n - i) == True and (n-i) >= i:
            list.append(str(i) + "+" + str(n-i))
    return list

#modify function above to return list of ways, prime_sum(28) returns ["5+23","7+21", etc...]

print "This code takes an even integer n greater than 2 and expresses all even numbers between 2 and n as a sum of two primes."

n = int(input("Enter n: "))

start=datetime.now()


while n % 2 != 0 or n==2:
    print "You must enter an even number greater than 2."
    n = int(input("Enter n: "))
else:
    print "OK, ", n, "is a good number. Here is your decomposition: "
    evens = []
    for i in range(4, n+1, 2):
        evens.append(i)
    for i in evens:
        print i, " = ", " = ".join(prime_sum(i))
        

print "Time taken: ", datetime.now()-start



