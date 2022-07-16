#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import cv2

def publishing_image():
    publisher_image = rospy.Publisher('topic1', Image, queue_size=1)
    rospy.init_node('webcam_pub',anonymous=True)
    rate = rospy.Rate(5)
    webcam_capture = cv2.VideoCapture(0)
    br = CvBridge()

    while not rospy.is_shutdown():
        is_captured, image_read = webcam_capture.read()

        if is_captured == True:
            rospy.loginfo("Publishing Image Capture")
            publisher_image.publish(br.cv2_to_imgmsg(image_read))

        rate.sleep()

if __name__ == '__main__':
    try:
        publishing_image()
    except rospy.ROSInterruptException():
        pass