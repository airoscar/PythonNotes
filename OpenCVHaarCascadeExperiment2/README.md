# OpenCVHaarCascadeExperiment2

Built on the previous experiment, this experiment uses several positive sample images. Each positive sample image is used to generate 2100 positive samples (by overlaying with 2100 negative samples).

A master info file was created by combining the individual info.lst files created for each time opencv_createsamples was ran. A vector file then created from the master info file for training.

Demo: https://www.youtube.com/watch?v=JMWDi3LhCnU

There is noticeable improvement in its ability to recognize the minion under varying lighting conditions and can handle under/over-exposed image better. However since the same 2100 negative samples were used, it does not seem to have improved on the false-positive occurrences; and for whatever reason it thinks my face is a minion too :D
