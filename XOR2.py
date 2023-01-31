#This program seems to be an almost repeat of python challenge 2
#I will take the liberty of copying the code I wrote and modifying it for use here

#XOR Encoding
#Input = RC2.txt
#Output = RC3.txt

#XOR Decoding
#Input = RC3.txt
#Output = RC4.txt

#Key
#Input = Key.txt

def menu():
    print("\n-----------------------------------------------")
    print("[1] to encode with XOR")
    print("[2] to decode with XOR")
    print("[0] to exit program")
# Print out the menu

def XORencode():
    with open('RC2.txt') as plainText:
        encodeText = ""
        with open("Key.txt", "r") as keyData:
            key = keyData.read()
        #Modified the above 2 lines for the new python challenge to read from key.txt
        keyRotation = 0
        print("\n")
        # Initialize variables and open file

        line = plainText.read()
        for char in range(len(line)):
            char2 = ord(line[char]) ^ ord(key[keyRotation])
            # '^' is XOR function in python. XOR with character in message with key
            # with a for loop. Each character is encoded.
            encodeText += hex(char2)[2:].zfill(2)
            # hex() conerts integer (ascii character) to hexadecimal number.
            # Since hex() prefixes 0x, [2:] to remove it.
            # zfill pads single char hex with 0 to make it a pair
            # Otherwise double digit integers dont get read correctly in the hexadecimal system
            # Due to hex going up at 16 = F
            keyRotation += 1
            if keyRotation >= len(key):
                keyRotation = 0
        print("Encrypted text :")
        print(encodeText)
        with open('RC3.txt', 'w') as cText:
            cText.writelines(encodeText)
        # Write to file as directed


def XORdecode():
    with open('RC3.txt') as ciphertext:
        hexDecode = ""
        with open("Key.txt", "r") as keyData:
            key = keyData.read()
        #Modified the above 2 lines for the new pyhton challenge task
        print("\n")
        keyRotation = 0
        decryptText = ""
        # Initialization. We need to decode the hex first then the ciphertext

        line2 = ciphertext.read()
        for hex in range(0, len(line2), 2):
            hexDecode += bytes.fromhex(line2[hex:hex+2]).decode('utf-8')
        # Hex is in pair digits due to encoding from decimal.
        # Need to decode pair digits at a time with bytes.fromhex

        for code in range(len(hexDecode)):
            code2 = ord(hexDecode[code]) ^ ord(key[keyRotation])
            decryptText += chr(code2)
    # Decoding is the same process in reverse, but requires to change
    # ASCII to normal text at the end with chr()
            keyRotation += 1
            if keyRotation >= len(key):
                keyRotation = 0
            # If key is multiple digits/letters, we can rotate through the characters
            # to make a stronger encryption. Standard practice.
        print("Decrypted text :")
        print(decryptText)
        with open('RC4.txt', 'w') as dText:
            dText.writelines(decryptText)
        # Write to file as directed


if __name__=='__main__':
    print("Please put the following files in the source folder with the program")
    print("XOR Encode takes input from RC2.txt and outputs to RC3.txt")
    print("XOR Decode takes input from RC3.txt and outputs to RC4.txt")
    while(True):
        menu();
        try:
            option = int(input('Type in the option you want to do -- '));
        except:
            print('Invalid input');
            menu();
# Set up the menu.
# While loop will keep the program operating until user decides to quit
# Give the user a choice, and limit user input to integers that I set to limit errors.
        if option == 1:
            XORencode();
        elif option == 2:
            XORdecode();
        elif option == 0:
            print("\nThank you for using this program");
            exit()
        else:
            print("Invalid option, choose from given options");
# User selects a choice, the if statements pick it up and activate the relevant funciton
# If user selects 0, exit the program
# Else, user input is incorrect, make them choose again.
