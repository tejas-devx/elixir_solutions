# 1. Create a list of 5 numbers and print the sum of all elements
numbers = [10, 20, 30, 40, 50]

total = sum(numbers)

print("Sum of elements:", total)

# 2. Find the largest and smallest number in a list
numbers = [12, 45, 7, 89, 23]

largest = max(numbers)
smallest = min(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)

# 3. Remove duplicate elements from a list
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print("List after removing duplicates:", unique_numbers)

# 4. Create a tuple and access elements using indexing
colors = ("Red", "Blue", "Green", "Yellow")

print("First element:", colors[0])
print("Second element:", colors[1])

# 5. Convert a list into a tuple
fruits = ["Apple", "Orange", "Mango"]

fruit_tuple = tuple(fruits)

print("Tuple:", fruit_tuple)

# 6. Create a dictionary with student name and marks,
# then print all keys and values

student = {
    "Tejas": 85,
    "Rahul": 90,
    "Anu": 78
}

print("Keys:", student.keys())
print("Values:", student.values())

# 7. Add a new key-value pair to a dictionary
student = {
    "Tejas": 85,
    "Rahul": 90
}

student["Anu"] = 78

print(student)

# 8. Check if a key exists in a dictionary
student = {
    "Tejas": 85,
    "Rahul": 90
}

key = "Tejas"

if key in student:
    print("Key exists")
else:
    print("Key does not exist")

# 9. Create a set and demonstrate union and intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

# 10. Count how many times a value appears in a list
numbers = [1, 2, 3, 2, 4, 2, 5]

count = numbers.count(2)

print("2 appears", count, "times")