var LENGTH = /^(\+|-)?([0-9]*\.)?[0-9]+(em|ex|ch|rem|vh|vw|vmin|vmax|px|mm|cm|in|pt|pc|%)$/i;
var ZERO = /^(\+|-)?(0*\.)?0+$/;

module.exports = function(value) {
	return LENGTH.test(value) || ZERO.test(value);
};
