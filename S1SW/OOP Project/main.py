from rov import ROV, ExplorationROV, SamplingROV, MaintenanceROV

def get_valid_int(promt):
	state = False
	while not state:
		number = input(promt)
		state = number.isnumeric()
		if not state:
			print("Invalid input! Please enter a valid integer.")
	return int(number)

def initialize_rovs():
	for i in range(number_of_rovs):
		print(f"Enter details for ROV {i+1}:")
		rov_type = input("Choose type (1 - Exploration, 2 - Sampling, 3 - Maintenance): ")
		match rov_type:
			case "1":
				rovs[i] = ExplorationROV()
			case "2":
				rovs[i] = SamplingROV()
			case "3":
				rovs[i] = MaintenanceROV()
			case _:
				print("Invalid type selected! Try again.")

def display_all_rovs():
	# Display all created ROVs
	for key, rov in rovs.items():
		print(f"{key+1}: ID = {rov.rov_id} | Type = {rov.type} | Status = {rov.status}")

def assign_missions():
	for _ in range(number_of_missions):
		display_all_rovs()
		assigned_rov = get_valid_int("Choose ROV to assign mission: ")
		assigned_mission = input(f"Input mission to assign ROV[{assigned_rov}]:")
		rovs[assigned_rov-1].receive_mission(assigned_mission)
		print(f"ROV[{assigned_rov}] mission queue: ", rovs[assigned_rov-1].mission_queue)

def execute_missions():
	for key, rov in rovs.items():
		if rov.mission_queue:
			rov.execute_mission()

if __name__ == '__main__':
	rovs = {}
	number_of_rovs = get_valid_int("Please enter the number of ROVS: ")

	initialize_rovs()
	display_all_rovs()

	number_of_missions = get_valid_int("Enter the number of missions to complete: ")
	assign_missions()

	execute_missions()