# softmatics

NITTA SOFTmatics packages

# Features

- ROS Noetic (Python3)
- Controler for NITTA SOFTmatics

# Installation

	$ git clone git@github.com:takuya-ki/softmatics.git catkin_ws/src; cd catkin_ws
	$ sudo rosdep install --from-paths ./src --ignore-packages-from-source --rosdistro noetic -y --os=ubuntu:focal -y
	$ catkin build -DPYTHON_EXECUTABLE=/usr/bin/python3

# Usage

## Visualize a model
    $ roslaunch softmatics_visualization disp_softmatics_model.launch

# Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)
