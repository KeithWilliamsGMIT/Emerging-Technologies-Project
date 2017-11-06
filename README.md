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
This is the main part of the point. Tensorflow is used to detect a digit between 0 and 9 from an image.
