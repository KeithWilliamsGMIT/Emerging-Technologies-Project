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

##### 2) Build a model

##### 3) Train the model

##### 4) Evaluate the model

#### What problem are we solving?

## Conclusion

### References
+ [Tensorflow](https://www.tensorflow.org/)