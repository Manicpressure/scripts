#Chaos function generates a series of pseudo-random numbers.
import random

def main():
   n = eval(input("How many iterations? "))
   x = random()
   
   for i in range(n):
      x = 3.9 * x * (1 - x)
      print(x)

   again = input("Again?? y/n ")
   if again[0] == y or again[0] == Y:
      main()
   else:
      print("Closing program")

main()




