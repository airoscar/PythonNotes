# OpenCVHaarCascadeExperiment1

Experimenting with computer vision: simple Haar cascade classifier trained to recognize a minion based on a picture.
This experiment was conducted on Python 3.6.7, Numpy 1.15.4, OpenCV 3.4.2.

This is intended as a learing experience with the OpenCV library on Jupyter Notebook, in particular the Haar cascade classifier and its utilities within OpenCV.

For ease of use, all code can be executed from Jupyter Notebook.

In this experiment, only one positive sample is provided, opencv_createsamples utility was used to overlay the positive samples on negative samples to create hundreds more positive samples.

The training process took only 5 minutes to complete all 10 stages on my little MacBook.

The trained model works only under ideal lighting conditions. It does not work if the object (the minion) is not well lit enough, or over-exposed.

Demo video:
https://www.youtube.com/watch?v=B-UgW2QJ-uk
