from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    urdf_file = os.path.join(
        os.path.dirname(__file__), '../urdf/diff_drive_robot.urdf'
    )

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            arguments=[urdf_file]
        ),
        Node(
            package='ros2_diff_drive_robot',
            executable='velocity_publisher.py',
            name='velocity_publisher'
        ),
        Node(
            package='ros2_diff_drive_robot',
            executable='velocity_subscriber.py',
            name='velocity_subscriber'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2'
        )
    ])
