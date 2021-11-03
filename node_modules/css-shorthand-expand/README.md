# css-shorthand-expand

[![Build Status](https://travis-ci.org/kapetan/css-shorthand-expand.svg?branch=master)](https://travis-ci.org/kapetan/css-shorthand-expand)

Expand CSS shorthand properties to their longhand equivalent.

	npm install css-shorthand-expand

# Usage

The module exposes a single function which takes a property name and a value and returns a map with the expanded properties.

```javascript
var expand = require('css-shorthand-expand');

expand('background', 'url(image.png) no-repeat #ff0');
```

The above returns an object.

```javascript
{
	'background-image': 'url(image.png)',
	'background-repeat': 'no-repeat',
	'background-color': '#ff0'
}
```

Currently the following properties are supported.

- background
- font
- padding
- margin
- border
- border-width
- border-style
- border-color
- border-top
- border-right
- border-bottom
- border-left
- border-radius
- outline
