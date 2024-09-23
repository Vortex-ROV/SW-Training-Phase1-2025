import uuid

# **Additional Requirements:**
# - Initialize ROVs based on user input from the CLI.
# - Assign unique IDs automatically.

def generate_id():
    return int(uuid.uuid4())

class ROV:
    def __init__(self, rov_type, status="inactive", battery_level=100, position=(0, 0)):
        self.rov_id = f"rov_{generate_id()}"
        self.type = rov_type
        self.status = status
        self.battery_level = battery_level
        self.position = position
        # self.mission_queue
        # self.data_storage

    def receive_mission(self, mission):
        pass

    def execute_mission(self):
        pass

    def send_status_update(self):
        pass

    def collect_data(self):
        pass

    def navigate_to(self, target_position):
        pass

    def check_battery(self):
        pass

    def handle_malfunction(self):
        pass

class ExplorationROV(ROV):
    def __init__(self, status="inactive", battery_level=100, position=(0, 0)):
        super().__init__("Exploration", status, battery_level, position)

    def map_area(self, area_coordinates):
        pass

class SamplingROV(ROV):
    # **Additional Capabilities:**
    # - Collecting water and sediment samples.
    # - Precision maneuvering.
    def __init__(self, status="inactive", battery_level=100, position=(0, 0)):
        super().__init__("Sampling", status, battery_level, position)

    def collect_sample(self, sample_type, location):
        pass

class MaintenanceROV(ROV):
    # **Additional Capabilities:**
    # - Performing repairs on underwater equipment.
    # - Handling tools and components.
    def __init__(self, status="inactive", battery_level=100, position=(0, 0)):
        super().__init__("Maintenance", status, battery_level, position)

    def perform_maintenance(self, equipment_id):
        pass

if __name__ == '__main__':
    test = ROV("Default")
    print(test.rov_id)
    test2 = ROV("Default")
    print(test2.rov_id)