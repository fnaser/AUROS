#!/usr/bin/env python
import roslib, rospy
import os
import sys

from audio_features_msgs.msg import featMsg
from audio_features_msgs.msg import classificationResult
from pyAudioAnalysis import audioTrainTest

global count_cars
global count_cars_left
global count_cars_right
count_cars = 0
count_cars_left = 0
count_cars_right = 0

def classificationResultCallback(classification_msg):
   global count_cars
   global count_cars_left
   global count_cars_right

   if classification_msg.class_result == "cars":
      count_cars = count_cars + 1

   if classification_msg.class_result == "cars_left":
      count_cars_left = count_cars_left + 1

   if classification_msg.class_result == "cars_right":
      count_cars_right = count_cars_right + 1

   print "cars: {0:.3f}\t left: {1:.3f}\t right: {2:.3f}".format(count_cars, count_cars_left, count_cars_right)

if __name__ == '__main__':

   rospy.init_node("audio_features_evaluate_node")

   sub_topic = "audio_features_classification_classifier/audio_classification"
   modelName = rospy.get_param('~classifier_name', 'modelSVM')

   #path_to_classifier_data = "/home/fnaser/catvehicle_ws/src/AUROS/audio_features_classification/scripts/classifier_data/"
   #modelName = ""
   #classifierInfo = {}

   #[Classifier, MEAN, STD, classNames, mtWin, mtStep, stWin, stStep, computeBEAT] = audioTrainTest.loadSVModel(path_to_classifier_data+modelName)

   classificationResultSub = rospy.Subscriber(sub_topic, classificationResult, classificationResultCallback)

   rospy.spin()

