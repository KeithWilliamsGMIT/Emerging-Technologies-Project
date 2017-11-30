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
	var errorModal = $('#error-modal');
	
	$('#upload-form').submit(function(event) {
		event.preventDefault();
		
		waitText.show();
		
		postImageData('/image', successCallback, errorCallback);
	});
	
	function postImageData(url, successCallback, errorCallback) {
		// Get the index of the current tab.
		var index = $('a.nav-link.active').parent().index();
		
		if (index == 1) {
			var canvas = document.getElementById('canvas');
			var dataURL = canvas.toDataURL('image/png');
			
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
	
	function errorCallback(data) {
		errorModal.modal('show');
		errorText.text('An error has occured!');
		waitText.hide();
	}
	
	$('#right').click(function(event) {
		postImageData('/learn/' + resultsText.text(), null, errorCallback);
		closeResultModal();
	});
	
	$('#wrong').click(function(event) {
		closeResultModal();
	});
	
	function closeResultModal() {
		resultsModal.modal('hide');
		clear();
	}
});