#The number theorem
#let c and d be positive integers which have no common factors.
#there exists integers a and b such that ac + bd = 1.
#what would be the algorithm to find the a's and b's
#to any variation of c's and d's?
#c and d provided by the user
#a and b to be provided by programmer in a list

def intro():
    print("""let c and d be positive integers which have no common factors.
    there exists integers a and b such that ac + bd = 1.""");
    print("Type in 'c' and 'd' and we will provide a list of a's and b's");
    return

def cdInput():
    conditional = False;
    while (conditional == False):
        try:
            c = int(input("Enter a positive integer 'c' :"));
            d = int(input("Enter a positive integer 'd' :"));
            if (c < 1) or (d < 1):
                print("Please enter a positive integer!");
            elif(c > 1) and (d > 1):
                conditional = True;
        except:
            print("Please enter a positive integer");
            continue
    return c, d;

def pair1(c, d):
    i = 1;
    while (i < (c * d)):
        if ((d * i) % c == 1):
            a1 = -1 * ((d * i) // c);
            b1 = (1 - (a1 * c)) / d;
            return int(a1), int(b1);
        else:
            i += 1;
            continue;
        elif (i = (c * d)):
            print("no solution");
            break

def pair2(c, d):
    i = 1;
    while (i < (c * d)):
        if ((c * i) % d == 1):
            b2 = -1 * ((c * i) // d);
            a2 = i;
            return int(a2), int(b2);
        else:
            i += 1;
            continue;
        elif (i = (c * d)):
            print("no solution");
            break

def conclusion(a1, a2, b1, b2, c, d):
    print("ac + bd = 1");
    print("First pair of a and b : a({}) * c({}) + b({}) * d({}) = 1".format(a1, c, b1, d));
    print("Second pair of a and b : a({}) * c({}) + b({}) * d({}) = 1".format(a2, c, b2, d));

def main():
    intro();
    c, d = cdInput();
    a1, b1 = pair1(c,d);
    a2, b2 = pair2(c,d);
    conclusion(a1, a2, b1, b2, c, d);

main()
