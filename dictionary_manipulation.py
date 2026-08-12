# ==============================================================================
# Python Fundamentals
# Topic       : Dictionary Manipulation
# By          : Pranay Savdekar
# Date        : 12/08/2026
# ==============================================================================


# ==============================================================================
# Problem 1: Create a dictionary with 5 key-value pairs and print it
# ==============================================================================

student = {
    "name": "Drake",
    "age": 21,
    "course": "Data Science",
    "city": "Indore",
    "year": 4
}

print(student)


# ==============================================================================
# Problem 2: Access a value from a dictionary using its key
# ==============================================================================

student = {
    "name": "Drake",
    "age": 21
}

print(student["name"])


# ==============================================================================
# Problem 3: Add a new key-value pair to an existing dictionary
# ==============================================================================

student = {
    "name": "Drake",
    "age": 21
}

student["city"] = "Indore"

print(student)



# ==============================================================================
# Problem 4: Update the value of an existing key
# ==============================================================================

student = {
    "name": "Drakey",
    "age": 21
}

student["age"] = 22

print(student)



# ==============================================================================
# Problem 5: Print all keys and values of a dictionary using a for loop
# ==============================================================================

student = {
    "name": "Drake",
    "age": 21,
    "city": "Indore"
}

for key, value in student.items():
    print(key, value)



# ==============================================================================
# Problem 6: Check whether a given key exists in a dictionary
# ==============================================================================

student = {
    "name": "Drake",
    "age": 21,
    "city": "Indore"
}

if "age" in student:
    print("Key exists")
else:
    print("Key does not exist")


# ==============================================================================
# Problem 7: Find the key having the maximum value
# ==============================================================================

marks = {
    "Maths": 85,
    "Python": 95,
    "SQL": 90
}

max_key = list(marks.keys())[0]

for key in marks:
    if marks[key] > marks[max_key]:
        max_key = key

print(max_key)


# ==============================================================================
# Problem 8: Count the frequency of each character in a string
# ==============================================================================

string = "banana"
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)



# ==============================================================================
# Problem 9: Remove a key-value pair from a dictionary using pop()
# ==============================================================================

student = {
    "name": "Drake",
    "age": 21,
    "city": "Indore"
}

student.pop("age")

print(student)

# ==============================================================================
# Problem 10: Find the sum of all values in a dictionary
# ==============================================================================

nums = {
    "a": 10,
    "b": 20,
    "c": 30
}

total = 0

for value in nums.values():
    total += value

print(total)

# ==============================================================================
# Problem 11: Merge two dictionaries into a single dictionary
# Input: {"a": 1, "b": 2} and {"c": 3, "d": 4}
# Output: {"a": 1, "b": 2, "c": 3, "d": 4}
# ==============================================================================

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

result = dict1.copy()
result.update(dict2)

print(result)

# ==============================================================================
# Problem 12: Create a dictionary from two lists
# ==============================================================================

keys = ["a", "b", "c"]
values = [10, 20, 30]

result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)

# ==============================================================================
# Problem 13: Count how many subjects have marks greater than 80
# ==============================================================================

student = {
    "name": "Drake",
    "marks": {
        "Python": 90,
        "SQL": 75,
        "Excel": 80,
        "Statistics": 95
    }
}

count = 0

for marks in student["marks"].values():
    if marks > 80:
        count += 1

print("Subjects above 80:", count)



# ==============================================================================
# Problem 14: Find the average marks from a nested dictionary
# ==============================================================================

student = {
    "name": "Drake",
    "marks": {
        "Python": 90,
        "SQL": 75,
        "Excel": 80,
        "Statistics": 95
    }
}

total = 0
count = 0

for marks in student["marks"].values():
    total += marks
    count += 1

average = total / count
print("Average marks:", average)

# ==============================================================================