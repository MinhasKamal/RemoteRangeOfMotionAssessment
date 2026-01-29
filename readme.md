# Remote Range of Motion Assessment
#### Device-Agnostic Remote Range-of-motion Assessment using Data Abstraction

![RemoteROMAssessment_Diagram](https://github.com/user-attachments/assets/4a74231e-ee0f-420b-9748-cffc07a557da)

Motion analysis is used for several applications related to exercise, movements, entertainment, and therapy. In-person clinical evaluations limit the flexibility of both the physician and the patients in terms of time and location. On the other hand, remote healthcare, such as telehealth options, provides patients the ability to receive healthcare without the need for in-person evaluation, increasing availability. Past research has been conducted as proof of concept of using virtual, joint tracking tools, such as RGB-D and RGB equipment, to assist with portability and low-cost solutions for computational motion analysis. Our work aims to ensure that a physician can record custom, lightweight abstract representation of movement data that can be stored in a library and later be retrieved by a patient for reference. To demonstrate that our system is device agnostic given the compact nature of data representation, we choose to present a prototype using Kinect V2 for RGB-D input and Google’s MediaPipe for RGB input. We utilize the system to capture motions by both a physician and patient, and calculate the Range of Motion for multiple exercises using either KinectV2 or a webcam based on the nature of the input. Our project acts as an easy-to-use system, allowing customization of motion plans and virtual range of motion feedback.

Access the full paper [here](https://www.computer.org/csdl/proceedings-article/mipr/2024/514200a221/213TEkgu6sg).

<div align="center">
<img width="600" height=auto alt="image" src="https://github.com/user-attachments/assets/08e06aee-e276-4cbd-9801-28b784aa0a25" />
</div>

## Environment Setup

```
conda create -n virt python=3.11

conda info --envs
conda deactivate
conda activate virt
conda info --envs

pip install mediapipe
pip install opencv-python
```

## Cite This Work
```
@INPROCEEDINGS {RemoteROMAssessment2024Ashtiani,
  author = {Ashtiani, Omeed and Maadugundu, Meghana Spurthi and Kamal, Minhas and Prabhakaran, Balakrishnan},
  title = {Device-Agnostic Remote Range-of-motion Assessment using Data Abstraction},
  booktitle = {2024 IEEE 7th International Conference on Multimedia Information Processing and Retrieval (MIPR)},
  publisher = {IEEE Computer Society},
  pages = {221-226},
  year = {2024},
  month = Aug,
  doi = {10.1109/MIPR62202.2024.00041}
}
```

See more of my research works [here](https://scholar.google.com/citations?user=SZxTaQgAAAAJ).
