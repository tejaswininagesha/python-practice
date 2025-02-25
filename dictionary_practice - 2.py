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

