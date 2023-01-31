#Numbering systems program
#This program will change numbering systems of 2 numbers
#After conversion it will prompt you if you want to convert again
#The conversion will happen between any two numbers from any numbering system
#The conversion must apply to decimal point numbers as well
#The number systems goes from 0 ~ 9, A ~ Z, a ~ z, for a maximum of base 61
#ord(A) = 65, ord(Z) = 90, ord(a) = 97, ord(z) = 122 for reference

#verify results at https://www.rapidtables.com/convert/number/base-converter.html

# - Program can convert any number system less than or equal to decimal system to any
# number base system up to base 61
# - Decimals can be converted too but only up to 5th place
# - You cannot convert any numbers that contain letters
#e.g 10 from decimal system to binary
#e.g 1208 from base 11 to base 26


import string
import math

def intro():
   print("""This program converts any number equal to or below the decimal system to any number base up to 61.
Decimal points can also be converted but only up to the 5th decimal place.
The numbers are from 0-9, A-Z, a-z.\n""")

   sNumber = eval(input("Enter the source number to be converted : "))
   sBase = eval(input("Enter the source number base : "))
   cBase = eval(input("Enter the conversion number base : "))
   return sNumber, sBase, cBase

#Intro will capture the 3 main inputs to the program.

def plan(sNumber, sBase, cBase):
#The point of 'plan' is to analyze the number that has come in and apply the correct functions
#in order to net out the correct conversion
   intConL = []
   decConL = []
   sNumberW = int(sNumber)
   sNumberD = sNumber % 1
#initialize the lists and variables that will be used.
#intConL = list that will house the integer conversion while it is being modified
#decConL = list that will house the decimal conversion while it is being modified
#sNumberW = source number whole (with only the integer part)
#sNumberD = source number decimal (with only the decimal part)

   if sBase != 10 and cBase == 10:
      snNumber = toDecimal(sNumberW, sBase, sNumberD)
      return snNumber

#There are 3 movements that are possible.
#Non decimal to decimal.
#Decimal to non decimal
#Non decimal to non decimal
#The first condition is to change to a decimal number

   elif sBase == 10 and cBase != 10:
      snNumber = fromDecimal(sNumberW, sNumberD, cBase, intConL, decConL)
      return snNumber

#Second condition is to change from a decimal number

   elif sBase != 10 and cBase != 10:
      snNumber = toDecimal(sNumberW, sBase, sNumberD)
      sNumberW = int(snNumber)
      sNumberD = snNumber % 1
      snNumber = fromDecimal(sNumberW, sNumberD, cBase, intConL, decConL)
      return snNumber

#The third condition of changing a non decimal to non decimal involves :
#Changing the non decimal source number base to an interim decimal number
#Then changing the interim decimal number to destination number base
#We first convert to a decimal number with the toDecimal() function
#Then because the interim number is different from the original input, we need to make an interim place holder
#The interim place holders are then put into the fromDecimal() function towards the destination number base

def toDecimal(sNumberW, sBase, sNumberD):
   snNumberW = toDecimalW(sNumberW, sBase)
   if sNumberD != 0:
      snNumberD = toDecimalD(sNumberD, sBase)
      snNumber = float(snNumberW + snNumberD)
      return snNumber
   snNumber = int(snNumberW)
   return snNumber

#This is the owner function that contains both slave functions.
#This is necessary in case decimal numbers exist.
#First we convert the number on the whole numbers side snNumberW
#If there is a decimal component we need to get the snNumberD
#Since snNumberW is a whole number, snNumberD is a decimal, it is possible to just add them together.
#The code must be ordered that way so that all the variables are referenced by the time you return snNumber

def toDecimalW(sNumberW, sBase):
   sNumberL = list(map(int,str(sNumberW)))
   snNumberL = []
   c = 1
   snNumberW = 0
   for i in sNumberL:
      snNumberL.append(i * sBase ** (len(sNumberL)-c))
      c += 1
   for i in range(0, len(snNumberL)):
      snNumberW = snNumberW + snNumberL[i]
   return snNumberW

#Split up the number into digits and put them into a list to iterate
#initialize the converted number list, counter, and final converted number
#iterate through the elements in sNumberL 'i', and multiply by base^c. Since the digits start at the largest,
#The exponent needs to start off with the biggest and decrease per iteration
#Lastly, sum all the elements in the list together to get the final whole number component

