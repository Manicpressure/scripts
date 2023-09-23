#Goldbach conjecture asserts that every even number is the sum of two prime numbers.
#Evaluate the 2 prime numbers that sum into the even number that the user inputs


#Sieve of Eratosthenes
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
         

def sieve(limit):
   for i in range(2, limit + 1):
      check.append(i)

   for j in check:
      primeCheck(j)
      if primeCheck(j) == True:
         primeKill(j)
      elif primeCheck(j) == False:
         pass
   return check

#//Sieve of Eratosthenes

def main():
   even = eval(input("Enter an even number greater than 2, to which two prime numbers will sum to: "))

   if even == "":
      print("Program terminated")
   
   if even % 2 == 0 and even > 2:
      sieve(even)
      for i in check:
         for j in check[:(int(len(check)/2)+1)]:
            if even == i + j:
               print('Primes', i, 'and', j, 'sum to the number', even)
               
   elif even % 2 == 1 or even <= 2:
      print("Number is an odd number or lesser than 2.")
      main()


main()
