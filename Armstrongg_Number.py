num = int(input("Enter number: "))

digits = str(num)
power = len(digits)
total = sum(int(digit) ** power for digit in digits)

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")