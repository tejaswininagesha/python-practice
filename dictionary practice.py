# Dictionary
capitals = {
	"France": "Paris",
	"Germany": "Berlin"
}
print(capitals["Germany"])

# Nested list in Dictionary
travel_logs = {
	"France": ["paris", "lille", "dijon"],
	"Germany": ["Stuttgart","Berlin"],
}
print(travel_logs["France"][1])


nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])

#student grades
student_scores = {
    "Harry": 92,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 85,
    "Neville": 66,
}

# Creating an empty dictionary for student grades
student_grades = {}

# Converting scores to grades
for student, score in student_scores.items():
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Print the final student_grades dictionary
print(student_grades)


#How to add next key, values

starting_dictionary = {
    "a": 9,
    "b": 8,
}

starting_dictionary["c"] = 7

print(starting_dictionary)

# print the word "Steak" but not as list

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])


# use of max and min in dictionary
fruits = {
  "Apple": 8023, "Orange": 5986,
  "Pineapple": 313, "Apple_5": 920,
  "Apple_2": 9300, "Orange_2": 4816,
  "Pineapple_2": 3925, "Apple_3": 9230
}
max_fruits = max(fruits, key=fruits.get)
min_fruits = min(fruits, key=fruits.get)

print(f"Maximum no of fruits are in '{max_fruits}'")
print(f"Minimum no of fruits are in '{min_fruits}'")
