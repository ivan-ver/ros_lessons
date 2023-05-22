#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class FirstNode(Node):

    def __init__(self):
        super().__init__("FirstNode")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello word")


def main(args=None):
    rclpy.init(args=args)
    node = FirstNode()
    rclpy.spin(node=node)
    rclpy.shutdown()

    