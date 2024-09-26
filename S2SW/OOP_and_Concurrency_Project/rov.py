import time
import random
from enum import Enum
from mission import MissionStatus


class RovType(Enum):
    EXPLORATION = 1
    SAMPLING = 2
    MAINTENANCE = 3


class RovStatus(Enum):
    IDLE = 1
    IN_MISSION = 2
    MALFUNCTION = 3


class ROV:
    def __init__(self, rov_id: int, rov_type: RovType):
        self.rov_id = rov_id
        self.rov_type = rov_type
        self.status = RovStatus.IDLE
        self.battery_level = 100
        self.position = (0, 0)
        self.mission_queue = []
        self.data_storage = []
        self.current_mission = None

    def receive_mission(self, mission):
        self.mission_queue.append(mission)
        print(f"ROV {self.rov_id} ({mission.mission_type.name}) assigned mission {mission.mission_id}")

    def execute_mission(self):
        if self.battery_level <= 10:
            self._handle_low_battery()
            return

        if self.mission_queue:
            mission = self.mission_queue.pop(0)
            mission.status = MissionStatus.IN_PROGRESS  # Mark as in progress
            self.current_mission = mission
            self.status = RovStatus.IN_MISSION
            print(f"ROV {self.rov_id} is executing Mission {mission.mission_id}")

            self.navigate_to(mission.target_location)
            self._handle_potential_malfunction()
            self.collect_data()

            mission.status = MissionStatus.COMPLETED  # Mark as completed
            self.status = RovStatus.IDLE
            self.battery_level -= 10
            print(f"ROV {self.rov_id} completed Mission {mission.mission_id}")
        else:
            print(f"ROV {self.rov_id} has no missions to execute.")

    def send_status_update(self):
        print(f"\n--- ROV {self.rov_id} STATUS UPDATE ---")
        print(f"Status: {self.status.name}")
        print(f"Battery level: {self.battery_level}%")
        print(f"Position: {self.position}")
        print(f"Data storage: {len(self.data_storage)} samples")
        if self.current_mission:
            print(f"Current mission: {self.current_mission['mission_id']}")
        print(f"Remaining missions: {len(self.mission_queue)}")
        print()

    def collect_data(self):
        print(f"\n--- ROV {self.rov_id} COLLECTING DATA ---")
        print(f"Collecting data at location: {self.position}")
        for _ in range(2):
            time.sleep(1)
            print("Collecting...")
        self.data_storage.append("Sample Data")
        print("Data collection complete!")

    def navigate_to(self, target_position):
        print(f"\nROV {self.rov_id} navigating from {self.position} to {target_position}...")
        for _ in range(3):
            time.sleep(1)
            print("Navigating...")
        self.position = target_position
        print(f"ROV {self.rov_id} has arrived at {target_position}")

    def _handle_low_battery(self):
        print(f"\nROV {self.rov_id} battery critically low. Returning to base.")
        self._return_to_base()
        self._recharge_battery()

    def _handle_potential_malfunction(self):
        malfunctions = ['Low Battery', 'Communication Failure', 'Sensor Malfunction',
                        'Leakage in Watertight Compartments', 'Navigation System Failure', None]
        malfunction = random.choice(malfunctions)

        if malfunction:
            print(f"\n--- !!! ROV {self.rov_id} MALFUNCTION DETECTED: {malfunction} !!! ---")
            if malfunction == 'Leakage in Watertight Compartments':
                self._emergency_shutdown()
            elif malfunction in ['Navigation System Failure', 'Communication Failure', 'Sensor Malfunction']:
                if not self._attempt_fix(malfunction):
                    self._return_to_base()
                    self._repair(malfunction)
            elif malfunction == 'Low Battery':
                self._handle_low_battery()

    def _emergency_shutdown(self):
        print(f"ROV {self.rov_id} initiating emergency shutdown.")
        for i in range(3, 0, -1):
            print(f"Shutting down in {i}...")
            time.sleep(1)
        print("SHUT DOWN COMPLETE")
        self.status = RovStatus.MALFUNCTION
        self._return_to_base()
        self._repair("Leakage in Watertight Compartments")

    def _attempt_fix(self, malfunction):
        print(f"Attempting to fix {malfunction}...")
        for _ in range(3):
            time.sleep(0.25)
            print("Attempting fix...")
        success = random.choice([True, False])
        if success:
            print(f"ROV {self.rov_id} successfully fixed the {malfunction}.")
        else:
            print(f"ROV {self.rov_id} failed to fix the {malfunction}.")
        return success

    def _return_to_base(self):
        print(f"ROV {self.rov_id} returning to base...")
        for _ in range(3):
            time.sleep(0.5)
            print("Returning...")
        self.navigate_to((0, 0))
        print(f"ROV {self.rov_id} has returned to base at {self.position}.")

    def _repair(self, malfunction):
        print(f"--- ROV {self.rov_id} MAINTENANCE ---")
        print("Initiating repair process...")
        for _ in range(3):
            time.sleep(0.5)
            print("Repairing...")
        print(f"ROV {self.rov_id} has been repaired. {malfunction} fixed.")
        self.status = RovStatus.IDLE

    def _recharge_battery(self):
        print(f"ROV {self.rov_id} recharging battery...")
        for _ in range(3):
            time.sleep(0.5)
            print("Charging...")
        self.battery_level = 100
        print(f"ROV {self.rov_id} battery fully recharged to {self.battery_level}%.")


class ExplorationROV(ROV):
    def __init__(self, rov_id):
        super().__init__(rov_id, RovType.EXPLORATION)

    def map_area(self, area_coordinates):
        print(f"ROV {self.rov_id} , is mapping the area defined by {area_coordinates}.")
        time.sleep(2)
        print(f"ROV {self.rov_id} , completed mapping of the area.")
        self.data_storage.append(f"Map Data for area {area_coordinates}")


class SamplingROV(ROV):
    def __init__(self, rov_id):
        super().__init__(rov_id, RovType.SAMPLING)

    def collect_sample(self, sample_type):
        print(f"ROV {self.rov_id} is collecting a {sample_type} sample at location {self.position}.")
        time.sleep(2)
        sample_data = f"{sample_type} Sample from {self.position}"
        print(f"ROV {self.rov_id} has collected the {sample_type} sample.")
        self.data_storage.append(sample_data)


class MaintenanceROV(ROV):
    def __init__(self, rov_id):
        super().__init__(rov_id, RovType.MAINTENANCE)

    def perform_maintenance(self, equipment_id):
        print(f"ROV {self.rov_id} , is performing maintenance on equipment {equipment_id}.")
        time.sleep(2)
        print(f"ROV {self.rov_id} , completed maintenance on equipment {equipment_id}.")
