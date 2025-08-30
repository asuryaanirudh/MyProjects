#Simple Calculator

a = float(input ("Enter your first number: ") )
b = float (input ("Enter your second number: "))
#to get a valid operator
def operator():  
    o = input("What do you want to perform today? (+, -, *, /): ")

    if o in ["+", "-", "*", "/"]:
        return o   # this will return the valid operator to op
    else :
        print("Invalid operator, please try again!")
        return operator()   #  to send the user back to get valid operator

op = operator()

if op == "+":
    print("The Sum of the two numbers is:", a + b)
elif op == "-":
    print("The Diff of the two numbers is:", a-b)
elif op == "*":
    print("The multiplication of two numbers is:", a * b)
elif op == "/":
    if b !=0:
        (print ("The division of the two numbers is:",a/b))
    else:
        (print ("Divsion by Zero is not possible "))

print ("Thank you for using this Calculator")