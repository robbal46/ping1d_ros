# ping1d_ros
ROS wrapper for BlueRobotics Ping Sonar (Echosounder &amp; Altimeter)

Publishes a ROS [sensor_msgs/Range](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Range.html) message with sonar data

To run the node, use the example launch file:

    roslaunch ping1d_ros example.launch

Make sure the `serial_port` parameter in the launch file to matches your system

If the serial port fails to open, check your user is added to the dialout group

If not, run

    sudo usermod -a -G dialout $USER
then reboot
