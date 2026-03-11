cmake_minimum_required(VERSION 3.0.2)
project(softmatics_gazebo)

find_package(catkin REQUIRED COMPONENTS gazebo_ros)
catkin_package(CATKIN_DEPENDS gazebo_ros)
