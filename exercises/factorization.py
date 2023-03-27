# factorial = 0
#
#
# def fact(nr):
#     while nr > 0:
#         global factorial
#         factorial = factorial * nr
#         print(factorial)
#         fact(nr-1)
#     return


# print(factorial)
# fact(2)
# print(factorial)
# TODO come back after loops part
'''
This code displays the greatest common divisor (GCD) and the least common multiple (LCM) of two positive integers
entered by the user.
E.g., for 180 and 1944: GCD = 36, LCM=9720
'''

import math
import sys

def inputCheck(num):
    if num / 1 != num // 1:
        #sys.exit() stops the execution
        sys.exit("The entered number is not an integer!")
    elif num < 1:
        sys.exit("The entered number is not a positive integer!")

#prime() function checks whether j is prime or not
def prime(j):
    i=1
    counter=0
    #Math module is imported to get the sqrt method. Instead of that, you may control the loop by i<=j/2
    while i<math.sqrt(j):
        if j%i==0:
            counter+=1
        i+=1
    if counter<2:
        return True
    else:
        return False

#createPrimeFactorization() returns a dictionaries, whose keys are the primes that build up the number
# and their values are their exponent in the prime factorization of the input number.
# e.g., for 234:
# {2:1, 3:2, 13:1}
def createPrimeFactorization(num):
    if num == 1:
        primes = {1:1}
    else:
        primes = {}
        i = 2
        while i <= num:
            if prime(i):
                while num % i == 0:
                    if i in primes:
                        primes[i]=primes[i]+1
                    else:
                        primes[i]=1
                    num /= i
            i += 1
    return primes

num1=float(input("Enter the first positive integer:\n"))
inputCheck(num1)
primes1=createPrimeFactorization(num1)
num2=float(input("Enter the second positive integer:\n"))
inputCheck(num2)
primes2=createPrimeFactorization(num2)
#Note: we do not have to use primes2=createPrimeFactorization(num2).copy(), since each function call creates a new dictionary,
#that is why primes1 and primes2 are stored at different places in the memory.

# -- Uncomment for checking purposes: --
#print(f"Prime factorization of {int(num1)} is: {primes1}")
#print(f"Prime factorization of {int(num2)} is: {primes2}")

primeSet1=set(primes1.keys())
primeSet2=set(primes2.keys())
intersectionSet=primeSet1.intersection(primeSet2)
unionSet=primeSet1.union(primeSet2)
# -- Uncomment for checking purposes: --
#print(f"The common prime numbers of the factorizations are: {intersectionSet}")
#print(f"All the prime numbers of the factorizations are: {unionSet}")

gcd=1
lcm=1
for prime in intersectionSet:
    if primes1[prime]<primes2[prime]:
        gcd*=prime**primes1[prime]
        lcm*=prime**primes2[prime]
    else:
        gcd*=prime**primes2[prime]
        lcm*=prime**primes1[prime]

for prime in primeSet1.difference(primeSet2):
    lcm*=prime**primes1[prime]

for prime in primeSet2.difference(primeSet1):
    lcm*=prime**primes2[prime]

print(f"The greatest common divisor (GCD) of {int(num1)} and {int(num2)} is: {gcd}")
print(f"The least common multiple (LCM) of {int(num1)} and {int(num2)} is: {lcm}")
