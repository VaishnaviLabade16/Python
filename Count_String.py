#Calculate Each Charecter in string\
'''
text = input("Enter a string: ")

for ch in set(text):
    print(ch, ":", text.count(ch))
'''

text = input("Enter a string: ")

count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1

print(count)
