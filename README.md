# Emerging Technologies Project
This is my 4th year project for the emerging technologies module in college. For this project I was tasked with creating a Python web application to recognise digits in images. Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image. This application will use Tensorflow and Flask.

## Getting started
First ensure you have Python 3 installed. The easiest way to install Python is through [Anaconda](https://www.anaconda.com/downloads). Next create a virtual environment in the app folder to store all the required packages. Once created, activate the new environment using the `source` command and install the packages listed in the `requirements.txt` file. Finally, start the application using the below command.

```
# Create the virtual environment
virtualenv -p python3 venv

# Activate the environment
source venv/bin/activate

# Install the requirements
pip3 install -r requirements.txt

# Start the application
python3 app.py
```

The application should now be running on [http://0.0.0.0:5000](http://0.0.0.0:5000).

## Project breakdown
This project is composed of two main parts. They are the web application and machine learning.

### Web application with Flask
The web application is quite simple. It contains only two endpoint defined using the [Flask](http://flask.pocoo.org/) micro-framework.

| Endpoint | HTTP Method | Description |
|----------|-------------|-------------|
| `/`      | GET         | Returns a static index.html file with a form for uploading an image to the `/image` endpoint and displaying the result |
| `/image` | POST        | Uses Tensorflow to detect a digit between 0 and 9 from a given image and return the result as JSON. |

### Machine learning with Tensorflow
This is the main aspect of this project. Tensorflow is used to detect a digit between 0 and 9 from an image. Before trying to solve this problem it is important to meantion what TensorFlow is and to also clearly define. 

#### What is TensorFlow?
TensorFlow is an open-source software library released in 2015 by Google. It is used for numerical computing and is based on the dataflow paradigm in which a program is modelled as a directed graph. The nodes in this graph represent mathematical operations, while the graph edges represent the data, or tensors, being passed between the nodes. A tensor in mathematics is a multidimensional data array. TensorFlow is applicable in many fields but it is primarily intended for machine learning because the graph in Tensorflow is essentially a neural network. While the human brain is effective at recognising patterns, it is a difficult challenge for a computer to solve. Neural networks try to overcome this challenge by modeling the human brain, where each node in the graph represents a single neuron. The following are the high level steps involved in using TensorFlow to solve a problem

##### 1) Analyse the data
The first step is to analyse the input data to the graph. How is the data set divided up? For example, the MNIST data set used by TensorFlow is split into three parts. They are 55,000 data points of training data, 10,000 points of test data, and 5,000 points of validation data, where each data point is an image with the dimensions 28px x 28px and a corresponding label between 0 and 9. What format is the data in? For example, the images in the MNIST data set aren't represented as 2D arrays but are instead flattened into a 1D array with 784 elements (28x28). It's important to understand the data set you will be dealing with.

##### 2) Build a model
The next step is to construct the model, or graph, in TensorFlow. The model you build will be directly related to the problem you want to solve and the algorithm you want to use. The model is created by creating nodes. Edges are created by using an existing node in the operation of a new node. Nodes with no incoming edges, meaning an in-degree of 0, are considered the start nodes. This is where the input data will enter the graph. There can be many start nodes. The node that is executed will output the result. It is also worth mentioning that a subgraph can be executed. In this case TensorFlow will walk backwards from the node that was executed and will only use the start nodes that have a path to the node that was executed. TensorFlow offers three types of nodes. The first is a constant node whose value is set when building the model and doesn't change. The second is a variable node whose value is set when the model is ran and whose value doesn't change during execution. The third type of node is a variable node whose value is set when the model is ran and can be changed by TensorFlow. The variable node is possibly the most important type of node as the aim of using TensorFlow is to get it to approximate the best values in these variable nodes.

##### 3) Train the model
Training is the process of adjusting the values in the variable nodes mentioned above. During the training phase the results should be known for each given input. For example, with the MNIST data set, if an image with the number 9 is the input to the model then we must know that 9 is the desired outcome. This is the purpose of the labels in the MNIST data set. Before being able to train a model we need a method to measure how good, or bad, the model is so that TensorFlow knows in what direction to change the variables, meaning should they be incremented or decremented. This is achieved using a cost function. The cost function will again depend on what problem you want to solve. This function determines how close the model is from the desired outcome. One algorithm used to train a model is Gradient descent. Gradient descent simply shifts each variable a little bit in the direction that reduces the cost. By training the model many times this cost function should get closer and closer to zero. Two variables to consider when training the model are the learning rate and the number of iterations it is trained. The learning rate is the proportional amount that each variable is changed on each iteration. If this learning rate is too low the model will take a long time to train. If this rate is too big it might never find the optimal values for the variables.

##### 4) Evaluate the model
We can evaluate our model based on its accuracy. We can do this by using test data. It is important that this test data is completely independent from the data used to train the model. However, like the training set we must know the outcome, or result, for each data point in the test set. To calculate the accuracy of a model we pass the test data through the model and compare the results to the expected outcome. From this we can then calculate the accuracy as a percentage.

#### What problem are we solving?

## Conclusion

### References
+ [TensorFlow](https://www.tensorflow.org/)
+ [TensorFlow MNIST tutorial](https://www.tensorflow.org/get_started/mnist/beginners)