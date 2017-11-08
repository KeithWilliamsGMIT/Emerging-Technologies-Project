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

# STEP 3) Train the model
# A cost function is used to quantify the accuracy of the model.
# The lower the cost the more accurate the model will be.
# The cross-entropy function is a common way to calculate the cost of a model in machine learning.

y_ = tf.placeholder(tf.float32, [None, 10])

# Implement the cross-entropy function.
# - tf.log computes the logarithm of each element of y.
# - Multiply each element of y_ with the corresponding element of tf.log(y).
# - tf.reduce_sum adds the elements in the second dimension of y, due to the reduction_indices=[1] parameter.
# - tf.reduce_mean computes the mean over all the examples in the batch.
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# Minimize cross_entropy using the gradient descent algorithm with a learning rate of 0.5.
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Create a tensorflow session in which the model will run and initialize the variables.
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

# Start by training the model 1000 times.
for _ in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# STEP 4) Evaluate the model
# Get index of highest entry on both the tensors representing the result and correct labels.
# - Result tensor (y) might be -		[0.1, 0.1, 0.5, 0.1, 0.1, 0.2, 0.1, 0.5, 0.1, 0.1] (Model classified digit as a 5 - total adds up to 1)
# - Correct label tensor (y) might be -	[  0,   0,   0,   0,   0,   1,   0,   0,   0,   0] (one-hot vector representing the label 5)
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

# Determine the fraction that are correct.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Get accuracy for test set.
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

# Return the digit in the given image as a string.
# The image is represented by an array with 784 elements.
# Each element represents a pixel value.
def get_digit_from_image(image):
	one_hot = sess.run(y, feed_dict={x: image})
	classification = tf.argmax(y, 1)
	return str(sess.run(classification, feed_dict={y: one_hot})[0])