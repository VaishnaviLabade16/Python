students = [
    ("Ram", 80),
    ("Aman", 95),
    ("Shyam", 80)
]

result = sorted(students, key=lambda x: (x[1], x[0]))

print(result)