'use strict';

var startsWith = require('path-starts-with');
var normalizePath = require('normalize-path');

function containsPath(filepath, substr, options) {
  if (typeof filepath !== 'string') {
    throw new TypeError('expected filepath to be a string');
  }
  if (typeof substr !== 'string') {
    throw new TypeError('expected substring to be a string');
  }

  if (substr === '') {
    return false;
  }

  // return true if the given strings are an exact match
  if (filepath === substr) {
    return true;
  }

  if (substr.charAt(0) === '!') {
    return !containsPath(filepath, substr.slice(1), options);
  }

  options = options || {};
  if (options.nocase === true) {
    filepath = filepath.toLowerCase();
    substr = substr.toLowerCase();
  }

  var fp = normalize(filepath, false);
  var str = normalize(substr, false);

  // return false if the normalized substring is only a slash
  if (str === '/') {
    return false;
  }

  // if normalized strings are equal, return true
  if (fp === str) {
    return true;
  }

  if (startsWith(filepath, substr, options)) {
    return true;
  }

  var idx = fp.indexOf(str);
  var prefix = substr.slice(0, 2);

  // if the original substring started with "./", we'll
  // assume it should match from the beginning of the string
  if (prefix === './' || prefix === '.\\') {
    return idx === 0;
  }

  if (idx !== -1) {
    if (options.partialMatch === true) {
      return true;
    }

    // if the first character in the substring is a
    // dot or slash, we can consider this a match
    var ch = str.charAt(0);
    if (ch === '/') {
      return true;
    }

    // since partial matches were not enabled, we only consider
    // this a match if the next character is a dot or a slash
    var before = fp.charAt(idx - 1);
    var after = fp.charAt(idx + str.length);
    return (before === '' || before === '/')
      && (after === '' || after === '/');
  }

  return false;
}

/**
 * Normalize paths
 */

function normalize(str) {
  str = normalizePath(str, false);
  if (str.slice(0, 2) === './') {
    str = str.slice(2);
  }
  return str;
}

/**
 * Expose `containsPath`
 */

module.exports = containsPath;
