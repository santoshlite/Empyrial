var hex = require('hex-color-regex');
var hsla = require('hsla-regex');
var hsl = require('hsl-regex');
var rgb = require('rgb-regex');
var rgba = require('rgba-regex');
var keywords = require('css-color-names');

var HEX = new RegExp('^' + hex().source + '$', 'i');
var HSLA = hsla({ exact: true });
var HSL = hsl({ exact: true });
var RGB = rgb({ exact: true });
var RGBA = rgba({ exact: true });

module.exports = function(value) {
	value = value.toLowerCase();

	return !!keywords[value] ||
		value === 'currentcolor' ||
		value === 'transparent' ||
		HEX.test(value) ||
		HSLA.test(value) ||
		HSL.test(value) ||
		RGB.test(value) ||
		RGBA.test(value);
};
