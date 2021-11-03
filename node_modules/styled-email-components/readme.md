# 💌 styled-email-components

[![npm Version](https://img.shields.io/npm/v/styled-email-components.svg)](https://www.npmjs.com/package/styled-email-components)
[![Build Status](https://img.shields.io/travis/sbekrin/styled-email-components.svg)](https://travis-ci.org/sbekrin/styled-email-components)
[![dependencies Status](https://img.shields.io/david/sbekrin/styled-email-components.svg)](https://david-dm.org/sbekrin/styled-email-components)
[![devDependencies Status](https://img.shields.io/david/dev/sbekrin/styled-email-components.svg)](https://david-dm.org/sbekrin/styled-email-components?type=dev)

Extension of [`styled-components (v5.x)`](https://www.styled-components.com/) with
essential features for building email components.

## Features

- Styles are injected inline
- [Shorthand rules](./src/css-to-style.js#L6) are expanded
- [`styled.*` aliases](./src/utils/xhtml-elements.js) are XHTML compliant
- Supports [Outlook-specific elements](#outlook-specific-vml-elements)
- Compatible with [original APIs](https://www.styled-components.com/docs/api)
- Provides TypeScript typings

## Motivation

`styled-components` is a universal styling solution with great developer
experience and low learning curve. Unfortunately, there's no native support for
inline styling which is essential for building emails. This module adds all
necessary features to build mail-first components.

## Installation

yarn:

```sh
yarn add styled-email-components
```

npm:

```sh
npm install --save styled-email-components
```

## Getting Started

Check original
[Getting Started](https://www.styled-components.com/docs/basics#getting-started)
for more examples.

```js
import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import styled from 'styled-email-components';

const Link = styled.a`
  font-family: sans-serif;
  background: blue;
  color: white;
`;

renderToStaticMarkup(<Link href="https://example.com">Hey</Link>),
// 👇 output
// <a href="https://example.com" style="font-family:sans-serif;background-color:blue;color:white;">Hey</a>
```

## API

### `styled.*`

This module sets list of XHTML 1.0 Transitional
[element aliases](./src/utils/xhtml-elements.js) instead of the original HTML5 set,
which is a widely used doctype in emails.

### Outlook-specific VML elements

In addition to XHTML elements, `styled.vml.*`, `styled.wml.*` and
`styled.office.*` aliases are available. These are simple proxies and pass tag
names as-is with `v:`, `w:` and `o:` prefixes respectively.

### Other APIs

[Original APIs](https://www.styled-components.com/docs/api) are mirrored without
any modifications from `styled-components`. Make sure to check
[server-side rendering](https://www.styled-components.com/docs/advanced#server-side-rendering)
guide for rendering the final email.

## License

MIT &copy; [Sergey Bekrin](http://bekrin.me/)