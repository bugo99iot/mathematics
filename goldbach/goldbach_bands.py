#this programs asks the user to input an even integer greater than 2 and expresses it as the sum of two primes
#the program gives all possible combinations of primes
#if you like to know how you can go from working in Subway aged 40 to solving one of the most important theorems in number theory read here: https://www.quantamagazine.org/yitang-zhang-and-the-mystery-of-numbers-20150402/


from datetime import datetime
from eratosthenes import prime_sieve
import matplotlib.pyplot as plt
import sys


#this function returns true if its input is a prime, false otherwise

def is_prime(numba):
    if numba < 2:
        return False
    else:
        for k in range(2,numba-1):
            if numba % k == 0:
                return False
        else:
            return True

#this function returns "prime_sum(22) = [['3+19', '5+17', '11+11'], 3]"
#if n-x = prime (call this y), then n = x + y !
#prime_sieve generates a list of primes between 2 and n using a prime sieve

def prime_sum(n):
    list = []
    both = []
    for i in prime_sieve(n):
        if is_prime(n - i) == True and (n-i) >= i:
            list.append(str(i) + "+" + str(n-i))
    both=[list,len(list)]
    return both

print prime_sum(22)[1]

#this function produces all even numbers up to n

def even_numbers_to_n(n):
    evens = []
    for i in range(4, n+1, 2):
        evens.append(i)
    return evens

#in what follow we split numbers into mod-bands for n mod 6 = 0,2,4. 
#For more info, read: https://scipython.com/blog/the-goldbach-comet/

n = int(input("Enter n: "))

n_0=[] #list of numbers for which n (even) % 6 = 0
n_2=[]
n_4=[]

nrp_0=[] #number of representations of each n (even) % 6 = 0
nrp_2=[]
nrp_4=[]

all_evens=even_numbers_to_n(n)

for i, item in enumerate(all_evens):
    if item % 6 == 0:
        n_0.append(item)
        nrp_0.append(prime_sum(all_evens[i])[1])
    if item % 6 == 2:
        n_2.append(item)
        nrp_2.append(prime_sum(all_evens[i])[1])
    if item % 6 == 4:
        n_4.append(item)
        nrp_4.append(prime_sum(all_evens[i])[1])

print max(nrp_0)
print int((round(float(max(nrp_0))/0.9))/100)*100

#plot even numbers vs. numer of prime sum representations
plt.scatter(n_0, nrp_0, marker="o", c="r", alpha=1, s=350,label="n mod 6 = 0")
plt.scatter(n_2, nrp_2, marker="o", c="b", alpha=1, s=350,label="n mod 6 = 2")
plt.scatter(n_4, nrp_4, marker="o", c="y", alpha=1, s=350,label="n mod 6 = 4")
plt.suptitle("Goldbach's Conjecture", fontsize=36, fontweight='bold')
plt.xlabel('Even numbers',fontsize=32)
plt.ylabel('Prime representations',fontsize=32)
plt.legend(loc='upper left')
plt.xlim(4, n)
plt.ylim(1, int((round(float(max(nrp_0))/0.9))/100)*100)
plt.matplotlib.rcParams.update({'font.size': 32})
plt.show()


