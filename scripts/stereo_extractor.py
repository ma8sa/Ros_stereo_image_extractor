#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image,CameraInfo
import message_filters
import cv2
from cv_bridge import CvBridge
import os

count = 0
bridge = CvBridge()

def callback(image_left , image_right):
    # wow 
         a = 10
         global count
         
         cv2_img_left = bridge.imgmsg_to_cv2(image_left, "bgr8")
         cv2_img_right = bridge.imgmsg_to_cv2(image_right, "bgr8")
         
         image_name = str(count).zfill(6)

         count += 1 
         print(count)
         if not os.path.exists('./Left'):
		os.mkdir('./Left') 
         if not os.path.exists('./Right'):
		os.mkdir('./Right') 
        
         cv2.imwrite('./Left/'+image_name+'.png', cv2_img_left)
         cv2.imwrite('./Right/'+image_name+'.png', cv2_img_right)
     


if __name__ == '__main__':
        
        rospy.init_node('extractor', anonymous=True)
        
	namespace = "frontNear/"
        topic = "image_rect_color"
 
	image_0_sub = message_filters.Subscriber(namespace+'left/'+topic, Image)
	image_1_sub = message_filters.Subscriber(namespace+'right/'+topic, Image)
        ts = message_filters.TimeSynchronizer([image_0_sub, image_1_sub], 10)
        ts.registerCallback(callback)
        rospy.spin()
