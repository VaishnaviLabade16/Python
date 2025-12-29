# Dictionary 
'''student = {
    "name": "Rahul",
    "age": 15,
    "marks": 90
}
print(student)'''

#update 
'''student["age"]=17 #update existing value
student["grade"]="A" #add new key
#print(student)'''

#Removing Elements
'''student.pop("age")        # Removes key "age"
student.popitem()         # Removes last inserted item
del student["marks"]      # Remove specific key
student.clear()           # Remove all items
print(student)'''

#Dictionary Operations
'''student = {"name": "Rahul", "age": 15}
teacher = {"name": "Amit", "subject": "Math"}
# Merge dictionaries (Python 3.9+)
all_people = student | teacher
print(all_people)'''

#Iterating through Dictionary
student = {"name": "Rahul", "age": 15, "marks": 90}
for key in student:
    print(key, ":", student[key])
