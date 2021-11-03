var map = require('map-obj');
var repeat = require('repeat-element');

var directional = function(value) {
	var values = value.split(/\s+/);

	if(values.length === 1) values = repeat(values[0], 4);
	else if(values.length === 2) values = values.concat(values);
	else if(values.length === 3) values.push(values[1]);
	else if(values.length > 4) return;

	return [
		'top-left',
		'top-right',
		'bottom-right',
		'bottom-left'
	].reduce(function(acc, direction, i) {
		acc[direction] = values[i];
		return acc;
	}, {});
};

var borderRadius = function(value) {
	var longhand = directional(value);

	return longhand && map(longhand, function(key, value) {
		return [ 'border-' + key + '-radius', value];
	});
}

module.exports = exports = borderRadius;
