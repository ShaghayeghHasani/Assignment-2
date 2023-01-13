name = input("Name:")
Ln = input("Last name:")
g1= float(input("Your Math score:"))
g2= float(input("Your Biology score:"))
g3= float(input ("Your Literature score:"))

average = (g1+g2+g3) / 3
if 20>= average and average >=17 :
    result= "Great!"
if average < 17 and average >= 12:
    result= "Normal"
if average < 12 and average >= 0:
    result="Fail"

print(name,Ln, " Your Average status is " , result, ".", "Would you like to see your average score?")
answer= str(input(""))
if answer =="yes" :
    print("Your average score is: ", average)
if answer== "no" :
    print("Okay. Have a nice day.")
