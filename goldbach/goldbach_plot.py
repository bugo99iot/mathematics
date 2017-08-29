#this programs asks the user to input an even integer greater than 2 and expresses it as the sum of two primes
#the program gives all possible combinations of primes
#if you like to know how you can go from working in Subway aged 40 to solving one of the most important theorems in number theory read here: https://www.quantamagazine.org/yitang-zhang-and-the-mystery-of-numbers-20150402/


#this function returns true if its input is a prime, false otherwise

from datetime import datetime
from eratosthenes import prime_sieve
import matplotlib.pyplot as plt
import sys

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
    number_of_ways = 0
    both = []
    for i in prime_sieve(n):
        if is_prime(n - i) == True and (n-i) >= i:
            list.append(str(i) + "+" + str(n-i))
    both=[list,len(list)]
    return both

def even_numbers_to_n(n):
    evens = []
    for i in range(4, n+1, 2):
        evens.append(i)
    return evens

def representations_of_n(n):
    repr=[]
    for i in even_numbers_to_n(n):
        repr.append(prime_sum(i)[1])
    return repr

n = int(input("Enter n: "))

#fig = plt.figure()

#plot even numbers vs. numer of prime representations
plt.plot(even_numbers_to_n(n), representations_of_n(n), "ro", markersize=20)
plt.matplotlib.rcParams.update({'font.size': 36})
plt.suptitle("Goldbach's Conjecture", fontsize=36, fontweight='bold')
plt.xlabel('Even numbers')
plt.ylabel('Prime representations')
plt.show()


