/*
Copyright (c) 2012 Greg Reimer
http://obadger.com/
"gregreimer" "at" "gmail" "dot" "com"

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

/* ########################################################################## */

/*
This library exposes window.Turte, which is a constructor for a turtle graphics
environment. Pass a canvas element to the constructor, like so:

    var canvas = document.getElementById('mycanvas');
    var t = new Turtle(canvas);

...then call methods on the "t" variable, like so:

    t.fd(100).lt(90); // forward 100px, left turn 90deg

...and a drawing will subsequently be drawn onto the canvas.
*/

window.Turtle = function(canvas){

	var slice = [].slice;

	var ctx = canvas.getContext("2d");
	var canvasWidth = canvas.width;
	var canvasHeight = canvas.height;
	ctx.lineCap = 'round';

	var T = this;

	// bits of unchanging info
	var defaultFg = '#fff';
	var defaultBg = '#222';
	var defaultWidth = '1';
	var origin = {
		x: Math.floor(canvasWidth / 2) + .5,
		y: Math.floor(canvasHeight / 2) + .5
	};

	// bits of info that change
	var foreground = defaultFg;
	var background = defaultBg;
	var width = width;
	var penDown = true;
	var pos = {};
	var heading = 0;

	// general purpose line drawing method, no rotation
	var go = (function(){
		var oldX = undefined;
		var oldY = undefined;
		var oldFg = undefined;
		var oldWidth = undefined;
		return function(args){
			ctx.beginPath();
			if (args.fg !== oldFg) {
				ctx.strokeStyle = args.fg;
				oldFg = args.fg;
			}
			if (args.width !== oldWidth) {
				ctx.lineWidth = args.width;
				oldWidth = args.width;
			}
			ctx.moveTo(oldX, oldY);
			ctx.lineTo(args.x, args.y);
			if (args.pd) {
				ctx.stroke();
			}
			oldX = args.x;
			oldY = args.y;
			trigger('move', args);
		};
	})();

	// queueing function
	var q = (function(){	
		var funs = [];
		var at = 0;
		(function run(){
			var len = funs.length - at;
			if (len > 0) {
				if (len > 500) {
					// for really long runs, batch actions together
					for (var i=0; i<len/250; i++) {
						funs[at++]();
					}
				} else {
					// otherwise one action at a time
					funs[at++]();
				}
				setTimeout(run,0);
			} else {
				if (funs.length > 0){
					funs = [];
					at = 0;
				}
				setTimeout(run, 200);
			}
		})();
		return function(fun){
			funs.push(fun);
		}
	})();

	// ######################################################
	// event handlers
	var events = {};
	T.on = function(ev, handler){
		var handlers = events[ev];
		if (!handlers) { handlers = events[ev] = []; }
		handlers.push(handler);
	};
	function trigger(ev){
		var args = slice.call(arguments);
		args.shift();
		var handlers = events[ev];
		if (handlers) {
			for (var i=0; i<handlers.length; i++) {
				handlers[i].apply(T, args);
			}
		}
	}

	// ######################################################
	// move forward, back
	T.fd = function(amount) {
		pos.x += Math.sin(heading) * -amount;
		pos.y += Math.cos(heading) * -amount;
		var args = {
			x:pos.x,
			y:pos.y,
			pd:penDown,
			width:width,
			fg:foreground
		};
		q(function(){ go(args); });
		return T;
	};
	T.bk = function(amount) {
		return T.fd(-amount);
	};

	// ######################################################
	// move to absolute positions
	function xy(x,y){
		pos.x = x;
		pos.y = y;
		var args = {
			x:pos.x,
			y:pos.y,
			pd:penDown,
			width:width,
			fg:foreground
		};
		q(function(){ go(args); });
	}
	T.xy = function(x, y){
		xy(origin.x+x, origin.y-y);
		return T;
	};
	T.x = function(x){
		xy(origin.x+x, pos.y);
		return T;
	};
	T.y = function(y){
		xy(pos.x, origin.y-y);
		return T;
	};
	T.heading = function(deg){
		heading = -deg * (Math.PI/180);
		var absDeg = T.get.heading();
		q(function(){
			trigger('rotate', absDeg);
		});
		return T;
	};
	T.face = function(x, y){
		y = -y;
		y += origin.y;
		x += origin.x;
		heading = Math.atan2(pos.x - x, pos.y - y);
		var absDeg = heading * (180/Math.PI);
		q(function(){
			trigger('rotate', absDeg);
		});
		return T;
	};
	T.butt = function(x, y){
		y = -y;
		y += origin.y;
		x += origin.x;
		heading = Math.atan2(pos.x - x, pos.y - y) + Math.PI;
		var absDeg = heading * (180/Math.PI);
		q(function(){
			trigger('rotate', absDeg);
		});
		return T;
	};

	// ######################################################
	// circular things
	T.disc = function(radius){
		var x = pos.x;
		var y = pos.y;
		q(function(){
			ctx.beginPath();
			ctx.fillStyle = foreground;
			ctx.arc(x, y, radius, 0, 2*Math.PI, true);
			ctx.fill();
		});
		return T;
	};
	T.circle = function(radius){
		var x = pos.x;
		var y = pos.y;
		q(function(){
			ctx.beginPath();
			ctx.strokeStyle = foreground;
			ctx.arc(x, y, radius, 0, 2*Math.PI, true);
			ctx.stroke();
		});
		return T;
	};

	// ######################################################
	// left turn, right turn
	T.rt = function(deg) {
		var delta = deg * (Math.PI/180);
		heading -= delta;
		var absDeg = T.get.heading();
		q(function(){
			trigger('rotate', absDeg);
		});
		return T;
	};
	T.lt = function(deg) {
		return T.rt(-deg);
	};

	// ######################################################
	// pen up, pen down
	T.pu = function() {
		penDown = false;
		q(function(){ trigger('pu'); });
		return T;
	};
	T.pd = function() {
		penDown = true;
		q(function(){ trigger('pd'); });
		return T;
	};

	// ######################################################
	// misc
	T.color = function(color) {
		foreground = color;
		return T;
	};
	T.thickness = function(aWidth){
		width = aWidth;
		return T;
	};
	T.clean = function(color){
		if (color) background = color;
		var bg = background;
		q(function(){
			ctx.fillStyle = bg;
			ctx.clearRect(0, 0, canvasWidth, canvasHeight);
			ctx.fillRect(0, 0, canvasWidth, canvasHeight);
		});
		return T;
	};
	T.home = function(){
		heading = 0;
		pos.x = origin.x;
		pos.y = origin.y;
		var args = {
			x:pos.x,
			y:pos.y,
			pd:false,
			width:width,
			fg:foreground
		};
		q(function(){
			go(args);
			trigger('rotate', 0);
		});
		return T;
	};
	T.clear = function(){
		return T
		.clean()
		.home()
		.pd();
	};
	T.reset = T.init = function(){
		background = defaultBg;
		return T
		.color(defaultFg)
		.thickness(defaultWidth)
		.clear();
	};

	// ######################################################
	// loopers
	T.repeat = function(amount, fun){
		for (var i=0; i<amount; i++) {
			var result = fun.call(T, i);
			if (!result && result !== undefined) break;
		}
		return T;
	};
	T.forever = function(fun){
		var i = 0;
		while (true) {
			var result = fun.call(T, i);
			if (!result && result !== undefined) break;
			i++;
		}
		return T;
	};

	// ######################################################
	// misc getters
	T.get = {
		x: function(){
			return pos.x - origin.x;
		},
		y: function(){
			return origin.y - pos.y;
		},
		heading: function(){
			return -heading * (180/Math.PI);
		},
		pu: function(){
			return !penDown;
		},
		pd: function(){
			return penDown;
		},
		thickness: function(){
			return width;
		},
		color: function(){
			return foreground;
		},
		background: function(){
			return background;
		},
		oob: function(){
			return pos.x > canvasWidth
				|| pos.y > canvasHeight
				|| pos.x < 0
				|| pos.y < 0;
		},
		top: function(){ return origin.y; },
		left: function(){ return -origin.x; },
		right: function(){ return origin.x; },
		bottom: function(){ return -origin.y; }
	};

	var normal = (function(){
		var _u, _v;
		function generate() {
			while (true) {
				var u = (2 * Math.random()) - 1;
				var v = (2 * Math.random()) - 1;
				var r = u*u + v*v;
				/*if outside interval [0,1] start over*/
				if(r === 0 || r >= 1) continue;

				var c = Math.sqrt(-2 * Math.log(r) / r);
				_u = u*c, _v = v*c;
				return;
			}
		}
		return function(){
			var result;
			if (_u === undefined && _v === undefined) generate();
			if (_u !== undefined) result = _u, _u = undefined;
			else                  result = _v, _v = undefined;
			return result;
		};
	})();

	T.rand = {
		uni:function(lower, upper){
			if (upper === undefined) upper = lower, lower = 0;
			var diff = upper - lower;
			return Math.random() * diff + lower;
		},
		norm:function(mean, stdDev){
			return mean + (normal() * stdDev);
		},
		chance:function(odds){
			return Math.random() < odds;
		}
	};




	// init this turtle
	T.init();
};





