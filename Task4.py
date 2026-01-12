#Arethmatic
'''
a=int(input("Enter First number: "))
b=int(input("Enter second number: "))
print("Addition :",a+b)
print("Subtraction :",a-b)
print("Multiplication :",a*b)
print("Division :",a/b)
print("Module :",a%b)
'''

#Find sum of digit
num=int(input("Enter number "))
total=0

while num > 0:
    digit=num%10
    total+=digit
    num//=10

print("Sum of digits:",total)