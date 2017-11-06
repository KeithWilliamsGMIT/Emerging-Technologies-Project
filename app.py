# Author:		Keith Williams
# Date:			22/10/2017
# Description:	Retrieve and respond to HTTP requests.

from flask import Flask

app = Flask(__name__)

# Serve the index.html from the static folder.
@app.route('/')
def index():
	# Adapted from https://stackoverflow.com/questions/24578330/flask-how-to-serve-static-html
    return app.send_static_file('index.html')

# Run the application if this is the main module.
if __name__ == '__main__':
	# Turn on debug mode for the flask app (Adapted from https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app)
	app.debug = True
	
	# Start the application
	app.run()