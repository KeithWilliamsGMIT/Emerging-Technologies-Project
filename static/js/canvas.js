/*
 * Script for drawing on the HTML5 canvas.
 * Adapted from https://stackoverflow.com/questions/2368784/draw-on-html5-canvas-using-a-mouse
 */
$(document).ready(function() {
	var canvas, ctx, flag = false;
	var prevX = 0, currX = 0, prevY = 0, currY = 0;
	
	function init() {
		canvas = document.getElementById('canvas');
		ctx = canvas.getContext('2d');
		w = canvas.width;
		h = canvas.height;

		canvas.addEventListener('mousemove', function (e) {
			findxy('move', e)
		}, false);

		canvas.addEventListener('mousedown', function (e) {
			findxy('down', e)
		}, false);

		canvas.addEventListener('mouseup', function (e) {
			findxy('up', e)
		}, false);

		canvas.addEventListener('mouseout', function (e) {
			findxy('out', e)
		}, false);
		
		// Remove transparent background.
		clear();
	}
	
	function draw() {
		ctx.beginPath();
		ctx.moveTo(prevX, prevY);
		ctx.lineTo(currX, currY);
		ctx.strokeStyle = 'black';
		ctx.lineWidth = 5;
		ctx.stroke();
		ctx.closePath();
	}
	
	function clear() {
		ctx.fillStyle = 'white';
		ctx.fillRect(0, 0, canvas.width, canvas.height);
	}
	
	function findxy(res, e) {
		if (res == 'down') {
			updateCoordinates(e);
			flag = true;
		}
		
		if (res == 'up' || res == 'out') {
			flag = false;
		}
		
		if (res == 'move') {
			if (flag) {
				updateCoordinates(e);
				draw();
			}
		}
	}
	
	function updateCoordinates(e) {
		prevX = currX;
		prevY = currY;
		
		// Adapted from https://stackoverflow.com/questions/20857593/canvas-mouse-event-position-different-than-cursor
		currX = e.clientX - canvas.getBoundingClientRect().left;
		currY = e.clientY - canvas.getBoundingClientRect().top;
	}
	
	init();
	
	$('#clear').click(function() {
		clear();
	});
});