import babel from 'rollup-plugin-babel';
import uglify from 'rollup-plugin-uglify';
import license from 'rollup-plugin-license';
import { minify } from 'uglify-es';

import pkjson from './package.json';

const prjName = pkjson.name;
const moduleName = pkjson.moduleName;

const banner = `/*!
* ${prjName} v${pkjson.version}
*
* Copyright 2018-${new Date().getFullYear()}, ${pkjson.authors[0]}
* Licensed under the MIT license
* http://www.opensource.org/licenses/mit-license
*
*/`;

const isDev = process.argv.splice(2).indexOf('--min') < 0;
const plugins = isDev ?
    [
        babel({
            exclude: 'node_modules/**',
        })
    ] : [
        babel({
            exclude: 'node_modules/**',
        }),
        uglify({}, minify),
        license({ banner })
    ];

const output = isDev ? { file: `build/${prjName}.js` } : { file: `build/${prjName}.min.js` };

export default {
    input: 'src/RAFManager.js',
    output: {
        ...output,
        format: 'umd',
        name: moduleName,
        sourcemap: true,
    },
    plugins: plugins
};