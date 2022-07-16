#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import cv2

def processing_image(captured_image):
    br = CvBridge()
    rospy.loginfo("Subscribing to Image Capture")
    current_frame = br.imgmsg_to_cv2(captured_image)
    
    t_lower = 50  
    t_upper = 150  
    edge = cv2.Canny(current_frame, t_lower, t_upper)
    
    cv2.imshow('original', current_frame)
    cv2.imshow('edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
          
def receive_message(): 
    rospy.init_node('webcam_sub', anonymous=True)
    rospy.Subscriber('topic1', Image, processing_image)
    rospy.spin()
    cv2.destroyAllWindows()
  
if __name__ == '__main__':
    receive_message()