def toDecimalD(sNumberD, sBase):
   sNumberD = int(sNumberD * 10000)
   sNumberL = list(map(int,str(sNumberD)))
   snNumberL = []
   snNumberD = 0
   c = 1
   for i in sNumberL:
      snNumberL.append(i * sBase ** -c)
      c += 1
   for i in range(0, len(snNumberL)):
      snNumberD = snNumberD + snNumberL[i]
   
   if snNumberD < 100 and snNumberD > 10:
      snNumberD = snNumberD / 100
   elif snNumberD < 10 and snNumberD > 1:
      snNumberD = snNumberD / 10
   return snNumberD

#Decimal places dont allow python manipulation very well so we will be turning the decimals into a whole number
#by multiplying by 10 000, then splitting it up for the same operation as toDecimalW()
#This time, the exponent increases negatively
#Once the digits are split up, multiplied by digit exponents, and then summed up, we need to make it a decimal
#number again. We will do this by dividing by x depending on the value of the snNumberD

def fromDecimal(sNumberW, sNumberD, cBase, intConL, decConL):
   intConL = intCon(sNumberW, cBase, intConL)
   if sNumberD != 0:
      decConL = decCon(sNumberD, cBase, decConL)
      convertLD2 = dictDecimal(decConL)
      convertLD2 = ''.join(str(y) for y in convertLD2)
      
   intConL = intConL[::-1]
   convertLW2 = dictDecimal(intConL)
   convertLW2 = ''.join(str(x) for x in convertLW2)

   if sNumberD != 0:
      snNumber = str(convertLW2) + "." + str(convertLD2)
   else:
      snNumber = convertLW2
   return snNumber

#This is the Master function controlling the 3 slave functions. One for whole number, decimal number, and
#final function for conversion of number into corresponding values.
#First, we need to input the whole number, decimal number, destination number base, and a housing list for
#the whole number/decimal number conversions (intConL and decConL).

#intConL is given by the function intCon, which houses the converted digits into a list.
#Once the list is obtained, dictDecimal() converts the digits into the new number system digit.
#The list of digits is then joined together to make a single number to represent a whole number or decimal part
#The final number can be produced with a little string manipulation

