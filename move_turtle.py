#ros2_ws/src/my_turtle_controller/my_turtle_controller/move_turtle.py
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveTurtle(Node):
    def __init__(self):
        super().__init__('move_turtle')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_timer(0.5, self.move)

    def move(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.publisher.publish(msg)
        self.get_logger().info('Moving the turtle!')

def main():
    rclpy.init()
    node = MoveTurtle()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
