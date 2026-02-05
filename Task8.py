# Exercise 1: Print first 10 natural numbers using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Calculate sum of all numbers from 1 to a given number
n = int(input("Enter a number: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("Sum =", sum)

#	Exercise 3: Display numbers from a list using a loop
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)

#	Exercise 4: Count the total number of digits in a number
num = int(input("Enter a number: "))
count = 0

while num != 0:
    count += 1
    num //= 10

print("Total digits:", count)

#	Exercise 5: Print list in reverse order using a loop
numbers = [10, 20, 30, 40, 50]
i = len(numbers) - 1

while i >= 0:
    print(numbers[i])
    i -= 1

#	Exercise 6: Display numbers from -10 to -1 using for loop
for i in range(-10, 0):
    print(i)

#	Exercise 7: Display a message “Done” after the successful execution of the for loop
for i in range(1, 6):
    print(i)

print("Done")

#	Exercise 8: Print all prime numbers within a range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#	Exercise 9: Display Fibonacci series up to 10 terms
a = 0
b = 1

for i in range(10):
    print(a)
    a, b = b, a + b

#	Exercise 10: Find the factorial of a given number
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)

#	Exercise 11: Print elements from a given list present at odd index positions
numbers = [10, 20, 30, 40, 50, 60]

for i in range(1, len(numbers), 2):
    print(numbers[i])

#	Exercise 12: Calculate the cube of all numbers from 1 to a given number
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("Cube of", i, "is", i ** 3)

#	Exercise 13: Find the sum of a series of a number up to n terms
n = int(input("Enter number of terms: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum of the series =", sum)

#	Exercise 14: Print the alternate numbers pattern
n = int(input("Enter a number: "))

for i in range(1, n + 1, 2):
    print(i)

#	Exercise 15: Find largest and smallest digit in a number
num = int(input("Enter a number: "))

largest = 0
smallest = 9

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    num //= 10

print("Largest digit:", largest)
print("Smallest digit:", smallest)
