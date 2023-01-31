def main():
    #When the user inputs a list of numbers and words, the program is meant to convert the whole list to the other
    #The program needs to repeat itself until the user closes the program by pressing enter
    #The conversion should include multi character inputs such as 122 being converted to 'z'
    #Convertibles do not include alternative number systems
   string = input("\nInput the convertibles separated by space or press enter to close: ")
   stringN = []
    
   if string == "": print("Conversion finished")
    
   if string != "":
      string = list(string.split(' '))
      for i in string:
         try:
            i = int(i)
            stringN.append(chr(i))
         except ValueError:
            stringN.append(ord(i))
      print(string)
      print(stringN)

      main()

main()


##Version X
##    if string != "":
##        for i in string:
##            try:
##                i = int(i)
##                stringN.append(chr(i))
##            except ValueError:
##                stringN.append(ord(i))
##        print(string.split(','))
##        print(stringN)
##
##        main()
##                
##    if string == "": print("Conversion ended")




