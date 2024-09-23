from rov import ROV, ExplorationROV, SamplingROV, MaintenanceROV

def checkInt(value):
    return value.isnumeric()

def get_valid_input(user_input):
    state = False
    while not state:
        number = input(user_input)
        state = checkInt(number)
        if not state:
            print("Invalid input, Please enter a valid integer.")
    return int(number)

number_of_rovs = get_valid_input("Please enter the number of ROVS: ")
print(f"Number of ROVs: {number_of_rovs}")

rovs = {}  # Use a dictionary to store ROV instances

for i in range(number_of_rovs):
    print(f"Enter details for ROV {i+1}:")
    rov_type = input("Choose type (1 - Exploration, 2 - Sampling, 3 - Maintenance): ")
    
    match rov_type:
        case "1":
            rovs[f"rov_{i+1}"] = ExplorationROV()
        case "2":
            rovs[f"rov_{i+1}"] = SamplingROV()
        case "3":
            rovs[f"rov_{i+1}"] = MaintenanceROV()
        case _:
            print("Invalid type selected, Defaulting to inactive ROV")
            rovs[f"rov_{i+1}"] = ROV("Inactive")

number_of_missions = get_valid_input("Enter the number of missions to complete: ")
print(f"Number of missions: {number_of_missions}")

# Display all created ROVs
for key, rov in rovs.items():
    print(f"{key}: ID = {rov.rov_id}, Type = {rov.type}, Status = {rov.status}")