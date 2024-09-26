import time
import threading
import random
import queue
from rov import RovType, RovStatus, MaintenanceROV
from mission import Mission


class MarineMissionControlSystem:
    def __init__(self, rov_fleet, mission_count, available_rov_types):
        self.rov_fleet = rov_fleet
        self.mission_count = mission_count
        self.available_rov_types = available_rov_types
        self.missions = []
        self.completed_missions = 0
        self.print_lock = threading.Lock()  # Lock to prevent multiple threads from printing at the same time
        self.mission_queue = queue.Queue()

    def generate_missions(self):
        """
        Generate random missions according to the number of missions, number of ROVs from each type.
        """
        for i in range(self.mission_count):
            mission_type = random.choice(list(self.available_rov_types))
            target_location = (random.randint(0, 100), random.randint(0, 100))
            parameters = {}
            if mission_type == RovType.EXPLORATION:
                parameters['area'] = (f"({target_location[0] - 5},{target_location[1] - 5}) to "
                                      f"({target_location[0] + 5},{target_location[1] + 5})")
            elif mission_type == RovType.SAMPLING:
                parameters['sample_type'] = random.choice(['water', 'sediment', 'biological'])
            elif mission_type == RovType.MAINTENANCE:
                parameters['equipment_id'] = f"EQ-{random.randint(100, 999)}"

            mission = Mission(i + 1, mission_type, target_location, parameters)
            self.missions.append(mission)
            self.mission_queue.put(mission)

    def assign_mission(self, rov):
        """
        Assign a mission to an ROV if the mission type matches the ROV type.
        If no mission is available, return False.
        """
        if not self.mission_queue.empty():
            mission = self.mission_queue.get()
            if mission.mission_type == rov.rov_type:
                rov.receive_mission(mission)
                return True
            else:
                # If the mission doesn't match the ROV type, put it back in the queue
                self.mission_queue.put(mission)
                return False
        return False

    def rov_thread(self, rov):
        """
        Thread function for each ROV. Assigns missions to the ROV and handles malfunctions.
        """
        while True:
            if self.completed_missions >= self.mission_count:
                break
            
            if rov.status == RovStatus.IDLE:
                if self.assign_mission(rov):
                    rov.execute_mission()
                    with self.print_lock:
                        self.completed_missions += 1
                else:
                    time.sleep(1) 
            elif rov.status == RovStatus.MALFUNCTION:
                self.handle_rov_malfunction(rov)
            else:
                time.sleep(1) 

    def handle_rov_malfunction(self, malfunctioned_rov):

        """
        Handle a malfunctioned ROV by assigning a Maintenance ROV to fix it.
        """
        maintenance_rov = next((rov for rov in self.rov_fleet if isinstance(rov, MaintenanceROV) and
                                rov.status == RovStatus.IDLE), None)  

        if maintenance_rov:
            with self.print_lock:
                print(f"[{self.get_timestamp()}] Maintenance ROV {maintenance_rov.rov_id} assigned to fix ROV "
                      f"{malfunctioned_rov.rov_id}")
            maintenance_rov.status = RovStatus.IN_MISSION
            maintenance_rov.navigate_to(malfunctioned_rov.position)
            maintenance_rov.perform_maintenance(f"ROV-{malfunctioned_rov.rov_id}")
            malfunctioned_rov.status = RovStatus.IDLE
            maintenance_rov.status = RovStatus.IDLE
        else:
            with self.print_lock:
                print(f"[{self.get_timestamp()}] No available Maintenance ROV to fix ROV {malfunctioned_rov.rov_id}")

    def run_simulation(self):
        """
        Run the simulation by generating missions and creating threads for each ROV.
        """
        self.generate_missions()
        threads = []
        for rov in self.rov_fleet:
            thread = threading.Thread(target=self.rov_thread, args=(rov,)) 
            threads.append(thread)
            thread.start()


        for thread in threads:
            thread.join()

        self.print_final_summary()

    def print_final_summary(self):
        """
        Print the final summary of the simulation.
        """
        with self.print_lock:
            print(f"\n[{self.get_timestamp()}] All missions have been completed.")
            print(f"[{self.get_timestamp()}] Simulation ended.\n")
            print("Final Summary:")
            print(f"- Total Missions Completed: {self.completed_missions}")
            for rov in self.rov_fleet:
                print(f"- ROV {rov.rov_id} Status: {rov.status.name}, Battery Level: {rov.battery_level}%")

    @staticmethod
    def get_timestamp():
        return time.strftime("%H:%M:%S", time.localtime())
