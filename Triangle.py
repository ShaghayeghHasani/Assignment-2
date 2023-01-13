a = float(input("First number:"))
b = float(input("Second number:"))
c = float(input("Third number:"))

if a+b <= c or a+c <= b or c+b <= a :
    result= "Sorry, we can't form a triangle with these numbers."
else:
    result= "Yes! Now we can form a Triangle."

print (result)