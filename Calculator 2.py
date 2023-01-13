import math
op = str(input("Which operation do you want to run?"))

if  op == "+" or "-" or "*" or "/" :
    a = float(input("Please enter your number: "))
if op == "+" :
    b = float(input("PLease enter a second number: "))
    result = a + b
if op == "-" :
    b = float(input("PLease enter a second number: "))
    result = a-b
if op == "*" :
    b = float(input("PLease enter a second number: "))
    result = a*b
if op == "/" :
    b = float(input("PLease enter a second number: "))
    if b == 0:
        result= "Error"
    else:
        result= a/b

if op == "radical" :
    result = math.sqrt(a)
if op == "factorial" :
    b = int(input("Your number should be an integer. If it is, repeat it; if not enter an integer :"))
    result = math.factorial(b)
if op == "sin" :
    result =math.sin(a)
if op == "cos" :
    result =math.cos(a)
if op == "tan" :
    result =math.tan(a)
if op == "cot" :
    result =math.cos(a) / math.sin(a)

print("Answer:" , result)