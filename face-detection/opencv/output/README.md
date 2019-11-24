# Output Folder

This folder contains output pickle files.
Any object in python can be pickled so that it can be saved on disk.
Basically converts objects into character streams.

#### embeddings.pickle

A serialized facial embeddings file. Embeddings have been computed for every face in the an old dataset

#### le.pickle

Our label encoder. Contains the name labels for the people that our model can recognize.

#### recognizer.pickle

Our Linear Support Vector Machine (SVM) model. This is a machine learning model, not deep learning model, and it is responsible for actually recognizing faces.
