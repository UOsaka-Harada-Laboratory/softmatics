cmake_minimum_required(VERSION 3.0.2)
project(softmatics_device)

find_package(catkin REQUIRED
  rospy
  std_srvs
)

catkin_package(
  CATKIN_DEPENDS rospy std_srvs
)

catkin_install_python(
    PROGRAMS nodes/trigger.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
