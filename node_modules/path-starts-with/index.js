'use strict';

var normalizePath = require('normalize-path');

module.exports = function startsWith(filepath, substr, options) {
  if (typeof filepath !== 'string') {
    throw new TypeError('expected filepath to be a string');
  }
  if (typeof substr !== 'string') {
    throw new TypeError('expected substring to be a string');
  }

  if (substr === '') {
    return false;
  }

  options = options || {};
  if (options.exact === true) {
    return filepath.indexOf(substr) === 0;
  }

  if (options.nocase === true) {
    substr = substr.toLowerCase();
    filepath = filepath.toLowerCase();
  }

  // return true if the given strings are an exact match
  if (filepath === substr) {
    return true;
  }

  if (substr.charAt(0) === '!') {
    return !startsWith(filepath, substr.slice(1), options);
  }

  var substrSlashes = leadingSlashes(substr);
  var filepathSlashes = leadingSlashes(filepath);

  // normalize slashes in substring and filepath
  var str = normalize(substr, false);
  var fp = normalize(filepath, false);

  // return if normalized strings are an exact match,
  // or if substring consists of only slashes
  if (substrSlashes === substr.length || fp === str) {
    return filepathSlashes === substrSlashes;
  }

  if (fp.indexOf(str) === 0) {
    if (options.partialMatch === true) {
      return true;
    }

    // handle "C:/foo" matching "C:/"
    if (str.slice(-1) === '/' && /^\w+:/.test(fp)) {
      return true;
    }

    var ch = fp.charAt(str.length);
    return ch === '' || ch === '/';
  }

  return false;
};

function leadingSlashes(str) {
  var i = 0;
  for (; i < str.length; i++) {
    var ch = str[i];
    if (ch !== '/' && ch !== '\\') {
      break;
    }
  }
  return i;
}

function normalize(str) {
  str = normalizePath(str, false);
  if (str.slice(0, 2) === './') {
    str = str.slice(2);
  }
  return str;
}
