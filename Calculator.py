#Calculatoar code
n1=int(input("Entetr first number: "))
n2=int(input("Enter second number: "))

print("*****Choose Operations*****")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

ch=input("Choose input 1/2/3/4: ")
if ch == '1':
    print("Addition: ",n1+n2)
elif ch == '2':
    print("Subtraction: ",n1+n2)
elif ch == '3':
    print("Multiplication: ",n1*n2)
elif ch == '4':
    if ch != 0:
        print("Division: ",n1/n2)
    else:
        print("Error: Number Divisible by zero is not allowed")
else:
    print("Invalid Choise")

