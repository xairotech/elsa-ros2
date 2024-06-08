use the below command to start the micro ros agent 

`ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyACM0`

use the below command to use the teleop twist

`ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=/turtle1/cmd_vel`

