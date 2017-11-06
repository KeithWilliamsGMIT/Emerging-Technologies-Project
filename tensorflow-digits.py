# Author:		Keith Williams
# Date:			06/11/2017
# Description:	Detect digit from image using TensorFlow.
# Adapted from:
#	- https://www.tensorflow.org/get_started/mnist/beginners

from tensorflow.examples.tutorials.mnist import input_data

# STEP 1) Load the data
# Download and read in the MNIST data set.
# - 55,000 data points of training data (mnist.train)
# - 10,000 points of test data (mnist.test)
# - 5,000 points of validation data (mnist.validation).
# Each data point, or image, is flattend, meaning it is a 1D array of 784 values (28px x 28px).
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)