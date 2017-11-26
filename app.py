# Author:		Keith Williams
# Date:			22/10/2017
# Description:	Retrieve and respond to HTTP requests.

import tensorflow as tf
import numpy as np
import base64
import re

from flask import Flask, request
from json import dumps
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Set of extensions that determine what files can be sent to the /image endpoint.
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# Serve the index.html from the static folder.
@app.route('/')
def index():
	# Adapted from https://stackoverflow.com/questions/24578330/flask-how-to-serve-static-html
    return app.send_static_file('index.html')

# POST an image file containing a single digit between 0 and 9.
# Return the digit as JSON.
# Adapted from http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
@app.route('/image', methods=['POST'])
def post_image():
	response = {'status': 'error', 'message': '', 'result': '-1'}
	
	# Check if the post request has the file part.
	if 'image' in request.files:
		image = request.files['image']

		# If the user does not select a file, the browser will submit an empty part without a filename.
		if image.filename == '':
			# ERROR: Image part is empty!
			response['message'] = 'Image part is empty!'

		if image and '.' in image.filename and image.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
			# Return digit in image.
			response['status'] = 'success'
			response['result'] = get_digit(image)
		else:
			# ERROR: Invalid file format!
			response['message'] = 'Invalid file format!'
	
	elif request.values['imageBase64'] is not None:
		b64 = request.values['imageBase64']
		b64 = re.sub('^data:image/.+;base64,', '', b64)
		image = base64.decodestring(b64.encode('ascii'))
		
		# Return digit in image.
		response['status'] = 'success'
		response['result'] = get_digit(BytesIO(base64.b64decode(b64)))
	else:
		# ERROR: No image found!
		response['message'] = 'No image found!'
	
	return dumps(response)

# Convert the image to the correct format.
# Use the TensorFlow model to detect the digit in the model.
# Return the digit.
def get_digit(image):
	# Resize image and convert it to greyscale using PIL.
	# Adapted from https://stackoverflow.com/questions/1109422/getting-list-of-pixel-values-from-pil
	img = Image.open(image)
	img = img.resize((28, 28))
	img = img.convert('L')
	
	# Convert the pixels to a 1D array using Numpy so that the image is represented by an array with 784 elements.
	# Therefore, each element represents a single pixel value between 0 and 255.
	pixels = np.asarray(img.getdata()).reshape(1, 784)
	
	# Restore the saved model.
	sess = tf.Session()
	saver = tf.train.import_meta_graph('./models/digit-model.meta')
	saver.restore(sess, tf.train.latest_checkpoint('./models/'))
	
	# Detect the digit in the image using the restored model.
	# First get an estimate as a one-hot vector.
	one_hot = sess.run('y_conv:0', feed_dict={'x:0': pixels, 'keep_prob:0': 1.0})
	
	# Then get the estimate as a number between 0 and 9 (index of highest value).
	classification = tf.argmax(one_hot, 1)
	
	# Return the estimate as a number between 0 and 9.
	return str(sess.run(classification)[0])
	
# Run the application if this is the main module.
if __name__ == '__main__':
	# Turn on debug mode for the flask app (Adapted from https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app)
	app.debug = True
	
	# Start the application
	app.run()