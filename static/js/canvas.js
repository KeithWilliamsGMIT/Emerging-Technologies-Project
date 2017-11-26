/*
 * Script for drawing on the HTML5 canvas.
 * Adapted from
 *	- https://stackoverflow.com/questions/2368784/draw-on-html5-canvas-using-a-mouse
 *	- https://www.codicode.com/art/how_to_draw_on_a_html5_canvas_with_a_mouse.aspx
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
        ctx.strokeStyle = 'white';
        ctx.lineWidth = 15;
        ctx.lineJoin = 'round';
        ctx.moveTo(prevX, prevY);
        ctx.lineTo(currX, currY);
        ctx.closePath();
        ctx.stroke();
	}
	
	function clear() {
		ctx.fillStyle = 'black';
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