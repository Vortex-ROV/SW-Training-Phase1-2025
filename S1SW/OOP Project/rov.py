import uuid
from time import sleep
import random

def generate_id():
	return int(uuid.uuid4())

class ROV:
	def __init__(self):
		self.rov_id = generate_id()
		self.type = None
		self.status = "Inactive"
		self.battery_level = 100
		self.position = "(0,0)"
		self.mission_queue = []
		self.data_storage = []


	def send_status_update(self):
		pass

	def collect_data(self):
		pass

	def check_battery(self):
		print(f"Current battery level: {self.battery_level}")


	def handle_malfunction(self):
		pass

	def navigate_to(self, target_position):
		random_delay = random.randint(1, 5)
		random_battery_expense = random.randint(1, 5)
		print(f"Navigating to {target_position}... This might take a while.")
		sleep(random_delay)
		self.battery_level -= random_battery_expense
		print(f"Reached destination {target_position} in {random_delay} Seconds.")
		self.check_battery()


	def receive_mission(self, mission):
		self.mission_queue.append(mission)

	def execute_mission(self):
		while self.mission_queue:
			self.status = "Active."
			mission_title = self.mission_queue[0]
			mission_type = 	self.mission_queue[0].split(" ")[0]
			mission_location = self.mission_queue[0].split(" ")[1]
			match mission_type:
				case "map":
					self.map_area(mission_location)
					self.mission_queue.pop(0)
				case "sample":
					self.collect_sample(mission_location)
					self.mission_queue.pop(0)
				case "fix":
					pass
				case _:
					print("Invalid mission type! Try again.")


class ExplorationROV(ROV):
	def __init__(self):
		super().__init__()
		self.status = "Idle."
		self.type = "Exploration."

	def map_area(self, location):
		self.navigate_to(location)
		print(f"Mapped area at {location}.")



class SamplingROV(ROV):
	# **Additional Capabilities:**
	# - Collecting water and sediment samples.
	# - Precision maneuvering.
	def __init__(self):
		super().__init__()
		self.status = "Idle."
		self.type = "Sampling."

	def collect_sample(self, location):
		self.navigate_to(location)
		print(f"Collected sample from {location}.")


class MaintenanceROV(ROV):
	# **Additional Capabilities:**
	# - Performing repairs on underwater equipment.
	# - Handling tools and components.
	def __init__(self):
		super().__init__()
		self.status = "Idle."
		self.type = "Maintenance."

	def perform_maintenance(self, equipment_id):
		# self.navigate_to(location)
		pass
