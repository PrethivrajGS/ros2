# ros2_diff_drive_robot

A ROS 2 Humble project demonstrating a **custom differential drive robot** with velocity publisher and subscriber nodes.

## Features

- Publishes velocity commands (`cmd_vel`).  
- Subscriber prints velocity on console.  
- Visualizes the robot URDF in RViz2.

## Build & Run

### Build

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
