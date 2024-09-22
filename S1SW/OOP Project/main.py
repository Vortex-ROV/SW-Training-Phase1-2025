def checkInt(value, func=None, *args):
	try:
		whatever_as_an_integer = int(value)
		print("That was an integer.")

	except ValueError:
		print("That is not an integer. Try again...")
		if args:
			func()

number_of_rovs = input("Please enter the number of ROVS: ")
checkInt(number_of_rovs)

for i in range(int(number_of_rovs)):
    print(f"Enter details for ROV {i+1}:")
    input("Choose type (1 - Exploration, 2 - Sampling, 3 - Maintenance): ")

number_of_missions = input("Enter the number of missions to complete: ")
checkInt(number_of_missions)