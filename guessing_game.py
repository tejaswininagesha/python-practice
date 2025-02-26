
# Guessing Number

guessed_num = 9
trials = 3

while trials > 0:
	guess = int(input("NUMBER: "))
	if guess == guessed_num:
		print("You won.!")
		break
	else:
		trials -= 1
		if trials > 0:
			print(f"Try Again! You have {trials} attempts left !")
		else:
			print(f"You failed! The correct number is: {guessed_num}")


