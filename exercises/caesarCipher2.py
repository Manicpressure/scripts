import string

def createShift(n):
    encoding = {}
    decoding = {}
    alphabetSize = len(string.ascii_uppercase);
    for i in range(alphabetSize):
        letter = string.ascii_uppercase[i];
        subLetter = string.ascii_uppercase[(i+n) % alphabetSize];
        encoding[letter] = subLetter;
        decoding[subLetter] = letter;
    return encoding, decoding;

def encode(message, subst):
    return "".join(subst.get(x, x) for x in message);


def decode(message, subst):
    return encode(message, subst);

def printableSubstitution(subst):
    mapping = sorted(subst.items());

    alphabetLine = " ".join(letter for letter, _ in mapping);
    cipherLine = " ".join(subLetter for _, subLetter in mapping);
    return "{}\n{}".format(alphabetLine, cipherLine);

if __name__ == "__main__":
    n = 1;
    encoding, decoding = createShift(n);
    while True:
        print("\nShift Encoder Decoder");
        print("------------------------");
        print("\tCurrent Shift : {}\n".format(n));
        print("\t1. Print Encoding/Decoding tables.");
        print("\t2. Encode Message.");
        print("\t3. Decode Message.");
        print("\t4. Change Shift.");
        print("\t5. Quit.\n");
        choice = input(">> ");
        print()

        if choice == '1':
            print("Encoding Table:");
            print(printableSubstitution(encoding));
            print("Decoding Table:");
            print(printableSubstitution(decoding));

        elif choice == '2':
            message = input("\nMessage to encode: ");
            print("Encoded Message: {}".format(encode(message.upper(), encoding)));

        elif choice == '3':
            message = input("\nMessage to decode: ");
            print("Decoded Message: {}".format(encode(message.upper(), decoding)));

        elif choice == '4':
            newShift = input("\nNew shift (currently {}): ".format(n));
            try:
                newShift = int(newShift);
                if newShift < 1:
                    raise Exception("Shift must be greater than 0");
            except ValueError:
                print("Shift {} is not a valid number.".format(newShift));
            else:
                n = newShift;
                encoding, decoding = createShift(n);

        elif choice == '5':
            print("Terminating program.\n");
            break;

        else:
            print("Unknown option {}.".format(choice));
