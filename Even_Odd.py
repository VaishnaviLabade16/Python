# Even Odd
'''
n=int(input("enter a number: "))
for i in range(1,n+1):
    if i % 2 == 0:
        print(i," Even")
    else:
        print(i," Odd")
'''
#Even Odd Using Def
def check_even_odd(num):
    if num % 2 == 0:
        print(num,"is Even")
    else:
        print(num,"is Odd")
check_even_odd(7)