def intCon(sNumberW, cBase, intConL):
   if (sNumberW // cBase) < cBase:
      intConL.append(sNumberW % cBase)
      intConL.append(sNumberW // cBase)
   else:
      x = (sNumberW // cBase)
      intConL.append(sNumberW % cBase)
      intCon(x, cBase, intConL)
   return intConL

#intCon function converts the decimal number into the destination number base through a recursive function.
#On the exit condition (when there are no more possible divisions), we need to add the remainder and 
#the divided. Because the function is recursive with the closing condition adding in reverse,
#it returns the digits in reverse order. 

def decCon(sNumberD, cBase, decConL):
   if len(decConL) == 5:
      return decConL
   else:
      a = sNumberD * cBase
      decConL.append(int(a//1))
      b = a % 1
      decCon(b, cBase, decConL)
   return decConL

#The decimal conversion function converts the decimal part of the decimal number. This is done through a
#recursive function. However, because the closing condition does not have any commands, the recursive function
#produces the number in correct order.

def dictDecimal(convertL):
   convertL2 = []
   dnumbers = {}
   dKey = []
   for i in range(62):
      dKey.append(i)
   dVal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] + list(string.ascii_uppercase) + list(string.ascii_lowercase)
   dnumber = dict(zip(dKey, dVal))

   for i in range(0, len(convertL)):
      convertL2.append(dnumber.get(convertL[i]))
   return convertL2

#The strings of numbers and alphabets are initialized first.
#The numbers are then zipped into a dictionary with 0-61 for keys and 0-9 A-Z a-z for values
#The function returns a list that can be manipulated offsite.

def summary(sNumber, sBase, cBase, snNumber):
   print("Converting \"{}\" from base \"{}\" to base \"{}\" = {}".format(sNumber, sBase, cBase, snNumber))
   startagain = input("Would you like to convert another number? Y/N ")
   if startagain[0] == 'y' or startagain[0] == 'Y':
      main()
   else:
      print("Closing program")

#Summary function to state the conversion parameters and results
#Finally to prompt user if the program needs to be run again or not.

def main():
   sNumber, sBase, cBase = intro()
   snNumber = plan(sNumber, sBase, cBase)
   summary(sBase, sBase, cBase, snNumber)
   
main()




























#Version 1
#Got the mathematics wrong, needed to start again in order to achieve the objectives of this program
##
##import string
##import math
###import decimal
##
##
##def divisor(convertw, convN, division):
##   if (convertw // convN) < convN:
##      division.append(convertw % convN)
##      division.append(convertw // convN)
##
##   else:
##      x = (convertw // convN)
##      division.append(convertw % convN)
##      divisor(x, convN, division)
##
##   return division
##
###Recursive function to calculate the new base number.
###Condition break upon the divisor being smaller than the dividend.
###The remainders will be slotted into a list for conversion into their new base numbers later
###The final dividend is the first digit in the new number base number
##
##
##def decimalcon(convertd, convN, multiply):
##   if len(multiply) == 5:
##      return multiply
##
##   else:
##      a = convertd * convN
##      multiply.append(int(a//1))
##      b = a % 1
##      decimalcon(b, convN, multiply)
##
##   return multiply
##
##def sourceDecimal():
##   
##
###Break condition upon reaching 5 decimal places
###We will be doing a maximum of 5 decimal places so set the exit condition to when the number of digits
###reach 5. The algorithm for converting decimal places to number base is in the code.
###Every iteration adds a digit to the base number.
###To be clear, multiply is the number that we are converting to in the new number base system.
##
##def main():
##   dnumbers = {}
##   dKey = []
##   for i in range(62):
##      dKey.append(i)
##   dVal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] + list(string.ascii_uppercase) + list(string.ascii_lowercase)
##   dnumber = dict(zip(dKey, dVal))
##
###initialize the dictionary that will be used to convert numbers with different number base systems.
###zip the keys and value lists together to create a dictionary quickly
###the dictionary goes from 0 to 61, just enough to take the milestone of base 60.
##   
##   convert = eval(input("Enter the number to be converted : "))
##   baseN = eval(input("Enter the number base of the number : "))
##   convN = eval(input("Enter the number base that the number will be converted to : "))
##
###Take the inputs. We need the number to be converted, the number base it is in, and the number base we will
###convert to.
##
##   convertd = convert % 1
##   convertw = int(convert)
##
###remainder of dividor by 1, gives the float of the remainder
###making the number an integer gets rid of the decimals
##
##   if convert == convertd + convertw and convertd != 0:
##      multiply = []
##      multiply = decimalcon(convertd, convN, multiply)
##      multiply2 = []
##
###convertd = decimal part of the converting number, convertw = integer part of the converting number
###we can test whether there are decimal numbers with the if statement.
###multiply contains the converted decimal number. multiply2 is an empty list
##
##      for i in range(0, len(multiply)):
##         multiply2.append(dnumber.get(multiply[i]))
##      multiply2 = ''.join(str(y) for y in multiply2)
##
###cycling through 1 to 5, the value of the list is transponded to the dictionary as the key
###and the value is appended to the mulitply2 list, which can now be modified one last time to
###make a single string
##
##   division = []
##   division = divisor(convertw, convN, division)
##   division = division[::-1]
##   division2 = []
###initialize a list to put the results into during the division.
###set a variable to which I can put the results of the function into
###reverse the list and then join up the elements in the list after stringifying them.
##
##   for j in range(0, len(division)):
##      division2.append(dnumber.get(division[j]))
##   division2 = ''.join(str(x) for x in division2)
##   
###cycle through the digits in division2, get the element in the list, transpond to the dictionary key
###get the value corresponding to the key, and add it to division3, the final list.
##   if convertd != 0:
##      finalN = str(division2) + "." + str(multiply2)
##   else:
##      finalN = str(division2)
##
###Finally putting together the converted number. We need to determine whether to include the
###decimals in the final number with the if/else statement
##
##   summary = 'Converting {} in base {} to base {} = {}'.format(convert, baseN, convN, finalN)
##   print(summary)
##
###Use string formatting to tidy up the program tidily.
##   
##main()
