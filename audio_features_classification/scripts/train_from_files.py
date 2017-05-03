#!/usr/bin/env python
import cPickle
import numpy
import rospy
import sys
import os
from pyAudioAnalysis import audioTrainTest


if __name__ == '__main__':
    rospy.init_node("classifier_train_node")
    modelName = rospy.get_param('~classifier_name', 'modelSVM')
    path_to_files = rospy.get_param('~path_to_files', '/home/fnaser/Music/')

    dirlist_names = os.listdir(path_to_files)
    dirlist = []

    for dir_name in dirlist_names:
        abs_path_to_dir = path_to_files + dir_name
        dirlist.append(abs_path_to_dir)

    print dirlist

    audioTrainTest.featureAndTrain(dirlist, 0.1, 0.05, 0.01, 0.005, 'svm', modelName)


