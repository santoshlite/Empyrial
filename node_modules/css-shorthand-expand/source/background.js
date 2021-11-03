var url = require('css-url-regex');
var map = require('map-obj');
var isColor = require('./is-color');
var isLength = require('./is-length');
var normalizeColor = require('./normalize-color');

var ATTACHMENT = /^(fixed|local|scroll)$/;
var BOX = /^(border-box|padding-box|content-box)$/;
var IMAGE = new RegExp('^(none|' + url().source + ')$', 'i');
var REPEAT_SINGLE = /^(repeat-x|repeat-y)$/i;
var REPEAT_DOUBLE = /^(repeat|space|round|no-repeat)$/i;
var POSITION_HORIZONTAL = /^(left|center|right)$/;
var POSITION_VERTICAL = /^(top|center|bottom)$/;
var SIZE_SINGLE = /^(cover|contain)$/;
var KEYWORD = /^(inherit|initial)$/i;

var normalizeUrl = function(value) {
	return value.replace(url(), function(match) {
		return match
			.replace(/^url\(\s+/, 'url(')
			.replace(/\s+\)$/, ')');
	});
};

module.exports = function(value) {
	var result = {};
	var values = normalizeUrl(normalizeColor(value))
		.replace(/\(.*\/.*\)|(\/)+/g, (match, group1) => (!group1) ? match : ' / ')
		.split(/\s+/);

	var first = values[0];

	if(values.length === 1 && KEYWORD.test(first)) {
		return {
			'background-attachment': first,
			'background-clip': first,
			'background-image': first,
			'background-repeat': first,
			'background-color': first,
			'background-position': first,
			'background-size': first
		};
	}

	for(var i = 0; i < values.length; i++) {
		var v = values[i];

		if(ATTACHMENT.test(v)) {
			if(result.attachment) return;
			result.attachment = v;
		} else if(BOX.test(v)) {
			if(result.clip) return;
			result.clip = v;
		} else if(IMAGE.test(v)) {
			if(result.image) return;
			result.image = v;
		} else if(REPEAT_SINGLE.test(v)) {
			if(result.repeat) return;
			result.repeat = v;
		} else if(REPEAT_DOUBLE.test(v)) {
			if(result.repeat) return;

			var n = values[i + 1];

			if(n && REPEAT_DOUBLE.test(n)) {
				v += ' ' + n;
				i++;
			}

			result.repeat = v;
		} else if(isColor(v)) {
			if(result.color) return;
			result.color = v;
		} else if(POSITION_HORIZONTAL.test(v) || POSITION_VERTICAL.test(v) || isLength(v)) {
			if(result.position) return;

			var n = values[i + 1];
			var isHorizontal = POSITION_HORIZONTAL.test(v) || isLength(v);
			var isVertical = POSITION_VERTICAL.test(n) || isLength(n);

			if(isHorizontal && isVertical) {
				result.position = v + ' ' + n;
				i++;
			} else {
				result.position = v;
			}

			v = values[i + 1];

			if(v === '/') {
				i += 2;
				v = values[i];

				if(SIZE_SINGLE.test(v)) {
					result.size = v;
				} else if(v === 'auto' || isLength(v)) {
					n = values[i + 1];

					if(n === 'auto' || isLength(n)) {
						v += ' ' + n;
						i++;
					}

					result.size = v;
				} else {
					return;
				}
			}
		} else {
			return;
		}
	}

	return map(result, function(key, value) {
		return ['background-' + key, value];
	});
};
