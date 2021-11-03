var map = require('map-obj');
var extend = require('xtend');
var directional = require('./directional');
var isColor = require('./is-color');
var isLength = require('./is-length');
var normalize = require('./normalize-color');

var WIDTH = /^(thin|medium|thick)$/;
var STYLE = /^(none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset)$/i;
var KEYWORD = /^(inherit|initial)$/i;

var suffix = function(suffix) {
	return function(value) {
		var longhand = directional(value);

		return longhand && map(longhand, function(key, value) {
			return ['border-' + key + '-' + suffix, value];
		});
	};
};

var direction = function(direction) {
	return function(value) {
		var longhand = all(value);

		return longhand && map(longhand, function(key, value) {
			return ['border-' + direction + '-' + key, value];
		});
	};
};

var all = function(value) {
	var values = normalize(value).split(/\s+/);
	var first = values[0];

	if(values.length > 3) return;
	if(values.length === 1 && KEYWORD.test(first)) {
		return {
			width: first,
			style: first,
			color: first
		};
	}

	var result = {};
	for(var i = 0; i < values.length; i++) {
		var v = values[i];

		if(WIDTH.test(v) || isLength(v)) {
			if(result.width) return;
			result.width = v;
		} else if(STYLE.test(v)) {
			if(result.style) return;
			result.style = v;
		} else if(isColor(v)) {
			if(result.color) return;
			result.color = v;
		} else {
			return;
		}
	}

	return result;
};

var border = function(value) {
	var longhand = all(value);

	return longhand && Object.keys(longhand)
		.reduce(function(acc, key) {
			var props = exports[key](longhand[key]);
			return extend(acc, props);
		}, {});
};

border.width = suffix('width');
border.style = suffix('style');
border.color = suffix('color');
border.top = direction('top');
border.right = direction('right');
border.bottom = direction('bottom');
border.left = direction('left');

module.exports = exports = border;
