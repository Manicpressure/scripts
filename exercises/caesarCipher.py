#This is the code of the Caesar Cipher. The basic function is to shift the letters of the original message
#up or down the alphabet to make a undecipherable message without knowing how many letters have been shifted.
#The main function will have user input whether to encode or decode.
#Once the selection is made the program will prompt the user to enter the message to be en/decoded, and the key.
#Only letters will be shifted, punctuation marks and spaces will be left as is.

import string
pText = str(string.ascii_uppercase+string.ascii_lowercase)
#This code makes a string of all the upper case and lower case alphabetical letters.
#This string will be used to turn the caesar cipher

def main():
    while True:
        print("-----------------------------")
        print("Caesar Cipher")
        print("Enter 1 to encode a message")
        print("Enter 2 to decode a message")
        print("Enter q to quit\n")
        edCode = input(" >>  ")
        if edCode == "1":
            encode = input("Message to encode: ")
            key = input("Key: ")
            cCipherEncoder(encode, key)

        elif edCode == "2":
            decode = input("Message to decode: ")
            key = input("Key: ")
            cCipherDecoder(decode, key)

        elif edCode == "q" or edCode == "Q":
            print("Thank you for using this program")
            break

        else:
            print("Invalid option {}".format(edCode))
#Print the menu with choices available to select.
#edCode sets up the variables to feed into the encoding/decoding functions
#cCipherEncoder and cCipherDecoder.

def cCipherEncoder(encode, key):
    encoded = ""
    for i in encode:
        j = pText.find(i)
        if j == -1:
            encoded = encoded + i
#encode is the message the user typed in, encoded is the message to be encoded.
#For every letter in the message, the code finds the letter in the alphabet
#and saves it as variable j
#If j reaches the end, the code terminates
        else:
            try:
                encoded = encoded + pText[int(j) + int(key)]
            except IndexError:
                encoded = encoded + pText[int(j) + int(key) - len(pText)]
    print("Encoded message : ", encoded, "\n")
#With the saved variable j, the letter is indexed from the pText alphabet string
#using sum of [j]+[key]. The indexed letter is added to the key to find position.
    with open('RC2e.txt', 'w') as RC2e:
        RC2e.write(encoded)
    return
#Write the encoded message to file and print

def cCipherDecoder(decode, key):
    decoded = ""
    for i in decode:
        j = pText.find(i)
        if j == -1:
            decoded = decoded + i
#Same concept as encoding function.
        else:
            try:
                decoded = decoded + pText[int(j) - int(key)]
            except IndexError:
                decoded = decoded + pText[int(j) - int(key) - len(pText)]
    print("Decoded message : ", decoded, "\n")
    with open('RC2d.txt', 'w') as RC2d:
        RC2d.write(decoded)
    return
#This time we subtract the variables to decode the message.

main()
#Activates the main code.
