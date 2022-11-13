# softmatics

[![support level: community](https://img.shields.io/badge/support%20level-community-lightgray.svg)](http://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ROS package for [NITTA SOFTmatics](https://www.nitta.co.jp/en/product/robothand/) gripper.

# Dependencies

- ROS Noetic (Python3)

# Installation

    $ cd catkin_ws/src
	$ git clone git@github.com:takuya-ki/softmatics.git --depth 1
    $ cd ../
	$ sudo rosdep update && sudo rosdep install --from-paths ./src --ignore-packages-from-source --rosdistro noetic -y --os=ubuntu:focal -y
	$ catkin build -DPYTHON_EXECUTABLE=/usr/bin/python3

# Usage

## Visualize a model
    $ roslaunch softmatics_description disp_softmatics_model.launch

<img src="softmatics_description/images/softmatics.gif" height="400">  

# Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
