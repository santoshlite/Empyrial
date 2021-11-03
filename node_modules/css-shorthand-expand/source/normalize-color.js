var hsla = require('hsla-regex');
var hsl = require('hsl-regex');
var rgb = require('rgb-regex');
var rgba = require('rgba-regex');

var FUNCTIONS = [
	hsla(),
	hsl(),
	rgb(),
	rgba()
];

module.exports = function(value) {
	return FUNCTIONS.reduce(function(acc, func) {
		return acc.replace(func, function(match) {
			return match.replace(/\s+/g, '');
		});
	}, value);
};
