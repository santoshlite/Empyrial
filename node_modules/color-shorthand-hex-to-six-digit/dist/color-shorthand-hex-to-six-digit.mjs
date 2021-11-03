/**
 * color-shorthand-hex-to-six-digit
 * Convert shorthand hex color codes into full
 * Version: 3.0.7
 * Author: Roy Revelt, Codsen Ltd
 * License: MIT
 * Homepage: https://codsen.com/os/color-shorthand-hex-to-six-digit/
 */

import r from"hex-color-regex";import e from"lodash.isplainobject";import t from"lodash.clonedeep";const o="3.0.7";function a(o){let c=t(o);if("string"==typeof o)c=c.replace(r(),(function(r,e,t,o){return"&"!==o[t-1]&&4===r.length&&"#"===r.charAt(0)?`#${r.charAt(1)}${r.charAt(1)}${r.charAt(2)}${r.charAt(2)}${r.charAt(3)}${r.charAt(3)}`.toLowerCase():r.toLowerCase()}));else if(Array.isArray(c))for(let r=0,e=c.length;r<e;r++)c[r]=a(c[r]);else{if(!e(o))return o;Object.keys(c).forEach((r=>{c[r]=a(c[r])}))}return c}export{a as conv,o as version};
