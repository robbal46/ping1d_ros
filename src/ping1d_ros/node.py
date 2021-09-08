#!/usr/bin/env python3

from brping import Ping1D

import rospy
from sensor_msgs.msg import Range

class Node:

    def __init__(self):

        rospy.init_node('ping1d_node')

        serial_port = rospy.get_param('~serial_port', '/dev/ttyUSB0')
        baud_rate = rospy.get_param('~baud_rate', 115200)

        sonar = Ping1D()
        sonar.connect_serial(serial_port, baud_rate)

        if sonar.initialize():
            rospy.loginfo("Initialised Ping1D device")
        else:
            rospy.logerr("Failed to initialise Ping1D device")



        range_pub = rospy.Publisher('/ping1d_node/range', Range, queue_size=10)

        range_msg = Range()
        range_msg.radiation_type = 0 #ultrasound
        range_msg.field_of_view = 0.58236
        
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():

            sonar_data = sonar.get_distance()
            if sonar_data:                

                range_msg.header.stamp = rospy.Time.now()                  

                scan_range = sonar_data['distance'] / 1000  #mm to m conversion
                scan_min = sonar_data['scan_start'] / 1000 
                scan_max = sonar_data['scan_length'] /1000 + scan_min

                range_msg.range = scan_range

                range_msg.min_range = scan_min
                range_msg.max_range = scan_max

                range_pub.publish(range_msg)

            else:
                rospy.logerr('Failed to get data from Ping1D')

            rate.sleep()