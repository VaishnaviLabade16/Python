text = input("Enter Message: ")
shift = 3

result = ""

for char in text:
    if char.isalpha():
        base = 65 if char.isupper() else 97
        result += chr((ord(char)-base+shift)%26+base)
    else:
        result += char

print("Encrypted:", result)