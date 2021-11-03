'use strict';var _slicedToArray = function () {function sliceIterator(arr, i) {var _arr = [];var _n = true;var _d = false;var _e = undefined;try {for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) {_arr.push(_s.value);if (i && _arr.length === i) break;}} catch (err) {_d = true;_e = err;} finally {try {if (!_n && _i["return"]) _i["return"]();} finally {if (_d) throw _e;}}return _arr;}return function (arr, i) {if (Array.isArray(arr)) {return arr;} else if (Symbol.iterator in Object(arr)) {return sliceIterator(arr, i);} else {throw new TypeError("Invalid attempt to destructure non-iterable instance");}};}();var _path = require('path');var _path2 = _interopRequireDefault(_path);
var _fs = require('fs');var _fs2 = _interopRequireDefault(_fs);
var _readPkgUp = require('read-pkg-up');var _readPkgUp2 = _interopRequireDefault(_readPkgUp);
var _minimatch = require('minimatch');var _minimatch2 = _interopRequireDefault(_minimatch);
var _resolve = require('eslint-module-utils/resolve');var _resolve2 = _interopRequireDefault(_resolve);
var _moduleVisitor = require('eslint-module-utils/moduleVisitor');var _moduleVisitor2 = _interopRequireDefault(_moduleVisitor);
var _importType = require('../core/importType');var _importType2 = _interopRequireDefault(_importType);
var _packagePath = require('../core/packagePath');
var _docsUrl = require('../docsUrl');var _docsUrl2 = _interopRequireDefault(_docsUrl);function _interopRequireDefault(obj) {return obj && obj.__esModule ? obj : { default: obj };}

const depFieldCache = new Map();

function hasKeys() {let obj = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};
  return Object.keys(obj).length > 0;
}

function arrayOrKeys(arrayOrObject) {
  return Array.isArray(arrayOrObject) ? arrayOrObject : Object.keys(arrayOrObject);
}

function extractDepFields(pkg) {
  return {
    dependencies: pkg.dependencies || {},
    devDependencies: pkg.devDependencies || {},
    optionalDependencies: pkg.optionalDependencies || {},
    peerDependencies: pkg.peerDependencies || {},
    // BundledDeps should be in the form of an array, but object notation is also supported by
    // `npm`, so we convert it to an array if it is an object
    bundledDependencies: arrayOrKeys(pkg.bundleDependencies || pkg.bundledDependencies || []) };

}

function getDependencies(context, packageDir) {
  let paths = [];
  try {
    const packageContent = {
      dependencies: {},
      devDependencies: {},
      optionalDependencies: {},
      peerDependencies: {},
      bundledDependencies: [] };


    if (packageDir && packageDir.length > 0) {
      if (!Array.isArray(packageDir)) {
        paths = [_path2.default.resolve(packageDir)];
      } else {
        paths = packageDir.map(dir => _path2.default.resolve(dir));
      }
    }

    if (paths.length > 0) {
      // use rule config to find package.json
      paths.forEach(dir => {
        const packageJsonPath = _path2.default.join(dir, 'package.json');
        if (!depFieldCache.has(packageJsonPath)) {
          const depFields = extractDepFields(
          JSON.parse(_fs2.default.readFileSync(packageJsonPath, 'utf8')));

          depFieldCache.set(packageJsonPath, depFields);
        }
        const _packageContent = depFieldCache.get(packageJsonPath);
        Object.keys(packageContent).forEach(depsKey =>
        Object.assign(packageContent[depsKey], _packageContent[depsKey]));

      });
    } else {
      // use closest package.json
      Object.assign(
      packageContent,
      extractDepFields(
      _readPkgUp2.default.sync({ cwd: context.getFilename(), normalize: false }).pkg));


    }

    if (![
    packageContent.dependencies,
    packageContent.devDependencies,
    packageContent.optionalDependencies,
    packageContent.peerDependencies,
    packageContent.bundledDependencies].
    some(hasKeys)) {
      return null;
    }

    return packageContent;
  } catch (e) {
    if (paths.length > 0 && e.code === 'ENOENT') {
      context.report({
        message: 'The package.json file could not be found.',
        loc: { line: 0, column: 0 } });

    }
    if (e.name === 'JSONError' || e instanceof SyntaxError) {
      context.report({
        message: 'The package.json file could not be parsed: ' + e.message,
        loc: { line: 0, column: 0 } });

    }

    return null;
  }
}

function missingErrorMessage(packageName) {
  return `'${packageName}' should be listed in the project's dependencies. ` +
  `Run 'npm i -S ${packageName}' to add it`;
}

function devDepErrorMessage(packageName) {
  return `'${packageName}' should be listed in the project's dependencies, not devDependencies.`;
}

function optDepErrorMessage(packageName) {
  return `'${packageName}' should be listed in the project's dependencies, ` +
  `not optionalDependencies.`;
}

