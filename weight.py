# Present program / Ask the user if wants to continue.
startProgram = input("Welcome to the Weight Measure! Here you can see if your body weight is healthy according to your height. Do you want to continue (Y/n): ")

# Request and measure of name, height and weight.
def weight_measure():
	userName = str(input("Please, enter your name: "))
	userHeight = float(input("Hello " + str(userName) + "! Enter your current height in meters: "))
	userWeight = int(input("We're almost done, enter your current weight in kilograms: "))

	# Confirm if the user's data is right.
	confirmation = input("Please confirm if the following information is correct: \nYour name is " + str(userName)+ ".\nYour height is " + str(userHeight) + "m. \nYour weight is " + str(userWeight) + "kg. \nIs this information right? (Y/n).")

	if confirmation == "Y":
		# Measure the weight of the user and see if is healthy according to the BMI measure protocol.
		BMI = float(userWeight/userHeight ** 2)
		# See if the BMI of the user is healthy.
		if BMI < 18.5:
			print("Your current BMI is " + str(BMI) + ", you're consider as a person with a insufficient weight.")
		elif BMI >= 18.4 and BMI < 24.9:
			print("Your current BMI is " + str(BMI) + ", you're consider as a person with a healthy weight.")
		elif BMI >= 25.0 and BMI < 29.9:
			print("Your current BMI is " + str(BMI) + ", you're consider as a person with overweight.")
		elif BMI >= 30.0:
			print("Your current BMI is " + str(BMI) + ", you're consider as a person with obesity.")

	else:
		print("Ok, try it again!")

# Continue with the program according to the user's choice.
if startProgram == "Y":
	weight_measure()
elif startProgram == "n":
	print("Ok, come back whenever you want!")
else:
	print("Please, just answer with 'Yes' (Y) or 'No' (n).")