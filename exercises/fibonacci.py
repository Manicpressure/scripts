#Input a number n into the program.
#Program will print up to the nth number in the fibonacci sequence.
#The program will also identify prime numbers in the sequence and mark with a P sign next to it.
#Then create a separate function to calculate the nth number of the sequence using 2 previous numbers
#F(m+n) = F(m)F(n+1) + F(m-1)F(n)

#Win condition
#Print the fibonacci sequence up to the nth number
#Mark prime numbers in the sequence with a (P) in a nested list
#Calculate and print the xth number extrapolated from the sequence using the equation

#Mark prime numbers in the sequence with a (P) in a nested list

#2021.12.18 comment : I could not mark prime numbers into a nested list in the fibonacci list because
#of the type error that occurs. There must be a way around this but for now I will settle for making a
#whole new list for prime numbers in the fibonacci sequence only.

#2021.12.19 0200 : Completed program with reserve. I was not able to mark a P next to the prime numbers in the
#sequence in a nested list. Instead I created a new list of prime numbers. This is not ideal but acceptable.

import math
fibonacci = [1, 1]

def main():
   nth = eval(input("Calculate fibonacci sequence to the nth number: "))
   Pfibonacci = []

   while len(fibonacci) != nth:
      fibonacci.append(fibonacci[len(fibonacci)-1]+fibonacci[len(fibonacci)-2])

   for i in fibonacci[2:]:
      for j in range(2, int(math.ceil(math.sqrt(i)))+1):
         if j == i or j == math.ceil(math.sqrt(i)):
            Pfibonacci.append(i)
         elif i % j == 0:
            break
         elif i % j != 0:
            pass
         
         
   print("\nFibonacci sequence: ", fibonacci)
   print("Prime numbers are: ", Pfibonacci)


   try:
      x = int(input("""\nInput number x if you want to calculate an upcoming number, or press enter to quit.
Condition : x <= nth + nth -1 : """))
      if isinstance(x, int):
         primecalc(x)
   except ValueError:
      print("Program terminated")

   
def primecalc(x):
   if x > len(fibonacci) - 1 + len(fibonacci):
      print("x is larger than the sum of the last two calculated fibonacci number positions")
   m = int(x/2 + 1)-1
   n = int(x/2 - 1)-1

   if x == m + n:
      xfibonacci = fibonacci[m] * fibonacci[n+1] + fibonacci[m-1] * fibonacci[n]
   if x != m + n:
      n = n + 1
      xfibonacci = fibonacci[m] * fibonacci[n+1] + fibonacci[m-1] * fibonacci[n]

   print("xth number in the fibonacci sequence is: ", xfibonacci)
   
   
   
main()
