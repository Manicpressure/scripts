#Euclid's algorithm
#Calculates the greatest common divisor of two integers, the largest number that divides them
#without a remainder. Based on the principle that the GCD of two numbers do not change if the
#larger number is replaced by its difference with the smaller number. 

def main():
   a = eval(input("Enter first number: "))
   b = eval(input("Enter second number: "))
   c = max(a,b)
   d = min(a,b)
   euclid(c, d)

def euclid(A, B):
   if A % B == 0:
      print("GCD : ", B)
   
   r = A % B
   A = B
   B = r

   if r != 0:
      euclid(A,B)
      

main()
      
