/*
 * Script for sending AJAX request on submission of form.
 * Output the result, either the digit or error message, to the page.
 * Adapted from from https://stackoverflow.com/questions/39716481/how-to-submit-multipart-formdata-using-jquery
 */
$(document).ready(function() {
	var waitText = $('#text-wait');
	var resultsText = $('#text-result');
	var errorText = $('#text-error');
	var resultsModal = $('#results-modal');
	var wrongResultText = $('#wrong-result-modal');
	var errorModal = $('#error-modal');
	
	/*
	 * Called when the form is submitted.
	 * Stop the page from being reloaded and send an image to the API.
	 */
	$('#upload-form').submit(function(event) {
		event.preventDefault();
		
		waitText.show();
		
		postImageData('/image', successCallback, errorCallback);
	});
	
	/*
	 * Post image data to the given url.
	 * This image can either be from a HTML form or encoded as a base64 string.
	 */
	function postImageData(url, successCallback, errorCallback) {
		// Get the index of the current tab.
		var index = $('a.nav-link.active').parent().index();
		
		if (index == 1) {
			var canvas = document.getElementById('canvas');
			var dataURL = canvas.toDataURL('image/png');
			
			// Send the canvas image as a base64 encoded string in JSON format.
			$.ajax({
				url: url,
				method: 'POST',
				dataType: 'json',
				data: {
					imageBase64: dataURL
				},
				success: function(data) {
					successCallback(data);
				},
				error: function(data) {
					errorCallback(data);
				}
			});
		} else {
			var form = new FormData($('#upload-form')[0]);
			
			// Send the image as part of the form.
			$.ajax({
				url: url,
				method: 'POST',
				dataType: 'json',
				data: form,
				processData: false,
				contentType: false,
				success: function(data) {
					successCallback(data);
				},
				error: function(data) {
					errorCallback(data);
				}
			});
		}
	}
	
	/*
	 * Called when the AJAX request is successful.
	 * There are two possible outcomes.
	 * If the status returned from the API is 'succes', show the result modal.
	 * This modal will display the digit the modal predicted and will give the user an option of verifying if it was right.
	 * If the status is 'error', show the error modal.
	 * This modal simply displays an error message returned from the API.
	 */
	function successCallback(data) {
		if (data.status == 'error') {
			errorModal.modal('show');
			errorText.text(data.message);
		} else {
			resultsModal.modal('show');
			resultsText.text(data.result);
		}
		
		waitText.hide();
	}
	
	/*
	 * Called when the AJAX request is successful.
	 * The error modal is shown with a predefined error message.
	 */
	function errorCallback(data) {
		errorModal.modal('show');
		errorText.text('An error has occured!');
		waitText.hide();
	}
	
	/*
	 * Called when the 'right' button is clicked.
	 * This means that the user determined that the prediction from the model was correct.
	 * Send the image back to the API with the correct label to train the model.
	 * Close the modal.
	 */
	$('#right').click(function(event) {
		var label = resultsText.text();
		resultsText.text('Training the model...');
		
		postImageData('/learn/' + label, function(data) {
			resultsModal.modal('hide');
			clear();
		}, errorCallback);
	});
	
	/*
	 * Called when the 'wrong' button is clicked.
	 * Close the modal.
	 */
	$('#wrong').click(function(event) {
		resultsModal.modal('hide');
		wrongResultText.modal('show');
	});
	
	/*
	 * Called when the user chooses the correct label.
	 * Close the modal.
	 */
	$('#correct-labels').on('click', function(event) {
		var label = $(event.target).text();
		
		postImageData('/learn/' + label, function(data) {
			wrongResultText.modal('hide');
			clear();
		}, errorCallback);
	});
});