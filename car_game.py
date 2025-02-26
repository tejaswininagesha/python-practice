command = ""
started = False
while True:
	command = input("Enter command >>> ").lower()
	if command == "start":
		if started:
			print("Car already started")
		else:
			started = True
			print("Car started.")
	elif command == "stop":
		if not started:
			print("Car already stopped")
		else:
			started = False
			print("Car stopped.")
	elif command == "help":
		print(" Start: Start the car\n stop: Stop the Car\n Quit: To Quit")
	elif command == "quit":
		break
	else:
		print("Please enter valid command..!!")

