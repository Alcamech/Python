import math 

def add():
    print("Enter the two numbers to Add")
    A= int(input("Enter A:"))
    B= int(input("Enter B:"))
    return A + B

def sub():
    print("Enter the two numbers to subtract")
    A= int(input("Enter A:"))
    B= int(input("Enter B:"))
    return A - B

def mul():
    print("Enter the two numbers to multiply")
    A= int(input("Enter A:"))
    B= int(input("Enter B:"))
    return A * B

def div():
    print("Enter the two numbers to divide.")
    A= float(input("Enter A:"))
    B= float(input("Enter B:"))
    return A / B

def Mod():
    print("Enter the two numbers to get the remainder")
    A= int(input("Enter A:"))
    B= int(input("Enter B:"))
    return A % B 
def Exp():
    print("Enter the first number as your exponential base and the second number  as your exponent.")
    A= int(input("Enter A:"))
    B= int(input("Enter B:"))
    return A ** B
def Sqrt():
    print("Enter a number to obtain its Square Root")
    x= int(input("Enter X:"))
    return math.sqrt(x) 

print("Caculator")
print("---------------------------------------------------------------")

print("1: ADDITION")
print("2: SUBTRACTION")
print("3: MULTIPLICATION")
print("4: DIVISION")
print("5: MODULUS[remainder]") 
print("6: EXPONENT")
print("7: SQUARE ROOT")
print("0: QUIT")

print("---------------------------------------------------------------")
print("Please which form of mathematics you wish to use.")

while True:

    CHOICE = int(input("ENTER THE CORRESPONDING NUMBER FOR A CALCULATION.")) 

    if CHOICE == 1: 
        print("ADDING TWO NUMBERS:")
        print (add())

    elif CHOICE == 2:
        print("SUBTRACTING TWO NUMBERS")
        print (sub())

    elif CHOICE == 3:
        print("MULTIPLYING TWO NUMBERS")
        print (mul())

    elif CHOICE == 4:
        print("DIVIDING TWO NUMBERS")
        print (div())
	
    elif CHOICE == 5:
        print("GETTING THE REMAINDER")
        print (Mod())

    elif CHOICE == 6:
	print("CALCULATING..")
	print(Exp())

    elif CHOICE == 7:
	print("GETTING THE SQUARE ROOT")
	print(Sqrt())

    elif CHOICE == 0:
        print("GoodBye!")
        exit()
    else:
        print("The value Enter value from 1-4")
