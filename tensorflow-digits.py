# Author:		Keith Williams
# Date:			06/11/2017
# Description:	Detect digit from image using TensorFlow.
# Adapted from:
#	- https://www.tensorflow.org/get_started/mnist/beginners

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# STEP 1) Load the data
# Download and read in the MNIST data set.
# - 55,000 data points of training data (mnist.train)
# - 10,000 points of test data (mnist.test)
# - 5,000 points of validation data (mnist.validation).
# Each data point, or image, is flattend, meaning it is a 1D array of 784 values (28px x 28px).
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# STEP 2) Define the model
# Softmax regression technique (Used to assign probabilities to an object being one of several different things).
# This techniques gives a list of values between 0 and 1 that add up to 1.
# 1) Add up the evidence of the input being in certain classes.
# 2) Convert that evidence into probabilities.

# Create a placeholder node for pixels of flattened image.
x = tf.placeholder(tf.float32, [None, 784])

# Create the weight and bias as variables so that their values can be adjusted by tensorflow.
# They are initialised as tensors full of zeros.
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Implement the model.
# - Multiply x by W
# - Add b
# - Apply softmax
y = tf.nn.softmax(tf.matmul(x, W) + b)