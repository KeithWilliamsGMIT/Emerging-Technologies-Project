# Author:		Keith Williams
# Date:			22/10/2017
# Description:	Retrieve and respond to HTTP requests.

import numpy as np
from flask import Flask, request
from json import dumps
from PIL import Image

from tensorflow_model import get_digit_from_image

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
	# Check if the post request has the file part.
	if 'image' not in request.files:
		# ERROR: Request does not contain part called 'image'!
		return dumps({'status': 'error', 'message': 'Request does not contain part called image!'})

	image = request.files['image']

	# If the user does not select a file, the browser will submit an empty part without a filename.
	if image.filename == '':
		# ERROR: Image part is empty!
		return dumps({'status': 'error', 'message': 'Image part is empty!'})

	if image and '.' in image.filename and image.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
		# Resize image and convert it to greyscale using PIL.
		# Adapted from https://stackoverflow.com/questions/1109422/getting-list-of-pixel-values-from-pil
		img = Image.open(image)
		img = img.resize((28, 28))
		img = img.convert('L')
		
		# Convert the pixels to a 1D array using Numpy
		pixels = np.asarray(img.getdata()).reshape(1, 784)
		
		# Detect digit in image and return the result.
		result = get_digit_from_image(pixels);
		return dumps({'status': 'success', 'result': result})
	else:
		# ERROR: Invalid file format!
		return dumps({'status': 'error', 'message': 'Invalid file format!'})

# Run the application if this is the main module.
if __name__ == '__main__':
	# Turn on debug mode for the flask app (Adapted from https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app)
	app.debug = True
	
	# Start the application
	app.run()