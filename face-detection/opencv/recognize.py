"""
recognize.py: This file will recognize faces in images. It will detect faces, extract embeddings, and query our SVM model to determine who is in an image.
We'll draw boxes around faces and annoate each box with a name.
"""
# import the necessary packages
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
ap.add_argument("-d", "--detector", required=True,
                help="path to OpenCV's deep learning face detector")
ap.add_argument("-m", "--embedding-model", required=True,
                help="path to OpenCV's deep learning face embedding model")
ap.add_argument("-r", "--recognizer", required=True,
                help="path to model trained to recognize faces")
ap.add_argument("-l", "--le", required=True,
                help="path to label encoder")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
                help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# load our serialized face detector from disk
print("[INFO] Loading Face Detector...")
protoPath = os.path.sep.join(args["detector"], "deploy.prototxt")
modelPath = os.path.sep.join(
    args["detector"], "res10_300x300_ssd_iter_140000.caffemodel")
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

# load our serialized face embedding model from disk
print("[INFO] Loading Face Recognizer...")
embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])

# load the labels and the recognizer
recognizer = pickle.loads(open(args["recognizer"], "rb").read())
le = pickle.loads(open(args["le"], "rb").read())
