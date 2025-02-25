name = input("Enter your name? ").upper()
color = input("Your fav color! ").title()

print(name + ' likes ' + color + ' color ')

# conditional statements

house_price =  1000000
good_credits = False

if good_credits:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price

print(f"Your down payment is ${down_payment}")

# conditional statements 2

name = input("Enter name:\n")
length_name = len(name)
print(f"Your name as {length_name} characters\n")

if length_name < 3:
    print("Name must be atleast 3 characters..!")
elif length_name > 50:
     print("Name must not be greater than 50characters..!")
else:
    print("Name looks good.!!")

# weight checking
try:
	weight = int(input("Enter your weight: "))
	weight_unit = input("(L)bs or (K)g: ").upper()

	kg_in_pounds = "{:.2f}".format(weight * 2.20)
	pounds_in_kg = (weight * 0.45)

	if weight <= 0:
		print("Please enter valid numbers (Negative numbers not valid).")
	elif weight_unit == "L":
		print(f"Your weight is {pounds_in_kg} kilos.")
	elif weight_unit == "K":
		print(f"Your weight is {kg_in_pounds} pounds.")
	else:
		print("Please enter correct unit.")

except ValueError:
	print("!!.Please enter valid weight in numbers.!!")

# using loops
while True:
	try:
		weight = float(input("Enter your weight: "))

		if weight <= 0:
			print("Please enter a valid weight (greater than 0).")
			continue

		weight_unit = input("(L)bs or (K)g: ").strip().upper()

		if weight_unit == "L":
			pounds_in_kg = weight * 0.45
			print(f"Your weight is {pounds_in_kg:.2f} kilograms.")
		elif weight_unit == "K":
			kg_in_pounds = weight * 2.20462
			print(f"Your weight is {kg_in_pounds:.2f} pounds.")
		else:
			print("Please enter a correct unit (L or K).")
			continue

		break

	except ValueError:
		print("Please enter a valid weight in numbers!")








