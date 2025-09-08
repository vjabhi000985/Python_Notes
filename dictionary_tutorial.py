# Dictionary are unordered collections of items. They store the data in key-value pairs. Keys must be unique and immutable (strings, tuples or numbers), while values can be of any type. 

# Creating dictionaries
# empty_dict = {}

# print(type(empty_dict))

# using dict() method
# empty_dict = dict()

# student = {
#   "name" : "Abhi",
#   "age" : 25,
#   "grade" : 9.81
# }

# print(student)

# Single key is always used. 
student = {
  "name" : "Abhi",
  "age" : 25,
  "grade" : 9.81
}

# print(student)

# Accessing Dictionary elements
# print(student['name'])
# print(student['grade'])
# print(student['age'])

# Accessing elements using get()

# print(student.get('grade'))
# print(student.get('number','Not available'))

# Modifying dictionary elements. 
# Dictionary are mutable, so we can add, remove and update elements. 
# Updated value of the key
# student['age'] = 18 

# print(student)

# Added a new key and value
# student['address'] = 'India'
# print(student)

# Delete the key and value pair 
# del student['address']
# print(student)


# Most Important Dictionary Methods
# Get all the keys
# keys = student.keys()
# print(keys)

# Get all the values
# values = student.values()
# print(values)

# Get all key value pairs
# items = student.items()
# print(items)

# Shallow copy
# student_copy = student 

# print(student)
# print(student_copy)

# student['name'] = "Alya"

# print(student)
# print(student_copy)

# Shallow copy - Change in original dictionary doesn't affect the copied dictionary. It will have a reference at the new memory location. 

# student_new = student.copy()

# print(student)
# print(student_new)

# student['name'] = 'Alya'
# print(student)
# print(student_new)


# Iteration over dictionaries
## You can use loops to iterate over dictionaries : keys, values, or items. 

## Iterating over keys 
# for keys in student.keys():
#   print(keys)

## Iterating over values 
# for values in student.values():
#   print(values)

## Iterating over key value pairs
# for key, value in student.items():
#   print(f"{key} : {value}")

# Nested dictionaries. 
## Dictionary inside dictionary. 

# students = {
#   "student_1" : {"name":"Abhi", "age":25, "grade":"A"},
#   "student_2" : {"name":"Alya","age":17, "grade":"A+"}
# } 

# print(students)

## Access Nested Dictionary elements
# print(students['student_2']['name'])
# print(students['student_2']['age'])

## Iterating over nested dictionary 
# for student_id,student_info in students.items():
#   print(f"{student_id} : {student_info}")

#   for key,value in student_info.items():
#     print(f"{key}:{value}")


# Dictionary comprehension

# squares = {x : x**2 for x in range(5)}
# print(squares)

## Conditional dictionary comprehension
# evens = {x : x**2 for x in range(1,11) if x % 2 == 0}
# print(evens)

# Practical examples
## Use a dictionary to count the frequency of elements in list. 

numbers = [1,2,2,3,3,3,4,4,4,4,5,5,4]
# frequency = {}

# for number in numbers:
#   if number in frequency:
#     frequency[number] += 1
#   else:
#     frequency[number] = 1

# print(frequency)

# for number in numbers:
#   frequency[number] = frequency.get(number, 0) + 1

# print(frequency)

## We can achieve this using collections.Counter()
# 👉 Counter automatically counts how many times each number appears.
from collections import Counter
frequency = Counter(numbers)
# frequency = dict(Counter(numbers))

print(frequency)

# 👉 You can still access values like a normal dictionary.
print(frequency[4])

## Merge 2 dictionaries into one. 
# dict1 = {"a":1,"b":2}
# dict2 = {"b":3,"c":4}

# merged_dict = {**dict1,**dict2}
# print(merged_dict)