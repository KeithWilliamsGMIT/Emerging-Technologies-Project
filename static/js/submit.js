/*
 * Script for sending AJAX request on submission of form.
 * Output the result, either the digit or error message, to the page.
 * Adapted from from https://stackoverflow.com/questions/39716481/how-to-submit-multipart-formdata-using-jquery
 */
$(document).ready(function() {
	var resultsTextbox = $('#text-result');
	
	$('#upload-form').submit(function(event) {
		event.preventDefault();
		
		$('#text-result').val('Please wait...');
		
		// Get the index of the current tab.
		var index = $('a.nav-link.active').parent().index();
		
		if (index == 1) {
			var canvas = document.getElementById('canvas');
			var dataURL = canvas.toDataURL('image/png');
			console.log(dataURL);
			
			$.ajax({
				url: '/image',
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
				url: '/image',
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
	});
	
	function successCallback(data) {
		if (data.status == 'error') {
			resultsTextbox.val(data.message);
		} else {
			resultsTextbox.val(data.result);
		}
	}
	
	function errorCallback(data) {
		resultsTextbox.val('An error has occured!');
	}
});