from rov import RovType
from rov import ExplorationROV, SamplingROV, MaintenanceROV
from marine_mission_control_system import MarineMissionControlSystem


def choose_rovs_num():
    while True:
        try:
            rovs_num = int(input("Please enter the number of ROVs: "))
            if rovs_num > 0:
                return rovs_num
            else:
                print("Number of ROVs must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def choose_rov_type(rov_idx):
    while True:
        print(f"\nEnter details for ROV {rov_idx}:")
        try:
            rov_type = int(input("\tChoose type (1 - Exploration, 2 - Sampling, 3 - Maintenance): "))
            if rov_type == 1:
                return RovType.EXPLORATION
            elif rov_type == 2:
                return RovType.SAMPLING
            elif rov_type == 3:
                return RovType.MAINTENANCE
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_missions_num():
    while True:
        try:
            missions_num = int(input("\nPlease enter the number of missions to complete: "))
            if missions_num > 0:
                return missions_num
            else:
                print("Number of missions must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Welcome to the Underwater ROV Fleet Management Simulator!\n")

    rovs_num = choose_rovs_num()
    rov_fleet = []
    available_rov_types = set()

    for i in range(1, rovs_num + 1):
        rov_type = choose_rov_type(i)
        if rov_type == RovType.EXPLORATION:
            rov_fleet.append(ExplorationROV(i))
            available_rov_types.add(RovType.EXPLORATION)
        elif rov_type == RovType.SAMPLING:
            rov_fleet.append(SamplingROV(i))
            available_rov_types.add(RovType.SAMPLING)
        elif rov_type == RovType.MAINTENANCE:
            rov_fleet.append(MaintenanceROV(i))
            available_rov_types.add(RovType.MAINTENANCE)

    missions_num = get_missions_num()

    print("\nSimulation starting...\n")

    control_system = MarineMissionControlSystem(rov_fleet, missions_num, available_rov_types)
    control_system.run_simulation()


if __name__ == "__main__":
    main()
