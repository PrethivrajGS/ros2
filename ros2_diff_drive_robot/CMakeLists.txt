cmake_minimum_required(VERSION 3.5)
project(ros2_diff_drive_robot)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(rviz2 REQUIRED)

install(DIRECTORY urdf launch
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  ros2_diff_drive_robot/velocity_publisher.py
  ros2_diff_drive_robot/velocity_subscriber.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
