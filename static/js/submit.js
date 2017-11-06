/*
 * Script for sending AJAX request on submission of form.
 * Output the result, either the digit or error message, to the page.
 * Adapted from from https://stackoverflow.com/questions/39716481/how-to-submit-multipart-formdata-using-jquery
 */
$(document).ready(function() {
	$('#upload-form').submit(function(event) {
		event.preventDefault();
		
		$('#text-result').val('Please wait...');
		
		var form = new FormData($('#upload-form')[0]);
		
		$.ajax({
			url: '/image',
			method: 'POST',
			dataType: 'json',
			data: form,
			processData: false,
			contentType: false,
			success: function(data) {
				if (data.status == 'error') {
					$('#text-result').val(data.message);
				} else {
					$('#text-result').val(data.result);
				}
			},
			error: function(data) {
				$('#text-result').val('An error has occured!');
			}
		});
	});
});