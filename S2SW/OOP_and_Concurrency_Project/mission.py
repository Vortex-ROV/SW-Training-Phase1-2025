from enum import Enum


class MissionStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    FAILED = 4


class Mission:
    def __init__(self, mission_id, mission_type, target_location, parameters):
        self.mission_id = mission_id
        self.mission_type = mission_type
        self.target_location = target_location
        self.parameters = parameters
        self.status = MissionStatus.PENDING
