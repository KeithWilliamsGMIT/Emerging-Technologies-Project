# Emerging Technologies Project
> Name - Keith Williams  
  ID - G00324844

This is my 4th year project for the emerging technologies module in college. For this project I was tasked with creating a Python web application to recognise digits in images. Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image. This application will use Tensorflow and Flask.

## Getting started
First ensure you have Python 3 installed. The easiest way to install Python is through [Anaconda](https://www.anaconda.com/downloads). Next create a virtual environment in the app folder to store all the required packages. Once created, activate the new environment using the `source` command and install the packages listed in the `requirements.txt` file. Then, train and save the TensorFlow model by running the `tensorflow_model.py` script. Note that this script can take up to 40 minutes to run. Therefore, for the purposes of this project, I included the binary files in the repository, which removes the need to run this script. Usually these files are not included. This will create a new folder called models. Finally, start the application. You can use the below commands.

```
# Create the virtual environment
virtualenv -p python3 venv

# Activate the environment
source venv/bin/activate

# Install the requirements
pip3 install -r requirements.txt

# Train and save model (Optional)
python3 tensorflow_model.py

# Start the application
python3 app.py
```

The application should now be running on [http://0.0.0.0:5000](http://0.0.0.0:5000).

## Project breakdown
The following are the instructions for this project.
+ Create a git repository with a README.md and an appropriate gitignore file. The README should explain who you are, why you created the application, how you created it, how to download and run it, and summarise any references you have used.
+ In the repository, create a web application that serves a HTML page as the root resource. The page should contain an input where the user can upload (or draw) an image containing a digit, and an area to display the image and the digit.
+ Add a route to your application that accepts requests containing a user input image and responds with the digit.
+ Connect the HTML page to the route using AJAX.

From these instructions we can break the project into two main parts. They are the web application and machine learning.

### Web application with Flask
The web application is quite simple. It contains only three endpoints defined using the [Flask](http://flask.pocoo.org/) micro-framework.

| Endpoint         | HTTP Method | Description |
|------------------|-------------|-------------|
| `/`              | GET         | Returns a static index.html file with a form for uploading an image to the `/image` endpoint and displaying the result |
| `/image`         | POST        | Uses Tensorflow to detect a digit between 0 and 9 from a given image and return the result as JSON. |
| `/learn/<label>` | POST        | Post an image along with the correct label to further train the model (Experimental). |

This web application allows the user to either browse for an image to upload or draw an image using the HTML5 canvas. There are a number of JavaScript files used to make the web application interactive. These have been heavily adapted from different sources. JQuery is also used for performing AJAX requests and manipulating the DOM (Document Object Model). Bootstrap 4, with the help of a custom CSS file, is used for styling the web application.

The reason the canvas has a black background is because all the images in the MNIST data set, including those used to train the model, had a black grackground and white foreground. Therefore, having the canvas mimic these images returns the best results.

### Machine learning with Tensorflow
Due to the amount of material on TensorFlow and machine learning, I decided to split this section across a number of Jupyter notebooks. To get started, open a terminal and navigate to the root of this repository and then run the following commands.

```
cd notebooks
jupyter notebook
```

Start with the notebook named `research.ipynb`.

## Extra features
Additional features added to this project include:

1. Continuous learning  
The API provided by the application provides an additional endpoint, that was not required in the project specification, which allows users to further train the model. The users of the web application are presented with this option after they submit an image to get a digit from. They are asked is the prediction is right or wrong. If they say the prediction was right, then the image is sent back to the API, with the correct label, and is used to further train the model. If the user says that it is wrong they will be asked to choose the correct label before sending back the image to train the model. One disadvantage of this is that if users repeatively decide that the prediction is right, when it was actually wrong, the accuracy of the model will suffer.

2. Hosted web application  
For demonstration purposes I decided to host the web application for this project on Heroku. The web application is available at [https://emerging-technologies-project.herokuapp.com/](https://emerging-technologies-project.herokuapp.com/).

## Conclusion
MNIST is a common data set used to demonstrate and teach machine learning. After completing this project I've gained a better understanding of TensorFlow, and machine learning in general. By breaking down the subject of machine learning into its smaller components, it made this project much more managable. These components include analysing the data, building the model, training the model and evaluating the model. The web application aspect of this project was relatively straightforward as the Flask framework was covered in a previous module. The use of Jupyter notebooks aided both the development and documentation of the TensorFlow model.

While there is still a lot of theory to cover on the topic of machine learning, I learned enough to be able to implement a model in TensorFlow capable of recognising a handwritten digit in an image. This model has an accuracy of over 99%. While this isn't state of the art for the MNIST problem, it is considered respectable.

### References
+ [TensorFlow](https://www.tensorflow.org/)
+ [TensorFlow MNIST for beginners tutorial](https://www.tensorflow.org/get_started/mnist/beginners)
+ [TensorFlow deep MNIST for experts tutorial](https://www.tensorflow.org/get_started/mnist/pros)
+ [Flask micro-framework](http://flask.pocoo.org/)