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
    features = []
    classNames = rospy.get_param('~classes', {'silence', 'speech'})
    classNames = classNames.split()
    for a in classNames:
        temp = numpy.load(os.path.dirname(os.path.realpath(sys.argv[0]))+'/classifier_data/'+a+'.npy')        
        features.append(temp)                                
    classifierParams = numpy.array([0.001, 0.01,  0.5, 1.0, 5.0])
    nExp = 50
    bestParam = audioTrainTest.evaluateClassifier(features, classNames, nExp, "svm", classifierParams, 0, perTrain = 0.01)
    [featuresNorm, MEAN, STD] = audioTrainTest.normalizeFeatures(features)
    MEAN = MEAN.tolist()
    STD = STD.tolist()
    Classifier = audioTrainTest.trainSVM(featuresNorm, bestParam)
    #todo
    #featureAndTrain("/home/fnaser/Music", )
    #Classifier.save_model(os.path.dirname(os.path.realpath(sys.argv[0]))+'/classifier_data/'+modelName)
    with open(os.path.dirname(os.path.realpath(sys.argv[0]))+'/classifier_data/'+modelName, 'wb') as fid:
        cPickle.dump(Classifier, fid)   
    fo = open(os.path.dirname(os.path.realpath(sys.argv[0]))+'/classifier_data/'+modelName + "MEANS", "wb")
    cPickle.dump(MEAN, fo, protocol=cPickle.HIGHEST_PROTOCOL)
    cPickle.dump(STD, fo, protocol=cPickle.HIGHEST_PROTOCOL)
    cPickle.dump(classNames, fo, protocol=cPickle.HIGHEST_PROTOCOL)
    cPickle.dump(0, fo, protocol=cPickle.HIGHEST_PROTOCOL)
    cPickle.dump(0, fo, protocol=cPickle.HIGHEST_PROTOCOL)
    cPickle.dump(0, fo, protocol=cPickle.HIGHEST_PROTOCOL)
    cPickle.dump(0, fo, protocol=cPickle.HIGHEST_PROTOCOL)
    cPickle.dump(0, fo, protocol=cPickle.HIGHEST_PROTOCOL)
    fo.close()
     
