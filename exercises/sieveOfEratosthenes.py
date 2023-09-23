#Sieve of erastosthenes
#Finds all prime numbers up to a given limit.
#Iteratively eliminates all composite numbers that are multiples of a prime number, starting with 2

import math
check = []

def primeCheck(primeC):
   for i in range(2, primeC+1):
      if primeC == i:
         return True
      elif primeC % i == 0:
         return False


def primeKill(primeK):
   for k in range(2, math.floor((check[-1]) / primeK)+1):
      primeK2 = primeK * k
      if primeK2 > check[-1]:
         break
      else:
         try:
            check.pop(check.index(primeK2))
         except ValueError:
            pass
   return check
         

def main():
   limit = eval(input("The number to which primes will be calculated: "))
   
   for i in range(2, limit + 1):
      check.append(i)

   for j in check:
      primeCheck(j)
      if primeCheck(j) == True:
         primeKill(j)
      elif primeCheck(j) == False:
         pass
      

   print(check)


main()

   
