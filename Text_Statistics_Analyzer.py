text = input("Enter text: ")

characters = len(text)
words = len(text.split())
lines = len(text.splitlines())
vowels = sum(1 for ch in text.lower() if ch in "aeiou")

print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)
print("Vowels:", vowels)