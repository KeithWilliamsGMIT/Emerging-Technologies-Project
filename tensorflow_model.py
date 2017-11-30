# Author:		Keith Williams
# Date:			06/11/2017
# Description:	Detect digit from image using TensorFlow.
# Adapted from:
#	- https://www.tensorflow.org/get_started/mnist/beginners
#	- https://stackoverflow.com/questions/33759623/tensorflow-how-to-save-restore-a-model
#	- https://www.tensorflow.org/get_started/mnist/pros

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Define some functions that will be used later.

# Function to initialise weights with a small amount of noise for symmetry breaking and to prevent 0 gradients.
def weight_variable(shape):
	initial = tf.truncated_normal(shape, stddev=0.1)
	return tf.Variable(initial)

# Function to initialise biases with a slightly positive initial bias to avoid "dead neurons" since ReLU neurons will be used.
# ReLU (rectified linear unit) neurons are used as activation function in deep learning networks.
# It's defined as f(x)=max(0,x) where x is the input.
def bias_variable(shape):
	initial = tf.constant(0.1, shape=shape)
	return tf.Variable(initial)

# Function to setup convolutions.
# These convolutions will use stride of one and are zero padded so that the output is the same size as the input.
def conv2d(x, W):
	# A convolution is an operation on two functions that produce a third.
	# In this case our two functions are x and W.
	return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

# Function to initialise pooling.
# The pooling is plain old max pooling over 2x2 blocks.
def max_pool_2x2(x):
	return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# STEP 1) Load the data
# Download and read in the MNIST data set.
# - 55,000 data points of training data (mnist.train)
# - 10,000 points of test data (mnist.test)
# - 5,000 points of validation data (mnist.validation).
# Each data point, or image, is flattend, meaning it is a 1D array of 784 values (28px x 28px).
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# STEP 2) Define the model
# Softmax regression technique (Used to assign probabilities to an object being one of several different things).
# This techniques gives a list of values between 0 and 1 that add up to 1.
# 1) Add up the evidence of the input being in certain classes.
# 2) Convert that evidence into probabilities.

# Create a placeholder node for pixels of flattened image.
x = tf.placeholder(tf.float32, [None, 784], name='x')

# Create the weight and bias as variables so that their values can be adjusted by tensorflow.
# They are initialised as tensors full of zeros.
W = tf.Variable(tf.zeros([784, 10]), name='W')
b = tf.Variable(tf.zeros([10]), name='b')

# First convolutional layer (convolution and max pooling)
# The convolution will compute 32 features for each 5x5 patch.
# A feature is an individual measurable property or characteristic of a phenomenon being observed, usually numeric.
# Its weight tensor will have a shape of [5, 5, 1, 32].
# The first two dimensions are the patch size, the next is the number of input channels, and the last is the number of output channels.
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

# First reshape x to a 4d tensor, with the second and third dimensions corresponding to image width and height, and the final dimension corresponding to the number of color channels.
x_image = tf.reshape(x, [-1, 28, 28, 1])

# Convolve x_image with the weight tensor.
# - Add the bias.
# - Apply the ReLU function.
# - Finally max pool.
# The max_pool_2x2 method will reduce the image size to 14x14.
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# Second convolutional layer
# This layer will have 64 features for each 5x5 patch.
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# Densely connected layer
# The image size has been reduced to 7x7.
# Add a fully-connected layer with 1024 neurons to allow processing on the entire image.
# Reshape the tensor from the pooling layer into a batch of vectors, multiply by a weight matrix, add a bias, and apply a ReLU.
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# Dropout
# To reduce overfitting, we will apply dropout before the readout layer.
# Create a placeholder for the probability that a neuron's output is kept during dropout. 
# This allows us to turn dropout on during training, and turn it off during testing.
# TensorFlow's tf.nn.dropout op automatically handles scaling neuron outputs in addition to masking them.
# Therefore, dropout just works without any additional scaling.
keep_prob = tf.placeholder(tf.float32, name='keep_prob')
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# Readout Layer
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.add(tf.matmul(h_fc1_drop, W_fc2), b_fc2, name='y_conv')

# STEP 3) Evaluate the model
# Define the neurons that will be used to evaluate the model here.
# The model will be evaluated at several training steps rather than afterwards.

# Placeholder for the correct label.
y_ = tf.placeholder(tf.float32, [None, 10], name='y_')

# Get index of highest entry on both the tensors representing the result and correct labels.
# - Result tensor (y) might be -		[0.1, 0.1, 0.05, 0.1, 0.1, 0.2, 0.1, 0.05, 0.1, 0.1] (Model classified digit as a 5 - total adds up to 1)
# - Correct label tensor (y) might be -	[  0,   0,    0,   0,   0,   1,   0,    0,   0,   0] (one-hot vector representing the label 5)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))

# Determine the fraction that are correct.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# STEP 4) Train the model
# A cost function is used to quantify the accuracy of the model.
# The lower the cost the more accurate the model will be.
# The cross-entropy function is a common way to calculate the cost of a model in machine learning.

# Implement the cross-entropy function between the target and the softmax activation function applied to the model's prediction.
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))

# Minimize cross_entropy using the adam algorithm.
# Pass a learning rate to the algorithm.
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

tf.add_to_collection('train_step', train_step)

# Create a Saver object.
saver = tf.train.Saver()

# Create a tensorflow session in which the model will run and initialize the variables.
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

# Train the model X numnber of times.
for i in range(20000):
	batch_xs, batch_ys = mnist.train.next_batch(50)
	
	# Evaluate the accuracy of the model every nth iteration.
	if i % 100 == 0:
		train_accuracy = sess.run(accuracy, feed_dict={x: batch_xs, y_: batch_ys, keep_prob: 1.0})
		print('Step %d - Training accuracy %g' % (i, train_accuracy))
	
	sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys, keep_prob: 0.5})

print('Accuracy: %s' % (sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0})))

# Save the final model.
saver.save(sess, './models/digit-model')