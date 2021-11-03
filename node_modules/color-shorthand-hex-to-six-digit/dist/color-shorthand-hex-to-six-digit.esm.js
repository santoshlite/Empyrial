/**
 * color-shorthand-hex-to-six-digit
 * Convert shorthand hex color codes into full
 * Version: 3.0.7
 * Author: Roy Revelt, Codsen Ltd
 * License: MIT
 * Homepage: https://codsen.com/os/color-shorthand-hex-to-six-digit/
 */

import r from 'hex-color-regex';
import isPlainObject from 'lodash.isplainobject';
import clone from 'lodash.clonedeep';

var version$1 = "3.0.7";

const version = version$1;
function conv(originalInput) {
  let input = clone(originalInput);
  function toFullHex(hex, _findings, offset, string) {
    if (string[offset - 1] !== "&" &&
    hex.length === 4 && hex.charAt(0) === "#") {
      return `#${hex.charAt(1)}${hex.charAt(1)}${hex.charAt(2)}${hex.charAt(2)}${hex.charAt(3)}${hex.charAt(3)}`.toLowerCase();
    }
    return hex.toLowerCase();
  }
  if (typeof originalInput === "string") {
    input = input.replace(r(), toFullHex);
  } else if (Array.isArray(input)) {
    for (let i = 0, len = input.length; i < len; i++) {
      input[i] = conv(input[i]);
    }
  } else if (isPlainObject(originalInput)) {
    Object.keys(input).forEach(key => {
      input[key] = conv(input[key]);
    });
  } else {
    return originalInput;
  }
  return input;
}

export { conv, version };