function getModuleOriginalName(name) {var _name$split =
  name.split('/'),_name$split2 = _slicedToArray(_name$split, 2);const first = _name$split2[0],second = _name$split2[1];
  return first.startsWith('@') ? `${first}/${second}` : first;
}

function getModuleRealName(resolved) {
  return (0, _packagePath.getFilePackageName)(resolved);
}

function reportIfMissing(context, deps, depsOptions, node, name) {
  // Do not report when importing types
  if (node.importKind === 'type' || node.parent && node.parent.importKind === 'type' || node.importKind === 'typeof') {
    return;
  }

  if ((0, _importType2.default)(name, context) !== 'external') {
    return;
  }

  const resolved = (0, _resolve2.default)(name, context);
  if (!resolved) {return;}

  // get the real name from the resolved package.json
  // if not aliased imports (alias/react for example) will not be correctly interpreted
  // fallback on original name in case no package.json found
  const packageName = getModuleRealName(resolved) || getModuleOriginalName(name);

  const isInDeps = deps.dependencies[packageName] !== undefined;
  const isInDevDeps = deps.devDependencies[packageName] !== undefined;
  const isInOptDeps = deps.optionalDependencies[packageName] !== undefined;
  const isInPeerDeps = deps.peerDependencies[packageName] !== undefined;
  const isInBundledDeps = deps.bundledDependencies.indexOf(packageName) !== -1;

  if (isInDeps ||
  depsOptions.allowDevDeps && isInDevDeps ||
  depsOptions.allowPeerDeps && isInPeerDeps ||
  depsOptions.allowOptDeps && isInOptDeps ||
  depsOptions.allowBundledDeps && isInBundledDeps)
  {
    return;
  }

  if (isInDevDeps && !depsOptions.allowDevDeps) {
    context.report(node, devDepErrorMessage(packageName));
    return;
  }

  if (isInOptDeps && !depsOptions.allowOptDeps) {
    context.report(node, optDepErrorMessage(packageName));
    return;
  }

  context.report(node, missingErrorMessage(packageName));
}

function testConfig(config, filename) {
  // Simplest configuration first, either a boolean or nothing.
  if (typeof config === 'boolean' || typeof config === 'undefined') {
    return config;
  }
  // Array of globs.
  return config.some(c =>
  (0, _minimatch2.default)(filename, c) ||
  (0, _minimatch2.default)(filename, _path2.default.join(process.cwd(), c)));

}

