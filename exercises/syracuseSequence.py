def main():
   num = eval(input("Input a starting number: "))

   while num != 1:
      if num % 2 == 0:
         num = num / 2
         print(int(num))
      elif num % 2 != 0:
         num = 3 * num + 1
         print(int(num))

main()
      
