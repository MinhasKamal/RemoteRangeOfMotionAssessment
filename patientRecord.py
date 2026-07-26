# Minhas Kamal (minhaskamal024@gmail.com)
# 10 Mar 24

import movement
import cv2
import json
import os
import re
from datetime import datetime
import utils

class PatientRecord:
    _datetime_format = "%Y%m%d%H%M%S"

    def __init__(self) -> None:
        self.name: str = ""
        self.repeat: int = ""
        self.assigned_movement: movement.Movement = None
        self.resting_pose_images: list[cv2.typing.MatLike] = []
        self.flexing_pose_images: list[cv2.typing.MatLike] = []
        self.dates: list[str] = []
        self.scores: list[str] = []
        self.file_path: str = ""
        self.movement_file_path: str = ""
        return

    def __str__(self) -> str:
        data = {
            "name": self.name,
            "repeat": self.repeat,
            "dates": self.dates,
            "scores": self.scores,
            "movement_file_path": self.movement_file_path
        }
        return json.dumps(data, indent=4) + "\n"

    def save(self) -> None:
        os.makedirs("res", exist_ok=True)
        if not self.file_path:
            safe_name = re.sub(r'[^\w\s-]', '', self.name).strip()
            self.file_path = "res/" + safe_name
        with open(self.file_path + utils.patient_file_extension, "w") as file:
            file.write(str(self))
        return

    @staticmethod
    def from_file(patientRecord, file_path: str):
        with open(file_path + utils.patient_file_extension, "r") as file:
            patientRecord_json = json.load(file)

        patientRecord.file_path = file_path
        patientRecord.name = patientRecord_json["name"]
        patientRecord.repeat = int(patientRecord_json["repeat"])
        patientRecord.dates = patientRecord_json["dates"]
        patientRecord.scores = patientRecord_json["scores"]
        patientRecord.movement_file_path = patientRecord_json["movement_file_path"]
        patientRecord.assigned_movement = movement.Movement.from_file(patientRecord.movement_file_path)
        return

# test
if __name__ == "__main__":
    patientRecord = PatientRecord()
    PatientRecord.from_file(patientRecord, "res/RightElbow-Minhas")
    patientRecord.dates.append(str(datetime.today().strftime(PatientRecord._datetime_format)))
    patientRecord.scores.append(str(75))
    print(patientRecord)
    # patientRecord.save()
