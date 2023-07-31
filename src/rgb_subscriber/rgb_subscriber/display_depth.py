#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class RGBSubscriber(Node):
    def __init__(self):
        super().__init__('depth_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/depth',  # 실제로 Isaac Sim에서 발행하는 토픽 이름으로 교체하세요
            self.image_callback,
            10
        )
        self.subscription  # 사용하지 않는 변수 경고를 방지하기 위해 추가
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            point_x, point_y = 250, 100
            distance_mm = cv_image[point_x, point_y]
            print(distance_mm)
            cv2.circle(cv_image, (point_x, point_y), 8, (0,0,255), -1)

            cv2.imshow('depth Image', cv_image)
            cv2.waitKey(1)
        except Exception as e:
            self.get_logger().error('이미지 처리 중 오류 발생: %s' % str(e))


def main(args=None):
    rclpy.init(args=args)
    rgb_subscriber = RGBSubscriber()
    rclpy.spin(rgb_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

