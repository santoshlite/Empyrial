var map = require('map-obj');
var extend = require('xtend');
var isColor = require('./is-color');
var isLength = require('./is-length');
var normalize = require('./normalize-color');

var WIDTH = /^(thin|medium|thick)$/;
var STYLE = /^(none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset)$/i;
var KEYWORD = /^(inherit|initial)$/i;

var outline = function(value) {
	var values = normalize(value).split(/\s+/);

	if(values.length > 3) return;
	if (values.length === 1 && KEYWORD.test(values[0])) {
		return {
			'outline-width': values[0],
			'outline-style': values[0],
			'outline-color': values[0]
		};
	}

	var result = {};
	for(var i = 0; i < values.length; i++) {
		var v = values[i];

		if (isLength(v) || WIDTH.test(v)) {
			if(result['outline-width']) return;
			result['outline-width'] = v;
		} else if (STYLE.test(v)) {
			if(result['outline-style']) return;
			result['outline-style'] = v;
		} else if (isColor(v)) {
			if(result['outline-color']) return;
			result['outline-color'] = v;
		} else {
			return;
		}
	};

	return result;
};

module.exports = exports = outline;
