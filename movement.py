# Minhas Kamal (minhaskamal024@gmail.com)
# 10 Mar 24

from datetime import datetime
import cv2
import json
import types
import os
import re
import utils

class Movement:

    def __init__(self) -> None:
        self.name: str = ""
        self.tracking_joint_list: list[str] = []
        self.observing_joint_list: list[str] = []
        self.resting_pose_joint_coordinates: list = []
        self.flexing_pose_joint_coordinates: list = []
        self.resting_pose_image: cv2.typing.MatLike = None
        self.flexing_pose_image: cv2.typing.MatLike = None
        self.file_path: str = ""
        return

    def __str__(self) -> str:
        data = {
            "name": self.name,
            "tracking_joint_list": self.tracking_joint_list,
            "observing_joint_list": self.observing_joint_list,
            "resting_pose_joint_coordinates": [
                {"x": j.x, "y": j.y, "z": j.z, "visibility": j.visibility} for j in self.resting_pose_joint_coordinates
            ] if self.resting_pose_joint_coordinates else [],
            "flexing_pose_joint_coordinates": [
                {"x": j.x, "y": j.y, "z": j.z, "visibility": j.visibility} for j in self.flexing_pose_joint_coordinates
            ] if self.flexing_pose_joint_coordinates else []
        }
        return json.dumps(data, indent=4) + "\n"
    
    def save(self) -> None:
        os.makedirs("res", exist_ok=True)
        if not self.file_path:
            safe_name = re.sub(r'[^\w\s-]', '', self.name).strip()
            self.file_path = "res/" + safe_name + "_" + datetime.today().strftime("%Y%m%d%H%M%S")
            
        with open(self.file_path + utils.movement_file_extension, "w") as file:
            file.write(str(self))

        cv2.imwrite(self.file_path + "_rest.jpg", self.resting_pose_image)
        cv2.imwrite(self.file_path + "_flex.jpg", self.flexing_pose_image)

        return

    @classmethod
    def from_file(cls, file_path: str):
        with open(file_path + utils.movement_file_extension, "r") as file:
            movement_json = json.load(file)

        movement: Movement = cls()
        movement.file_path = file_path
        movement.name = movement_json["name"]
        movement.tracking_joint_list = movement_json["tracking_joint_list"]
        movement.observing_joint_list = movement_json["observing_joint_list"]
        for resting_pose_joint_coordinate in movement_json["resting_pose_joint_coordinates"]:
            movement.flexing_pose_joint_coordinates.append(
                cls._load_coordinate(resting_pose_joint_coordinate))
        for flexing_pose_joint_coordinate in movement_json["flexing_pose_joint_coordinates"]:
            movement.flexing_pose_joint_coordinates.append(
                cls._load_coordinate(flexing_pose_joint_coordinate))

        movement.resting_pose_image = cv2.imread(file_path + "_rest.jpg")
        movement.flexing_pose_image = cv2.imread(file_path + "_flex.jpg")

        return movement
    
    @classmethod
    def _load_coordinate(cls, joint_coordinate) -> types.SimpleNamespace:
        coordinate = types.SimpleNamespace()
        coordinate.x = joint_coordinate["x"]
        coordinate.y = joint_coordinate["y"]
        coordinate.z = joint_coordinate["z"]
        coordinate.visibility = joint_coordinate["visibility"]
        return coordinate


# test
if __name__ == "__main__":
    movement = Movement.from_file("res/test")
    print(movement)
