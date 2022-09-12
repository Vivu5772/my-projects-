


print("welcome to calculator")
num1= input("chosse operation")
num2= int(input("number1"))
num3= int(input("number2"))
a= "made by vivu"
if num1=="+":
    print(num2 + num3)
    print("made by vivu")
elif num1=="*":
    print(num2 * num3)
    print(a)
elif num1=="/":
    print(num2 / num3)
    print(a)
elif num1=="-":
    print(num2 - num3)
    print(a)
else:
    print("no other operation available except +,-,*,/")
    print(a)
print("thank you for using our calculator")

