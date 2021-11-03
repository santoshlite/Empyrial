/**
 Copied from https://github.com/bramstein/css-font-parser
 */

/**
 * @enum {number}
 */
var states = {
	VARIATION: 1,
	LINE_HEIGHT: 2,
	FONT_FAMILY: 3
};

/**
 * @param {string} input
 * @return {Object}
 */
function parse(input) {
	var state = states.VARIATION,
			buffer = '',
			result = {
				'font-family': []
			};

	for (var c, i = 0; c = input.charAt(i); i += 1) {
		if (state === states.FONT_FAMILY && (c === '"' || c === "'")) {
			var index = i + 1;

			// consume the entire string
			do {
				index = input.indexOf(c, index) + 1;
				if (!index) {
					// If a string is not closed by a ' or " return null.
					// TODO: Check to see if this is correct.
					return null;
				}
			} while (input.charAt(index - 2) === '\\');

			result['font-family'].push(input.slice(i + 1, index - 1).replace(/\\('|")/g, "$1"));

			i = index - 1;
			buffer = '';
		} else if (state === states.FONT_FAMILY && c === ',') {
			if (!/^\s*$/.test(buffer)) {
				result['font-family'].push(buffer.replace(/^\s+|\s+$/, '').replace(/\s+/g, ' '));
				buffer = '';
			}
		} else if (state === states.VARIATION && (c === ' ' || c === '/')) {
			if (/^((xx|x)-large|(xx|s)-small|small|large|medium)$/.test(buffer) ||
					/^(larg|small)er$/.test(buffer) ||
					/^(\+|-)?([0-9]*\.)?[0-9]+(em|ex|ch|rem|vh|vw|vmin|vmax|px|mm|cm|in|pt|pc|%)$/.test(buffer)) {
				state = c === '/' ? states.LINE_HEIGHT : states.FONT_FAMILY;
				result['font-size'] = buffer;
			} else if (/^(italic|oblique)$/.test(buffer)) {
				result['font-style'] = buffer;
			} else if (/^small-caps$/.test(buffer)) {
				result['font-variant'] = buffer;
			} else if (/^(bold(er)?|lighter|normal|[1-9]00)$/.test(buffer)) {
				result['font-weight'] = buffer;
			} else if (/^((ultra|extra|semi)-)?(condensed|expanded)$/.test(buffer)) {
				result['font-stretch'] = buffer;
			}
			buffer = '';
		} else if (state === states.LINE_HEIGHT && c === ' ') {
			if (/^(\+|-)?([0-9]*\.)?[0-9]+(em|ex|ch|rem|vh|vw|vmin|vmax|px|mm|cm|in|pt|pc|%)?$/.test(buffer)) {
				result['line-height'] = buffer;
			}
			state = states.FONT_FAMILY;
			buffer = '';
		} else {
			buffer += c;
		}
	}

	if (state === states.FONT_FAMILY && !/^\s*$/.test(buffer)) {
		result['font-family'].push(buffer.replace(/^\s+|\s+$/, '').replace(/\s+/g, ' '));
	}

	if (result['font-size'] && result['font-family'].length) {
		return result;
	} else {
		return null;
	}
}

module.exports = function(input) {
	if(/^(inherit|initial)$/.test(input)) {
		return {
			'font-size': input,
			'line-height': input,
			'font-style': input,
			'font-weight': input,
			'font-variant': input,
			'font-stretch': input,
			'font-family': input
		}
	}

	input = input.replace(/\s*\/\s*/, '/');
	var result = parse(input);

	if(result) {
		result['font-family'] = result['font-family'].map(function(family) {
			return /^(serif|sans-serif|monospace|cursive|fantasy)$/.test(family) ? family : ('"' + family + '"');
		}).join(', ');
	}

	return result;
};
