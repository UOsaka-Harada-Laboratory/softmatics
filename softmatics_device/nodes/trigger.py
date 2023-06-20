#!/usr/bin/env 3

import serial

import rospy
from std_srvs.srv import Trigger, TriggerResponse


class SoftmaticsTriggerNode:
    """Class to handle toggle control."""
    def __init__(self, devicename, baudrate):
        self._current_mode = False
        self._ser = serial.Serial(devicename, baudrate)
        rospy.sleep(1)
        self.toggle_softmatics_srv = rospy.Service(
            "/softmatics_device/toggle",
            Trigger,
            self.handle_toggle_softmatics)

    def handle_toggle_softmatics(self, req):
        """To handle toggle control via serial communication."""
        self._current_mode = not self._current_mode
        if self._current_mode:
            self._ser.write(b"0")  # off
            rospy.sleep(1)
            self._ser.write(b"1")  # on
            rospy.sleep(1)
        else:
            self._ser.write(b"1")  # on
            rospy.sleep(1)
            self._ser.write(b"0")  # off
            rospy.sleep(1)

        return TriggerResponse(
            success=None,  # TODO: implement
            message=None)  # TODO: implement


if __name__ == '__main__':
    rospy.init_node('softmatics_trigger_node', log_level=rospy.DEBUG)
    devicename = rospy.get_param(
        "/softmatics_device/port", "/dev/ttyACM0")
    baudrate = rospy.get_param(
        "/softmatics_device/baudrate", 9600)
    node = SoftmaticsTriggerNode(devicename, baudrate)
    rospy.spin()
