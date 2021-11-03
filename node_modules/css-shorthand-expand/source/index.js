var map = require('map-obj');

var font = require('./font');
var border = require('./border');
var borderRadius = require('./border-radius');
var background = require('./background');
var directional = require('./directional');
var outline = require('./outline');

var prefix = function(prefix) {
	return function(value) {
		var longhand = directional(value);

		return longhand && map(longhand, function(key, value) {
			return [prefix + '-' + key, value];
		});
	};
};

var shorthand = {
	font: font,
	padding: prefix('padding'),
	margin: prefix('margin'),
	border: border,
	'border-width': border.width,
	'border-style': border.style,
	'border-color': border.color,
	'border-top': border.top,
	'border-right': border.right,
	'border-bottom': border.bottom,
	'border-left': border.left,
	'border-radius': borderRadius,
	background: background,
	outline: outline
};

module.exports = function(property, value) {
	var normalized = value.trim();
	var important = /\s+!important$/.test(normalized);
	normalized = normalized.replace(/\s+!important$/, '');

	var parse = shorthand[property];
	var longhand = parse && parse(normalized);

	if(!longhand) return;
	if(!important) return longhand;

	return map(longhand, function(key, value) {
		return [key, value + ' !important'];
	});
};
