"""
extract_embeddings.py: This file is responsbile for using a deep learning feature extractor to generate a 128-D vector describing a face.
All faces in our dataset will be passed through the neural network to generate embeddings.
"""

# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
                help="path to input directory of faces + images")
ap.add_argument("-e", "--embeddings", required=True,
                help="path to output serialized db of facial embeddings")
ap.add_argument("-d", "--detector", required=True,
                help="path to OpenCV's deep learning face detector")
ap.add_argument("-m", "--embedding-model", required=True,
                help="path to OpenCV's deep learning face embedding model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
                help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# load our serialized face detector from disk
print("[INFO] Loading Face Detector...")
protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
