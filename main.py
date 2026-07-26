# Minhas Kamal (minhaskamal024@gmail.com)
# 09 Mar 24

import tkinter as tk
from tkinter import messagebox
import movement
import patientRecord
import homeView
import jointSelectorView
import openFileView
import poseCapturerView
import poseCapturerViewPatient
import previewMovementView
import patientView

class Main:

    view_frame: tk.Frame
    action_button: tk.Button
    cancel_button: tk.Button

    ok_text = "Ok"
    save_text = "Save"
    cancel_text = "Cancel"
    exit_text = "Exit"

    @classmethod
    def main(cls) -> None:
        doctor_movement = movement.Movement()
        patient_record = patientRecord.PatientRecord()

        ui = tk.Tk()
        ui.title("Virt")
        ui.geometry("+0+0")
        ui.state('zoomed')
        ui.option_add("*Font", ('Arial', 12))
        ui.option_add("*Background", "#fff")


        cls.view_frame = tk.Frame(ui)
        cls.view_frame.name = ""
        cls.view_frame.pack(fill="both")

        button_frame = tk.Frame(ui, bg='#eee')
        button_frame.pack(pady=10)

        operation_option = tk.StringVar(cls.view_frame, "0")

        cls.cancel_button = tk.Button(
            button_frame,
            command=lambda:
            cls._cancel_button_command(operation_option))
        cls.cancel_button.pack(side=tk.LEFT, padx=10)

        cls.action_button = tk.Button(
            button_frame,
            command=lambda:
            cls._action_button_command(
                doctor_movement,
                patient_record,
                operation_option))
        cls.action_button.pack(side=tk.LEFT, padx=10)

        cls._load_view(cls.ok_text, cls.exit_text, homeView.HomeView.show, operation_option)

        try:
            ui.mainloop()
        finally:
            if hasattr(poseCapturerView.PoseCapturerView, 'camera') and poseCapturerView.PoseCapturerView.camera.isOpened():
                poseCapturerView.PoseCapturerView.camera.release()
            if hasattr(poseCapturerViewPatient.PoseCapturerViewPatient, 'camera') and poseCapturerViewPatient.PoseCapturerViewPatient.camera.isOpened():
                poseCapturerViewPatient.PoseCapturerViewPatient.camera.release()
        return

    @classmethod
    def _cancel_button_command(
            cls, operation_option: tk.StringVar) -> None:
        
        if cls.view_frame.name == homeView.HomeView.__name__:
            cls.view_frame.quit()
            return
        elif cls.view_frame.name == poseCapturerView.PoseCapturerView.__name__:
            if poseCapturerView.PoseCapturerView.camera.isOpened():
                poseCapturerView.PoseCapturerView.camera.release()
        elif cls.view_frame.name == poseCapturerViewPatient.PoseCapturerViewPatient.__name__:
            if poseCapturerViewPatient.PoseCapturerViewPatient.camera.isOpened():
                poseCapturerViewPatient.PoseCapturerViewPatient.camera.release()
                
        cls._load_view(cls.ok_text, cls.exit_text, homeView.HomeView.show, operation_option)

        return

    @classmethod
    def _action_button_command(
            cls, doctor_movement: movement.Movement, patient_record: patientRecord.PatientRecord,
            operation_option: tk.StringVar) -> None:
        
        if cls.view_frame.name == homeView.HomeView.__name__:
            if operation_option.get() == homeView.HomeView.create_new_movement_option:
                cls._load_view("Next 1", cls.cancel_text, jointSelectorView.JointSelectorView.show,
                               doctor_movement)
            elif operation_option.get() == homeView.HomeView.create_new_patient_option:
                cls._load_view(cls.save_text, cls.cancel_text, patientView.PatientView.show,
                               patient_record)
            elif operation_option.get() == homeView.HomeView.perform_movement_option:
                cls._load_view("Open", cls.cancel_text, openFileView.OpenFileView.show,
                               patient_record)
            else:
                print(operation_option.get())

        elif cls.view_frame.name == jointSelectorView.JointSelectorView.__name__:
            cls._load_view("Next 2", cls.cancel_text, poseCapturerView.PoseCapturerView.show,
                           doctor_movement)

        elif cls.view_frame.name == poseCapturerView.PoseCapturerView.__name__:
            if not poseCapturerView.PoseCapturerView.camera.isOpened():
                cls._load_view(cls.save_text, cls.cancel_text, previewMovementView.PreviewMovementView.show,
                           doctor_movement)

        elif cls.view_frame.name == previewMovementView.PreviewMovementView.__name__:
            if cls.action_button.cget("text") == cls.save_text:
                doctor_movement.save()
                messagebox.showinfo("Saved", "New movement \"" +
                                    doctor_movement.name + "\" is created.")
            
            cls._load_view(cls.ok_text, cls.exit_text, homeView.HomeView.show, operation_option)

        elif cls.view_frame.name == openFileView.OpenFileView.__name__:
            if patient_record.file_path:
                patientRecord.PatientRecord.from_file(patient_record, patient_record.file_path)
                cls._load_view(cls.save_text, cls.cancel_text,
                        poseCapturerViewPatient.PoseCapturerViewPatient.show,
                        patient_record)

        elif cls.view_frame.name == poseCapturerViewPatient.PoseCapturerViewPatient.__name__:
            if not poseCapturerViewPatient.PoseCapturerViewPatient.camera.isOpened():
                patient_record.save()
                cls._load_view(cls.ok_text, cls.exit_text, homeView.HomeView.show, operation_option)

        elif cls.view_frame.name == patientView.PatientView.__name__:
            if cls.action_button.cget("text") == cls.save_text:
                patient_record.save()
                print(patient_record)
                messagebox.showinfo("Saved", "New patient \"" +
                                    patient_record.name + "\" is created.")
            
            cls._load_view(cls.ok_text, cls.exit_text, homeView.HomeView.show, operation_option)
        else:
            cls.action_button.config(bg="#f00")

        return

    @classmethod
    def _load_view(
            cls, action_button_text: str, cancel_button_text: str,
            show_func, show_func_arg) -> None:
        cls._clear_view_frame(cls.view_frame)
        cls.action_button['text'] = action_button_text
        cls.cancel_button['text'] = cancel_button_text
        show_func(cls.view_frame, show_func_arg)

    @classmethod
    def _clear_view_frame(cls, view_frame: tk.Frame) -> None:
        for component in view_frame.winfo_children():
            component.destroy()
        return


if __name__ == "__main__":
    Main.main()