module.exports = {
  meta: {
    type: 'problem',
    docs: {
      url: (0, _docsUrl2.default)('no-extraneous-dependencies') },


    schema: [
    {
      'type': 'object',
      'properties': {
        'devDependencies': { 'type': ['boolean', 'array'] },
        'optionalDependencies': { 'type': ['boolean', 'array'] },
        'peerDependencies': { 'type': ['boolean', 'array'] },
        'bundledDependencies': { 'type': ['boolean', 'array'] },
        'packageDir': { 'type': ['string', 'array'] } },

      'additionalProperties': false }] },




  create: function (context) {
    const options = context.options[0] || {};
    const filename = context.getFilename();
    const deps = getDependencies(context, options.packageDir) || extractDepFields({});

    const depsOptions = {
      allowDevDeps: testConfig(options.devDependencies, filename) !== false,
      allowOptDeps: testConfig(options.optionalDependencies, filename) !== false,
      allowPeerDeps: testConfig(options.peerDependencies, filename) !== false,
      allowBundledDeps: testConfig(options.bundledDependencies, filename) !== false };


    return (0, _moduleVisitor2.default)((source, node) => {
      reportIfMissing(context, deps, depsOptions, node, source.value);
    }, { commonjs: true });
  } };
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uLy4uL3NyYy9ydWxlcy9uby1leHRyYW5lb3VzLWRlcGVuZGVuY2llcy5qcyJdLCJuYW1lcyI6WyJkZXBGaWVsZENhY2hlIiwiTWFwIiwiaGFzS2V5cyIsIm9iaiIsIk9iamVjdCIsImtleXMiLCJsZW5ndGgiLCJhcnJheU9yS2V5cyIsImFycmF5T3JPYmplY3QiLCJBcnJheSIsImlzQXJyYXkiLCJleHRyYWN0RGVwRmllbGRzIiwicGtnIiwiZGVwZW5kZW5jaWVzIiwiZGV2RGVwZW5kZW5jaWVzIiwib3B0aW9uYWxEZXBlbmRlbmNpZXMiLCJwZWVyRGVwZW5kZW5jaWVzIiwiYnVuZGxlZERlcGVuZGVuY2llcyIsImJ1bmRsZURlcGVuZGVuY2llcyIsImdldERlcGVuZGVuY2llcyIsImNvbnRleHQiLCJwYWNrYWdlRGlyIiwicGF0aHMiLCJwYWNrYWdlQ29udGVudCIsInBhdGgiLCJyZXNvbHZlIiwibWFwIiwiZGlyIiwiZm9yRWFjaCIsInBhY2thZ2VKc29uUGF0aCIsImpvaW4iLCJoYXMiLCJkZXBGaWVsZHMiLCJKU09OIiwicGFyc2UiLCJmcyIsInJlYWRGaWxlU3luYyIsInNldCIsIl9wYWNrYWdlQ29udGVudCIsImdldCIsImRlcHNLZXkiLCJhc3NpZ24iLCJyZWFkUGtnVXAiLCJzeW5jIiwiY3dkIiwiZ2V0RmlsZW5hbWUiLCJub3JtYWxpemUiLCJzb21lIiwiZSIsImNvZGUiLCJyZXBvcnQiLCJtZXNzYWdlIiwibG9jIiwibGluZSIsImNvbHVtbiIsIm5hbWUiLCJTeW50YXhFcnJvciIsIm1pc3NpbmdFcnJvck1lc3NhZ2UiLCJwYWNrYWdlTmFtZSIsImRldkRlcEVycm9yTWVzc2FnZSIsIm9wdERlcEVycm9yTWVzc2FnZSIsImdldE1vZHVsZU9yaWdpbmFsTmFtZSIsInNwbGl0IiwiZmlyc3QiLCJzZWNvbmQiLCJzdGFydHNXaXRoIiwiZ2V0TW9kdWxlUmVhbE5hbWUiLCJyZXNvbHZlZCIsInJlcG9ydElmTWlzc2luZyIsImRlcHMiLCJkZXBzT3B0aW9ucyIsIm5vZGUiLCJpbXBvcnRLaW5kIiwicGFyZW50IiwiaXNJbkRlcHMiLCJ1bmRlZmluZWQiLCJpc0luRGV2RGVwcyIsImlzSW5PcHREZXBzIiwiaXNJblBlZXJEZXBzIiwiaXNJbkJ1bmRsZWREZXBzIiwiaW5kZXhPZiIsImFsbG93RGV2RGVwcyIsImFsbG93UGVlckRlcHMiLCJhbGxvd09wdERlcHMiLCJhbGxvd0J1bmRsZWREZXBzIiwidGVzdENvbmZpZyIsImNvbmZpZyIsImZpbGVuYW1lIiwiYyIsInByb2Nlc3MiLCJtb2R1bGUiLCJleHBvcnRzIiwibWV0YSIsInR5cGUiLCJkb2NzIiwidXJsIiwic2NoZW1hIiwiY3JlYXRlIiwib3B0aW9ucyIsInNvdXJjZSIsInZhbHVlIiwiY29tbW9uanMiXSwibWFwcGluZ3MiOiJxb0JBQUEsNEI7QUFDQSx3QjtBQUNBLHdDO0FBQ0Esc0M7QUFDQSxzRDtBQUNBLGtFO0FBQ0EsZ0Q7QUFDQTtBQUNBLHFDOztBQUVBLE1BQU1BLGdCQUFnQixJQUFJQyxHQUFKLEVBQXRCOztBQUVBLFNBQVNDLE9BQVQsR0FBMkIsS0FBVkMsR0FBVSx1RUFBSixFQUFJO0FBQ3pCLFNBQU9DLE9BQU9DLElBQVAsQ0FBWUYsR0FBWixFQUFpQkcsTUFBakIsR0FBMEIsQ0FBakM7QUFDRDs7QUFFRCxTQUFTQyxXQUFULENBQXFCQyxhQUFyQixFQUFvQztBQUNsQyxTQUFPQyxNQUFNQyxPQUFOLENBQWNGLGFBQWQsSUFBK0JBLGFBQS9CLEdBQStDSixPQUFPQyxJQUFQLENBQVlHLGFBQVosQ0FBdEQ7QUFDRDs7QUFFRCxTQUFTRyxnQkFBVCxDQUEwQkMsR0FBMUIsRUFBK0I7QUFDN0IsU0FBTztBQUNMQyxrQkFBY0QsSUFBSUMsWUFBSixJQUFvQixFQUQ3QjtBQUVMQyxxQkFBaUJGLElBQUlFLGVBQUosSUFBdUIsRUFGbkM7QUFHTEMsMEJBQXNCSCxJQUFJRyxvQkFBSixJQUE0QixFQUg3QztBQUlMQyxzQkFBa0JKLElBQUlJLGdCQUFKLElBQXdCLEVBSnJDO0FBS0w7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QVdhLFFBQVFwRixlQUFuQixFQUFvQ3lFLFFBQXBDLE1BQWtELEtBRDlDO0FBRWxCSixvQkFBY0UsV0FBV2EsUUFBUW5GLG9CQUFuQixFQUF5Q3dFLFFBQXpDLE1BQXVELEtBRm5EO0FBR2xCTCxxQkFBZUcsV0FBV2EsUUFBUWxGLGdCQUFuQixFQUFxQ3VFLFFBQXJDLE1BQW1ELEtBSGhEO0FBSWxCSCx3QkFBa0JDLFdBQVdhLFFBQVFqRixtQkFBbkIsRUFBd0NzRSxRQUF4QyxNQUFzRCxLQUp0RCxFQUFwQjs7O0FBT0EsV0FBTyw2QkFBYyxDQUFDWSxNQUFELEVBQVM1QixJQUFULEtBQWtCO0FBQ3JDSCxzQkFBZ0JoRCxPQUFoQixFQUF5QmlELElBQXpCLEVBQStCQyxXQUEvQixFQUE0Q0MsSUFBNUMsRUFBa0Q0QixPQUFPQyxLQUF6RDtBQUNELEtBRk0sRUFFSixFQUFFQyxVQUFVLElBQVosRUFGSSxDQUFQO0FBR0QsR0FyQ2MsRUFBakIiLCJmaWxlIjoibm8tZXh0cmFuZW91cy1kZXBlbmRlbmNpZXMuanMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgcGF0aCBmcm9tICdwYXRoJztcbmltcG9ydCBmcyBmcm9tICdmcyc7XG5pbXBvcnQgcmVhZFBrZ1VwIGZyb20gJ3JlYWQtcGtnLXVwJztcbmltcG9ydCBtaW5pbWF0Y2ggZnJvbSAnbWluaW1hdGNoJztcbmltcG9ydCByZXNvbHZlIGZyb20gJ2VzbGludC1tb2R1bGUtdXRpbHMvcmVzb2x2ZSc7XG5pbXBvcnQgbW9kdWxlVmlzaXRvciBmcm9tICdlc2xpbnQtbW9kdWxlLXV0aWxzL21vZHVsZVZpc2l0b3InO1xuaW1wb3J0IGltcG9ydFR5cGUgZnJvbSAnLi4vY29yZS9pbXBvcnRUeXBlJztcbmltcG9ydCB7IGdldEZpbGVQYWNrYWdlTmFtZSB9IGZyb20gJy4uL2NvcmUvcGFja2FnZVBhdGgnO1xuaW1wb3J0IGRvY3NVcmwgZnJvbSAnLi4vZG9jc1VybCc7XG5cbmNvbnN0IGRlcEZpZWxkQ2FjaGUgPSBuZXcgTWFwKCk7XG5cbmZ1bmN0aW9uIGhhc0tleXMob2JqID0ge30pIHtcbiAgcmV0dXJuIE9iamVjdC5rZXlzKG9iaikubGVuZ3RoID4gMDtcbn1cblxuZnVuY3Rpb24gYXJyYXlPcktleXMoYXJyYXlPck9iamVjdCkge1xuICByZXR1cm4gQXJyYXkuaXNBcnJheShhcnJheU9yT2JqZWN0KSA/IGFycmF5T3JPYmplY3QgOiBPYmplY3Qua2V5cyhhcnJheU9yT2JqZWN0KTtcbn1cblxuZnVuY3Rpb24gZXh0cmFjdERlcEZpZWxkcyhwa2cpIHtcbiAgcmV0dXJuIHtcbiAgICBkZXBlbmRlbmNpZXM6IHBrZy5kZXBlbmRlbmNpZXMgfHwge30sXG4gICAgZGV2RGVwZW5kZW5jaWVzOiBwa2cuZGV2RGVwZW5kZW5jaWVzIHx8IHt9LFxuICAgIG9wdGlvbmFsRGVwZW5kZW5jaWVzOiBwa2cub3B0aW9uYWxEZXBlbmRlbmNpZXMgfHwge30sXG4gICAgcGVlckRlcGVuZGVuY2llczogcGtnLnBlZXJEZXBlbmRlbmNpZXMgfHwge30sXG4gICAgLy8gQnVuZGxlZERlcHMgc2hvdWxkIGJlIGluIHRoZSBmb3JtIG9mIGFuIGFycmF5LCBidXQgb2JqZWN0IG5vdGF0aW9uIGlzIGFsc28gc3VwcG9ydGVkIGJ5XG4gICAgLy8gYG5wbWAsIHNvIHdlIGNvbnZlcnQgaXQgdG8gYW4gYXJyYXkgaWYgaXQgaXMgYW4gb2JqZWN0XG4gICAgYnVuZGxlZERlcGVuZGVuY2llczogYXJyYXlPcktleXMocGtnLmJ1bmRsZURlcGVuZGVuY2llcyB8fCBwa2cuYnVuZGxlZERlcGVuZGVuY2llcyB8fCBbXSksXG4gIH07XG59XG5cbmZ1bmN0aW9uIGdldERlcGVuZGVuY2llcyhjb250ZXh0LCBwYWNrYWdlRGlyKSB7XG4gIGxldCBwYXRocyA9IFtdO1xuICB0cnkge1xuICAgIGNvbnN0IHBhY2thZ2VDb250ZW50ID0ge1xuICAgICAgZGVwZW5kZW5jaWVzOiB7fSxcbiAgICAgIGRldkRlcGVuZGVuY2llczoge30sXG4gICAgICBvcHRpb25hbERlcGVuZGVuY2llczoge30sXG4gICAgICBwZWVyRGVwZW5kZW5jaWVzOiB7fSxcbiAgICAgIGJ1bmRsZWREZXBlbmRlbmNpZXM6IFtdLFxuICAgIH07XG5cbiAgICBpZiAocGFja2FnZURpciAmJiBwYWNrYWdlRGlyLmxlbmd0aCA+IDApIHtcbiAgICAgIGlmICghQXJyYXkuaXNBcnJheShwYWNrYWdlRGlyKSkge1xuICAgICAgICBwYXRocyA9IFtwYXRoLnJlc29sdmUocGFja2FnZURpcildO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgcGF0aHMgPSBwYWNrYWdlRGlyLm1hcChkaXIgPT4gcGF0aC5yZXNvbHZlKGRpcikpO1xuICAgICAgfVxuICAgIH1cblxuICAgIGlmIChwYXRocy5sZW5ndGggPiAwKSB7XG4gICAgICAvLyB1c2UgcnVsZSBjb25maWcgdG8gZmluZCBwYWNrYWdlLmpzb25cbiAgICAgIHBhdGhzLmZvckVhY2goZGlyID0+IHtcbiAgICAgICAgY29uc3QgcGFja2FnZUpzb25QYXRoID0gcGF0aC5qb2luKGRpciwgJ3BhY2thZ2UuanNvbicpO1xuICAgICAgICBpZiAoIWRlcEZpZWxkQ2FjaGUuaGFzKHBhY2thZ2VKc29uUGF0aCkpIHtcbiAgICAgICAgICBjb25zdCBkZXBGaWVsZHMgPSBleHRyYWN0RGVwRmllbGRzKFxuICAgICAgICAgICAgSlNPTi5wYXJzZShmcy5yZWFkRmlsZVN5bmMocGFja2FnZUpzb25QYXRoLCAndXRmOCcpKVxuICAgICAgICAgICk7XG4gICAgICAgICAgZGVwRmllbGRDYWNoZS5zZXQocGFja2FnZUpzb25QYXRoLCBkZXBGaWVsZHMpO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IF9wYWNrYWdlQ29udGVudCA9IGRlcEZpZWxkQ2FjaGUuZ2V0KHBhY2thZ2VKc29uUGF0aCk7XG4gICAgICAgIE9iamVjdC5rZXlzKHBhY2thZ2VDb250ZW50KS5mb3JFYWNoKGRlcHNLZXkgPT5cbiAgICAgICAgICBPYmplY3QuYXNzaWduKHBhY2thZ2VDb250ZW50W2RlcHNLZXldLCBfcGFja2FnZUNvbnRlbnRbZGVwc0tleV0pXG4gICAgICAgICk7XG4gICAgICB9KTtcbiAgICB9IGVsc2Uge1xuICAgICAgLy8gdXNlIGNsb3Nlc3QgcGFja2FnZS5qc29uXG4gICAgICBPYmplY3QuYXNzaWduKFxuICAgICAgICBwYWNrYWdlQ29udGVudCxcbiAgICAgICAgZXh0cmFjdERlcEZpZWxkcyhcbiAgICAgICAgICByZWFkUGtnVXAuc3luYyh7IGN3ZDogY29udGV4dC5nZXRGaWxlbmFtZSgpLCBub3JtYWxpemU6IGZhbHNlIH0pLnBrZ1xuICAgICAgICApXG4gICAgICApO1xuICAgIH1cblxuICAgIGlmICghW1xuICAgICAgcGFja2FnZUNvbnRlbnQuZGVwZW5kZW5jaWVzLFxuICAgICAgcGFja2FnZUNvbnRlbnQuZGV2RGVwZW5kZW5jaWVzLFxuICAgICAgcGFja2FnZUNvbnRlbnQub3B0aW9uYWxEZXBlbmRlbmNpZXMsXG4gICAgICBwYWNrYWdlQ29udGVudC5wZWVyRGVwZW5kZW5jaWVzLFxuICAgICAgcGFja2FnZUNvbnRlbnQuYnVuZGxlZERlcGVuZGVuY2llcyxcbiAgICBdLnNvbWUoaGFzS2V5cykpIHtcbiAgICAgIHJldHVybiBudWxsO1xuICAgIH1cblxuICAgIHJldHVybiBwYWNrYWdlQ29udGVudDtcbiAgfSBjYXRjaCAoZSkge1xuICAgIGlmIChwYXRocy5sZW5ndGggPiAwICYmIGUuY29kZSA9PT0gJ0VOT0VOVCcpIHtcbiAgICAgIGNvbnRleHQucmVwb3J0KHtcbiAgICAgICAgbWVzc2FnZTogJ1RoZSBwYWNrYWdlLmpzb24gZmlsZSBjb3VsZCBub3QgYmUgZm91bmQuJyxcbiAgICAgICAgbG9jOiB7IGxpbmU6IDAsIGNvbHVtbjogMCB9LFxuICAgICAgfSk7XG4gICAgfVxuICAgIGlmIChlLm5hbWUgPT09ICdKU09ORXJyb3InIHx8IGUgaW5zdGFuY2VvZiBTeW50YXhFcnJvcikge1xuICAgICAgY29udGV4dC5yZXBvcnQoe1xuICAgICAgICBtZXNzYWdlOiAnVGhlIHBhY2thZ2UuanNvbiBmaWxlIGNvdWxkIG5vdCBiZSBwYXJzZWQ6ICcgKyBlLm1lc3NhZ2UsXG4gICAgICAgIGxvYzogeyBsaW5lOiAwLCBjb2x1bW46IDAgfSxcbiAgICAgIH0pO1xuICAgIH1cblxuICAgIHJldHVybiBudWxsO1xuICB9XG59XG5cbmZ1bmN0aW9uIG1pc3NpbmdFcnJvck1lc3NhZ2UocGFja2FnZU5hbWUpIHtcbiAgcmV0dXJuIGAnJHtwYWNrYWdlTmFtZX0nIHNob3VsZCBiZSBsaXN0ZWQgaW4gdGhlIHByb2plY3QncyBkZXBlbmRlbmNpZXMuIGAgK1xuICAgIGBSdW4gJ25wbSBpIC1TICR7cGFja2FnZU5hbWV9JyB0byBhZGQgaXRgO1xufVxuXG5mdW5jdGlvbiBkZXZEZXBFcnJvck1lc3NhZ2UocGFja2FnZU5hbWUpIHtcbiAgcmV0dXJuIGAnJHtwYWNrYWdlTmFtZX0nIHNob3VsZCBiZSBsaXN0ZWQgaW4gdGhlIHByb2plY3QncyBkZXBlbmRlbmNpZXMsIG5vdCBkZXZEZXBlbmRlbmNpZXMuYDtcbn1cblxuZnVuY3Rpb24gb3B0RGVwRXJyb3JNZXNzYWdlKHBhY2thZ2VOYW1lKSB7XG4gIHJldHVybiBgJyR7cGFja2FnZU5hbWV9JyBzaG91bGQgYmUgbGlzdGVkIGluIHRoZSBwcm9qZWN0J3MgZGVwZW5kZW5jaWVzLCBgICtcbiAgICBgbm90IG9wdGlvbmFsRGVwZW5kZW5jaWVzLmA7XG59XG5cbmZ1bmN0aW9uIGdldE1vZHVsZU9yaWdpbmFsTmFtZShuYW1lKSB7XG4gIGNvbnN0IFtmaXJzdCwgc2Vjb25kXSA9IG5hbWUuc3BsaXQoJy8nKTtcbiAgcmV0dXJuIGZpcnN0LnN0YXJ0c1dpdGgoJ0AnKSA/IGAke2ZpcnN0fS8ke3NlY29uZH1gIDogZmlyc3Q7XG59XG5cbmZ1bmN0aW9uIGdldE1vZHVsZVJlYWxOYW1lKHJlc29sdmVkKSB7XG4gIHJldHVybiBnZXRGaWxlUGFja2FnZU5hbWUocmVzb2x2ZWQpO1xufVxuXG5mdW5jdGlvbiByZXBvcnRJZk1pc3NpbmcoY29udGV4dCwgZGVwcywgZGVwc09wdGlvbnMsIG5vZGUsIG5hbWUpIHtcbiAgLy8gRG8gbm90IHJlcG9ydCB3aGVuIGltcG9ydGluZyB0eXBlc1xuICBpZiAobm9kZS5pbXBvcnRLaW5kID09PSAndHlwZScgfHwgKG5vZGUucGFyZW50ICYmIG5vZGUucGFyZW50LmltcG9ydEtpbmQgPT09ICd0eXBlJykgfHwgbm9kZS5pbXBvcnRLaW5kID09PSAndHlwZW9mJykge1xuICAgIHJldHVybjtcbiAgfVxuXG4gIGlmIChpbXBvcnRUeXBlKG5hbWUsIGNvbnRleHQpICE9PSAnZXh0ZXJuYWwnKSB7XG4gICAgcmV0dXJuO1xuICB9XG5cbiAgY29uc3QgcmVzb2x2ZWQgPSByZXNvbHZlKG5hbWUsIGNvbnRleHQpO1xuICBpZiAoIXJlc29sdmVkKSB7IHJldHVybjsgfVxuXG4gIC8vIGdldCB0aGUgcmVhbCBuYW1lIGZyb20gdGhlIHJlc29sdmVkIHBhY2thZ2UuanNvblxuICAvLyBpZiBub3QgYWxpYXNlZCBpbXBvcnRzIChhbGlhcy9yZWFjdCBmb3IgZXhhbXBsZSkgd2lsbCBub3QgYmUgY29ycmVjdGx5IGludGVycHJldGVkXG4gIC8vIGZhbGxiYWNrIG9uIG9yaWdpbmFsIG5hbWUgaW4gY2FzZSBubyBwYWNrYWdlLmpzb24gZm91bmRcbiAgY29uc3QgcGFja2FnZU5hbWUgPSBnZXRNb2R1bGVSZWFsTmFtZShyZXNvbHZlZCkgfHwgZ2V0TW9kdWxlT3JpZ2luYWxOYW1lKG5hbWUpO1xuXG4gIGNvbnN0IGlzSW5EZXBzID0gZGVwcy5kZXBlbmRlbmNpZXNbcGFja2FnZU5hbWVdICE9PSB1bmRlZmluZWQ7XG4gIGNvbnN0IGlzSW5EZXZEZXBzID0gZGVwcy5kZXZEZXBlbmRlbmNpZXNbcGFja2FnZU5hbWVdICE9PSB1bmRlZmluZWQ7XG4gIGNvbnN0IGlzSW5PcHREZXBzID0gZGVwcy5vcHRpb25hbERlcGVuZGVuY2llc1twYWNrYWdlTmFtZV0gIT09IHVuZGVmaW5lZDtcbiAgY29uc3QgaXNJblBlZXJEZXBzID0gZGVwcy5wZWVyRGVwZW5kZW5jaWVzW3BhY2thZ2VOYW1lXSAhPT0gdW5kZWZpbmVkO1xuICBjb25zdCBpc0luQnVuZGxlZERlcHMgPSBkZXBzLmJ1bmRsZWREZXBlbmRlbmNpZXMuaW5kZXhPZihwYWNrYWdlTmFtZSkgIT09IC0xO1xuXG4gIGlmIChpc0luRGVwcyB8fFxuICAgIChkZXBzT3B0aW9ucy5hbGxvd0RldkRlcHMgJiYgaXNJbkRldkRlcHMpIHx8XG4gICAgKGRlcHNPcHRpb25zLmFsbG93UGVlckRlcHMgJiYgaXNJblBlZXJEZXBzKSB8fFxuICAgIChkZXBzT3B0aW9ucy5hbGxvd09wdERlcHMgJiYgaXNJbk9wdERlcHMpIHx8XG4gICAgKGRlcHNPcHRpb25zLmFsbG93QnVuZGxlZERlcHMgJiYgaXNJbkJ1bmRsZWREZXBzKVxuICApIHtcbiAgICByZXR1cm47XG4gIH1cblxuICBpZiAoaXNJbkRldkRlcHMgJiYgIWRlcHNPcHRpb25zLmFsbG93RGV2RGVwcykge1xuICAgIGNvbnRleHQucmVwb3J0KG5vZGUsIGRldkRlcEVycm9yTWVzc2FnZShwYWNrYWdlTmFtZSkpO1xuICAgIHJldHVybjtcbiAgfVxuXG4gIGlmIChpc0luT3B0RGVwcyAmJiAhZGVwc09wdGlvbnMuYWxsb3dPcHREZXBzKSB7XG4gICAgY29udGV4dC5yZXBvcnQobm9kZSwgb3B0RGVwRXJyb3JNZXNzYWdlKHBhY2thZ2VOYW1lKSk7XG4gICAgcmV0dXJuO1xuICB9XG5cbiAgY29udGV4dC5yZXBvcnQobm9kZSwgbWlzc2luZ0Vycm9yTWVzc2FnZShwYWNrYWdlTmFtZSkpO1xufVxuXG5mdW5jdGlvbiB0ZXN0Q29uZmlnKGNvbmZpZywgZmlsZW5hbWUpIHtcbiAgLy8gU2ltcGxlc3QgY29uZmlndXJhdGlvbiBmaXJzdCwgZWl0aGVyIGEgYm9vbGVhbiBvciBub3RoaW5nLlxuICBpZiAodHlwZW9mIGNvbmZpZyA9PT0gJ2Jvb2xlYW4nIHx8IHR5cGVvZiBjb25maWcgPT09ICd1bmRlZmluZWQnKSB7XG4gICAgcmV0dXJuIGNvbmZpZztcbiAgfVxuICAvLyBBcnJheSBvZiBnbG9icy5cbiAgcmV0dXJuIGNvbmZpZy5zb21lKGMgPT4gKFxuICAgIG1pbmltYXRjaChmaWxlbmFtZSwgYykgfHxcbiAgICBtaW5pbWF0Y2goZmlsZW5hbWUsIHBhdGguam9pbihwcm9jZXNzLmN3ZCgpLCBjKSlcbiAgKSk7XG59XG5cbm1vZHVsZS5leHBvcnRzID0ge1xuICBtZXRhOiB7XG4gICAgdHlwZTogJ3Byb2JsZW0nLFxuICAgIGRvY3M6IHtcbiAgICAgIHVybDogZG9jc1VybCgnbm8tZXh0cmFuZW91cy1kZXBlbmRlbmNpZXMnKSxcbiAgICB9LFxuXG4gICAgc2NoZW1hOiBbXG4gICAgICB7XG4gICAgICAgICd0eXBlJzogJ29iamVjdCcsXG4gICAgICAgICdwcm9wZXJ0aWVzJzoge1xuICAgICAgICAgICdkZXZEZXBlbmRlbmNpZXMnOiB7ICd0eXBlJzogWydib29sZWFuJywgJ2FycmF5J10gfSxcbiAgICAgICAgICAnb3B0aW9uYWxEZXBlbmRlbmNpZXMnOiB7ICd0eXBlJzogWydib29sZWFuJywgJ2FycmF5J10gfSxcbiAgICAgICAgICAncGVlckRlcGVuZGVuY2llcyc6IHsgJ3R5cGUnOiBbJ2Jvb2xlYW4nLCAnYXJyYXknXSB9LFxuICAgICAgICAgICdidW5kbGVkRGVwZW5kZW5jaWVzJzogeyAndHlwZSc6IFsnYm9vbGVhbicsICdhcnJheSddIH0sXG4gICAgICAgICAgJ3BhY2thZ2VEaXInOiB7ICd0eXBlJzogWydzdHJpbmcnLCAnYXJyYXknXSB9LFxuICAgICAgICB9LFxuICAgICAgICAnYWRkaXRpb25hbFByb3BlcnRpZXMnOiBmYWxzZSxcbiAgICAgIH0sXG4gICAgXSxcbiAgfSxcblxuICBjcmVhdGU6IGZ1bmN0aW9uIChjb250ZXh0KSB7XG4gICAgY29uc3Qgb3B0aW9ucyA9IGNvbnRleHQub3B0aW9uc1swXSB8fCB7fTtcbiAgICBjb25zdCBmaWxlbmFtZSA9IGNvbnRleHQuZ2V0RmlsZW5hbWUoKTtcbiAgICBjb25zdCBkZXBzID0gZ2V0RGVwZW5kZW5jaWVzKGNvbnRleHQsIG9wdGlvbnMucGFja2FnZURpcikgfHwgZXh0cmFjdERlcEZpZWxkcyh7fSk7XG5cbiAgICBjb25zdCBkZXBzT3B0aW9ucyA9IHtcbiAgICAgIGFsbG93RGV2RGVwczogdGVzdENvbmZpZyhvcHRpb25zLmRldkRlcGVuZGVuY2llcywgZmlsZW5hbWUpICE9PSBmYWxzZSxcbiAgICAgIGFsbG93T3B0RGVwczogdGVzdENvbmZpZyhvcHRpb25zLm9wdGlvbmFsRGVwZW5kZW5jaWVzLCBmaWxlbmFtZSkgIT09IGZhbHNlLFxuICAgICAgYWxsb3dQZWVyRGVwczogdGVzdENvbmZpZyhvcHRpb25zLnBlZXJEZXBlbmRlbmNpZXMsIGZpbGVuYW1lKSAhPT0gZmFsc2UsXG4gICAgICBhbGxvd0J1bmRsZWREZXBzOiB0ZXN0Q29uZmlnKG9wdGlvbnMuYnVuZGxlZERlcGVuZGVuY2llcywgZmlsZW5hbWUpICE9PSBmYWxzZSxcbiAgICB9O1xuXG4gICAgcmV0dXJuIG1vZHVsZVZpc2l0b3IoKHNvdXJjZSwgbm9kZSkgPT4ge1xuICAgICAgcmVwb3J0SWZNaXNzaW5nKGNvbnRleHQsIGRlcHMsIGRlcHNPcHRpb25zLCBub2RlLCBzb3VyY2UudmFsdWUpO1xuICAgIH0sIHsgY29tbW9uanM6IHRydWUgfSk7XG4gIH0sXG59O1xuIl19