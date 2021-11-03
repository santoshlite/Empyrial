'use strict';var _slicedToArray = function () {function sliceIterator(arr, i) {var _arr = [];var _n = true;var _d = false;var _e = undefined;try {for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) {_arr.push(_s.value);if (i && _arr.length === i) break;}} catch (err) {_d = true;_e = err;} finally {try {if (!_n && _i["return"]) _i["return"]();} finally {if (_d) throw _e;}}return _arr;}return function (arr, i) {if (Array.isArray(arr)) {return arr;} else if (Symbol.iterator in Object(arr)) {return sliceIterator(arr, i);} else {throw new TypeError("Invalid attempt to destructure non-iterable instance");}};}(); /**
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       * @fileOverview Ensures that no imported module imports the linted module.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       * @author Ben Mosher
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       */

var _resolve = require('eslint-module-utils/resolve');var _resolve2 = _interopRequireDefault(_resolve);
var _ExportMap = require('../ExportMap');var _ExportMap2 = _interopRequireDefault(_ExportMap);
var _importType = require('../core/importType');
var _moduleVisitor = require('eslint-module-utils/moduleVisitor');var _moduleVisitor2 = _interopRequireDefault(_moduleVisitor);
var _docsUrl = require('../docsUrl');var _docsUrl2 = _interopRequireDefault(_docsUrl);function _interopRequireDefault(obj) {return obj && obj.__esModule ? obj : { default: obj };}

// todo: cache cycles / deep relationships for faster repeat evaluation
module.exports = {
  meta: {
    type: 'suggestion',
    docs: { url: (0, _docsUrl2.default)('no-cycle') },
    schema: [(0, _moduleVisitor.makeOptionsSchema)({
      maxDepth: {
        oneOf: [
        {
          description: 'maximum dependency depth to traverse',
          type: 'integer',
          minimum: 1 },

        {
          enum: ['∞'],
          type: 'string' }] },



      ignoreExternal: {
        description: 'ignore external modules',
        type: 'boolean',
        default: false } })] },




  create: function (context) {
    const myPath = context.getFilename();
    if (myPath === '<text>') return {}; // can't cycle-check a non-file

    const options = context.options[0] || {};
    const maxDepth = typeof options.maxDepth === 'number' ? options.maxDepth : Infinity;
    const ignoreModule = name => options.ignoreExternal && (0, _importType.isExternalModule)(
    name,
    context.settings,
    (0, _resolve2.default)(name, context),
    context);


    function checkSourceValue(sourceNode, importer) {
      if (ignoreModule(sourceNode.value)) {
        return; // ignore external modules
      }

      if (
      importer.type === 'ImportDeclaration' && (
      // import type { Foo } (TS and Flow)
      importer.importKind === 'type' ||
      // import { type Foo } (Flow)
      importer.specifiers.every((_ref) => {let importKind = _ref.importKind;return importKind === 'type';})))

      {
        return; // ignore type imports
      }

      const imported = _ExportMap2.default.get(sourceNode.value, context);

      if (imported == null) {
        return; // no-unresolved territory
      }

      if (imported.path === myPath) {
        return; // no-self-import territory
      }

      const untraversed = [{ mget: () => imported, route: [] }];
      const traversed = new Set();
      function detectCycle(_ref2) {let mget = _ref2.mget,route = _ref2.route;
        const m = mget();
        if (m == null) return;
        if (traversed.has(m.path)) return;
        traversed.add(m.path);

        for (const _ref3 of m.imports) {var _ref4 = _slicedToArray(_ref3, 2);const path = _ref4[0];var _ref4$ = _ref4[1];const getter = _ref4$.getter;const declarations = _ref4$.declarations;
          if (path === myPath) return true;
          if (traversed.has(path)) continue;
          for (const _ref5 of declarations) {const source = _ref5.source;const isOnlyImportingTypes = _ref5.isOnlyImportingTypes;
            if (ignoreModule(source.value)) continue;
            // Ignore only type imports
            if (isOnlyImportingTypes) continue;

            if (route.length + 1 < maxDepth) {
              untraversed.push({
                mget: getter,
                route: route.concat(source) });

            }
          }
        }
      }

      while (untraversed.length > 0) {
        const next = untraversed.shift(); // bfs!
        if (detectCycle(next)) {
          const message = next.route.length > 0 ?
          `Dependency cycle via ${routeString(next.route)}` :
          'Dependency cycle detected.';
          context.report(importer, message);
          return;
        }
      }
    }

    return (0, _moduleVisitor2.default)(checkSourceValue, context.options[0]);
  } };


function routeString(route) {
  return route.map(s => `${s.value}:${s.loc.start.line}`).join('=>');
}
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uLy4uL3NyYy9ydWxlcy9uby1jeWNsZS5qcyJdLCJuYW1lcyI6WyJtb2R1bGUiLCJleHBvcnRzIiwibWV0YSIsInR5cGUiLCJkb2NzIiwidXJsIiwic2NoZW1hIiwibWF4RGVwdGgiLCJvbmVPZiIsImRlc2NyaXB0aW9uIiwibWluaW11bSIsImVudW0iLCJpZ25vcmVFeHRlcm5hbCIsImRlZmF1bHQiLCJjcmVhdGUiLCJjb250ZXh0IiwibXlQYXRoIiwiZ2V0RmlsZW5hbWUiLCJvcHRpb25zIiwiSW5maW5pdHkiLCJpZ25vcmVNb2R1bGUiLCJuYW1lIiwic2V0dGluZ3MiLCJjaGVja1NvdXJjZVZhbHVlIiwic291cmNlTm9kZSIsImltcG9ydGVyIiwidmFsdWUiLCJpbXBvcnRLaW5kIiwic3BlY2lmaWVycyIsImV2ZXJ5IiwiaW1wb3J0ZWQiLCJFeHBvcnRzIiwiZ2V0IiwicGF0aCIsInVudHJhdmVyc2VkIiwibWdldCIsInJvdXRlIiwidHJhdmVyc2VkIiwiU2V0IiwiZGV0ZWN0Q3ljbGUiLCJtIiwiaGFzIiwiYWRkIiwiaW1wb3J0cyIsImdldHRlciIsImRlY2xhcmF0aW9ucyIsInNvdXJjZSIsImlzT25seUltcG9ydGluZ1R5cGVzIiwibGVuZ3RoIiwicHVzaCIsImNvbmNhdCIsIm5leHQiLCJzaGlmdCIsIm1lc3NhZ2UiLCJyb3V0ZVN0cmluZyIsInJlcG9ydCIsIm1hcCIsInMiLCJsb2MiLCJzdGFydCIsImxpbmUiLCJqb2luIl0sIm1hcHBpbmdzIjoic29CQUFBOzs7OztBQUtBLHNEO0FBQ0EseUM7QUFDQTtBQUNBLGtFO0FBQ0EscUM7O0FBRUE7QUFDQUEsT0FBT0MsT0FBUCxHQUFpQjtBQUNmQyxRQUFNO0FBQ0pDLFVBQU0sWUFERjtBQUVKQyxVQUFNLEVBQUVDLEtBQUssdUJBQVEsVUFBUixDQUFQLEVBRkY7QUFHSkMsWUFBUSxDQUFDLHNDQUFrQjtBQUN6QkMsZ0JBQVU7QUFDUkMsZUFBTztBQUNMO0FBQ0VDLHVCQUFhLHNDQURmO0FBRUVOLGdCQUFNLFNBRlI7QUFHRU8sbUJBQVMsQ0FIWCxFQURLOztBQU1MO0FBQ0VDLGdCQUFNLENBQUMsR0FBRCxDQURSO0FBRUVSLGdCQUFNLFFBRlIsRUFOSyxDQURDLEVBRGU7Ozs7QUFjekJTLHNCQUFnQjtBQUNkSCxxQkFBYSx5QkFEQztBQUVkTixjQUFNLFNBRlE7QUFHZFUsaUJBQVMsS0FISyxFQWRTLEVBQWxCLENBQUQsQ0FISixFQURTOzs7OztBQTBCZkMsVUFBUSxVQUFVQyxPQUFWLEVBQW1CO0FBQ3pCLFVBQU1DLFNBQVNELFFBQVFFLFdBQVIsRUFBZjtBQUNBLFFBQUlELFdBQVcsUUFBZixFQUF5QixPQUFPLEVBQVAsQ0FGQSxDQUVXOztBQUVwQyxVQUFNRSxVQUFVSCxRQUFRRyxPQUFSLENBQWdCLENBQWhCLEtBQXNCLEVBQXRDO0FBQ0EsVUFBTVgsV0FBVyxPQUFPVyxRQUFRWCxRQUFmLEtBQTRCLFFBQTVCLEdBQXVDVyxRQUFRWCxRQUEvQyxHQUEwRFksUUFBM0U7QUFDQSxVQUFNQyxlQUFnQkMsSUFBRCxJQUFVSCxRQUFRTixjQUFSLElBQTBCO0FBQ3ZEUyxRQUR1RDtBQUV2RE4sWUFBUU8sUUFGK0M7QUFHdkQsMkJBQVFELElBQVIsRUFBY04sT0FBZCxDQUh1RDtBQUl2REEsV0FKdUQsQ0FBekQ7OztBQU9BLGFBQVNRLGdCQUFULENBQTBCQyxVQUExQixFQUFzQ0MsUUFBdEMsRUFBZ0Q7QUFDOUMsVUFBSUwsYUFBYUksV0FBV0UsS0FBeEIsQ0FBSixFQUFvQztBQUNsQyxlQURrQyxDQUMxQjtBQUNUOztBQUVEO0FBQ0VELGVBQVN0QixJQUFULEtBQWtCLG1CQUFsQjtBQUNFO0FBQ0FzQixlQUFTRSxVQUFULEtBQXdCLE1BQXhCO0FBQ0E7QUFDQUYsZUFBU0csVUFBVCxDQUFvQkMsS0FBcEIsQ0FBMEIsZUFBR0YsVUFBSCxRQUFHQSxVQUFILFFBQW9CQSxlQUFlLE1BQW5DLEVBQTFCLENBSkYsQ0FERjs7QUFPRTtBQUNBLGVBREEsQ0FDUTtBQUNUOztBQUVELFlBQU1HLFdBQVdDLG9CQUFRQyxHQUFSLENBQVlSLFdBQVdFLEtBQXZCLEVBQThCWCxPQUE5QixDQUFqQjs7QUFFQSxVQUFJZSxZQUFZLElBQWhCLEVBQXNCO0FBQ3BCLGVBRG9CLENBQ1g7QUFDVjs7QUFFRCxVQUFJQSxTQUFTRyxJQUFULEtBQWtCakIsTUFBdEIsRUFBOEI7QUFDNUIsZUFENEIsQ0FDbkI7QUFDVjs7QUFFRCxZQUFNa0IsY0FBYyxDQUFDLEVBQUVDLE1BQU0sTUFBTUwsUUFBZCxFQUF3Qk0sT0FBTSxFQUE5QixFQUFELENBQXBCO0FBQ0EsWUFBTUMsWUFBWSxJQUFJQyxHQUFKLEVBQWxCO0FBQ0EsZUFBU0MsV0FBVCxRQUFzQyxLQUFmSixJQUFlLFNBQWZBLElBQWUsQ0FBVEMsS0FBUyxTQUFUQSxLQUFTO0FBQ3BDLGNBQU1JLElBQUlMLE1BQVY7QUFDQSxZQUFJSyxLQUFLLElBQVQsRUFBZTtBQUNmLFlBQUlILFVBQVVJLEdBQVYsQ0FBY0QsRUFBRVAsSUFBaEIsQ0FBSixFQUEyQjtBQUMzQkksa0JBQVVLLEdBQVYsQ0FBY0YsRUFBRVAsSUFBaEI7O0FBRUEsNEJBQStDTyxFQUFFRyxPQUFqRCxFQUEwRCw0Q0FBOUNWLElBQThDLHdDQUF0Q1csTUFBc0MsVUFBdENBLE1BQXNDLE9BQTlCQyxZQUE4QixVQUE5QkEsWUFBOEI7QUFDeEQsY0FBSVosU0FBU2pCLE1BQWIsRUFBcUIsT0FBTyxJQUFQO0FBQ3JCLGNBQUlxQixVQUFVSSxHQUFWLENBQWNSLElBQWQsQ0FBSixFQUF5QjtBQUN6Qiw4QkFBK0NZLFlBQS9DLEVBQTZELE9BQWhEQyxNQUFnRCxTQUFoREEsTUFBZ0QsT0FBeENDLG9CQUF3QyxTQUF4Q0Esb0JBQXdDO0FBQzNELGdCQUFJM0IsYUFBYTBCLE9BQU9wQixLQUFwQixDQUFKLEVBQWdDO0FBQ2hDO0FBQ0EsZ0JBQUlxQixvQkFBSixFQUEwQjs7QUFFMUIsZ0JBQUlYLE1BQU1ZLE1BQU4sR0FBZSxDQUFmLEdBQW1CekMsUUFBdkIsRUFBaUM7QUFDL0IyQiwwQkFBWWUsSUFBWixDQUFpQjtBQUNmZCxzQkFBTVMsTUFEUztBQUVmUix1QkFBT0EsTUFBTWMsTUFBTixDQUFhSixNQUFiLENBRlEsRUFBakI7O0FBSUQ7QUFDRjtBQUNGO0FBQ0Y7O0FBRUQsYUFBT1osWUFBWWMsTUFBWixHQUFxQixDQUE1QixFQUErQjtBQUM3QixjQUFNRyxPQUFPakIsWUFBWWtCLEtBQVosRUFBYixDQUQ2QixDQUNLO0FBQ2xDLFlBQUliLFlBQVlZLElBQVosQ0FBSixFQUF1QjtBQUNyQixnQkFBTUUsVUFBV0YsS0FBS2YsS0FBTCxDQUFXWSxNQUFYLEdBQW9CLENBQXBCO0FBQ1osa0NBQXVCTSxZQUFZSCxLQUFLZixLQUFqQixDQUF3QixFQURuQztBQUViLHNDQUZKO0FBR0FyQixrQkFBUXdDLE1BQVIsQ0FBZTlCLFFBQWYsRUFBeUI0QixPQUF6QjtBQUNBO0FBQ0Q7QUFDRjtBQUNGOztBQUVELFdBQU8sNkJBQWM5QixnQkFBZCxFQUFnQ1IsUUFBUUcsT0FBUixDQUFnQixDQUFoQixDQUFoQyxDQUFQO0FBQ0QsR0F4R2MsRUFBakI7OztBQTJHQSxTQUFTb0MsV0FBVCxDQUFxQmxCLEtBQXJCLEVBQTRCO0FBQzFCLFNBQU9BLE1BQU1vQixHQUFOLENBQVVDLEtBQU0sR0FBRUEsRUFBRS9CLEtBQU0sSUFBRytCLEVBQUVDLEdBQUYsQ0FBTUMsS0FBTixDQUFZQyxJQUFLLEVBQTlDLEVBQWlEQyxJQUFqRCxDQUFzRCxJQUF0RCxDQUFQO0FBQ0QiLCJmaWxlIjoibm8tY3ljbGUuanMiLCJzb3VyY2VzQ29udGVudCI6WyIvKipcbiAqIEBmaWxlT3ZlcnZpZXcgRW5zdXJlcyB0aGF0IG5vIGltcG9ydGVkIG1vZHVsZSBpbXBvcnRzIHRoZSBsaW50ZWQgbW9kdWxlLlxuICogQGF1dGhvciBCZW4gTW9zaGVyXG4gKi9cblxuaW1wb3J0IHJlc29sdmUgZnJvbSAnZXNsaW50LW1vZHVsZS11dGlscy9yZXNvbHZlJztcbmltcG9ydCBFeHBvcnRzIGZyb20gJy4uL0V4cG9ydE1hcCc7XG5pbXBvcnQgeyBpc0V4dGVybmFsTW9kdWxlIH0gZnJvbSAnLi4vY29yZS9pbXBvcnRUeXBlJztcbmltcG9ydCBtb2R1bGVWaXNpdG9yLCB7IG1ha2VPcHRpb25zU2NoZW1hIH0gZnJvbSAnZXNsaW50LW1vZHVsZS11dGlscy9tb2R1bGVWaXNpdG9yJztcbmltcG9ydCBkb2NzVXJsIGZyb20gJy4uL2RvY3NVcmwnO1xuXG4vLyB0b2RvOiBjYWNoZSBjeWNsZXMgLyBkZWVwIHJlbGF0aW9uc2hpcHMgZm9yIGZhc3RlciByZXBlYXQgZXZhbHVhdGlvblxubW9kdWxlLmV4cG9ydHMgPSB7XG4gIG1ldGE6IHtcbiAgICB0eXBlOiAnc3VnZ2VzdGlvbicsXG4gICAgZG9jczogeyB1cmw6IGRvY3NVcmwoJ25vLWN5Y2xlJykgfSxcbiAgICBzY2hlbWE6IFttYWtlT3B0aW9uc1NjaGVtYSh7XG4gICAgICBtYXhEZXB0aDoge1xuICAgICAgICBvbmVPZjogW1xuICAgICAgICAgIHtcbiAgICAgICAgICAgIGRlc2NyaXB0aW9uOiAnbWF4aW11bSBkZXBlbmRlbmN5IGRlcHRoIHRvIHRyYXZlcnNlJyxcbiAgICAgICAgICAgIHR5cGU6ICdpbnRlZ2VyJyxcbiAgICAgICAgICAgIG1pbmltdW06IDEsXG4gICAgICAgICAgfSxcbiAgICAgICAgICB7XG4gICAgICAgICAgICBlbnVtOiBbJ+KIniddLFxuICAgICAgICAgICAgdHlwZTogJ3N0cmluZycsXG4gICAgICAgICAgfSxcbiAgICAgICAgXSxcbiAgICAgIH0sXG4gICAgICBpZ25vcmVFeHRlcm5hbDoge1xuICAgICAgICBkZXNjcmlwdGlvbjogJ2lnbm9yZSBleHRlcm5hbCBtb2R1bGVzJyxcbiAgICAgICAgdHlwZTogJ2Jvb2xlYW4nLFxuICAgICAgICBkZWZhdWx0OiBmYWxzZSxcbiAgICAgIH0sXG4gICAgfSldLFxuICB9LFxuXG4gIGNyZWF0ZTogZnVuY3Rpb24gKGNvbnRleHQpIHtcbiAgICBjb25zdCBteVBhdGggPSBjb250ZXh0LmdldEZpbGVuYW1lKCk7XG4gICAgaWYgKG15UGF0aCA9PT0gJzx0ZXh0PicpIHJldHVybiB7fTsgLy8gY2FuJ3QgY3ljbGUtY2hlY2sgYSBub24tZmlsZVxuXG4gICAgY29uc3Qgb3B0aW9ucyA9IGNvbnRleHQub3B0aW9uc1swXSB8fCB7fTtcbiAgICBjb25zdCBtYXhEZXB0aCA9IHR5cGVvZiBvcHRpb25zLm1heERlcHRoID09PSAnbnVtYmVyJyA/IG9wdGlvbnMubWF4RGVwdGggOiBJbmZpbml0eTtcbiAgICBjb25zdCBpZ25vcmVNb2R1bGUgPSAobmFtZSkgPT4gb3B0aW9ucy5pZ25vcmVFeHRlcm5hbCAmJiBpc0V4dGVybmFsTW9kdWxlKFxuICAgICAgbmFtZSxcbiAgICAgIGNvbnRleHQuc2V0dGluZ3MsXG4gICAgICByZXNvbHZlKG5hbWUsIGNvbnRleHQpLFxuICAgICAgY29udGV4dFxuICAgICk7XG5cbiAgICBmdW5jdGlvbiBjaGVja1NvdXJjZVZhbHVlKHNvdXJjZU5vZGUsIGltcG9ydGVyKSB7XG4gICAgICBpZiAoaWdub3JlTW9kdWxlKHNvdXJjZU5vZGUudmFsdWUpKSB7XG4gICAgICAgIHJldHVybjsgLy8gaWdub3JlIGV4dGVybmFsIG1vZHVsZXNcbiAgICAgIH1cblxuICAgICAgaWYgKFxuICAgICAgICBpbXBvcnRlci50eXBlID09PSAnSW1wb3J0RGVjbGFyYXRpb24nICYmIChcbiAgICAgICAgICAvLyBpbXBvcnQgdHlwZSB7IEZvbyB9IChUUyBhbmQgRmxvdylcbiAgICAgICAgICBpbXBvcnRlci5pbXBvcnRLaW5kID09PSAndHlwZScgfHxcbiAgICAgICAgICAvLyBpbXBvcnQgeyB0eXBlIEZvbyB9IChGbG93KVxuICAgICAgICAgIGltcG9ydGVyLnNwZWNpZmllcnMuZXZlcnkoKHsgaW1wb3J0S2luZCB9KSA9PiBpbXBvcnRLaW5kID09PSAndHlwZScpXG4gICAgICAgIClcbiAgICAgICkge1xuICAgICAgICByZXR1cm47IC8vIGlnbm9yZSB0eXBlIGltcG9ydHNcbiAgICAgIH1cblxuICAgICAgY29uc3QgaW1wb3J0ZWQgPSBFeHBvcnRzLmdldChzb3VyY2VOb2RlLnZhbHVlLCBjb250ZXh0KTtcblxuICAgICAgaWYgKGltcG9ydGVkID09IG51bGwpIHtcbiAgICAgICAgcmV0dXJuOyAgLy8gbm8tdW5yZXNvbHZlZCB0ZXJyaXRvcnlcbiAgICAgIH1cblxuICAgICAgaWYgKGltcG9ydGVkLnBhdGggPT09IG15UGF0aCkge1xuICAgICAgICByZXR1cm47ICAvLyBuby1zZWxmLWltcG9ydCB0ZXJyaXRvcnlcbiAgICAgIH1cblxuICAgICAgY29uc3QgdW50cmF2ZXJzZWQgPSBbeyBtZ2V0OiAoKSA9PiBpbXBvcnRlZCwgcm91dGU6W10gfV07XG4gICAgICBjb25zdCB0cmF2ZXJzZWQgPSBuZXcgU2V0KCk7XG4gICAgICBmdW5jdGlvbiBkZXRlY3RDeWNsZSh7IG1nZXQsIHJvdXRlIH0pIHtcbiAgICAgICAgY29uc3QgbSA9IG1nZXQoKTtcbiAgICAgICAgaWYgKG0gPT0gbnVsbCkgcmV0dXJuO1xuICAgICAgICBpZiAodHJhdmVyc2VkLmhhcyhtLnBhdGgpKSByZXR1cm47XG4gICAgICAgIHRyYXZlcnNlZC5hZGQobS5wYXRoKTtcblxuICAgICAgICBmb3IgKGNvbnN0IFtwYXRoLCB7IGdldHRlciwgZGVjbGFyYXRpb25zIH1dIG9mIG0uaW1wb3J0cykge1xuICAgICAgICAgIGlmIChwYXRoID09PSBteVBhdGgpIHJldHVybiB0cnVlO1xuICAgICAgICAgIGlmICh0cmF2ZXJzZWQuaGFzKHBhdGgpKSBjb250aW51ZTtcbiAgICAgICAgICBmb3IgKGNvbnN0IHsgc291cmNlLCBpc09ubHlJbXBvcnRpbmdUeXBlcyB9IG9mIGRlY2xhcmF0aW9ucykge1xuICAgICAgICAgICAgaWYgKGlnbm9yZU1vZHVsZShzb3VyY2UudmFsdWUpKSBjb250aW51ZTtcbiAgICAgICAgICAgIC8vIElnbm9yZSBvbmx5IHR5cGUgaW1wb3J0c1xuICAgICAgICAgICAgaWYgKGlzT25seUltcG9ydGluZ1R5cGVzKSBjb250aW51ZTtcblxuICAgICAgICAgICAgaWYgKHJvdXRlLmxlbmd0aCArIDEgPCBtYXhEZXB0aCkge1xuICAgICAgICAgICAgICB1bnRyYXZlcnNlZC5wdXNoKHtcbiAgICAgICAgICAgICAgICBtZ2V0OiBnZXR0ZXIsXG4gICAgICAgICAgICAgICAgcm91dGU6IHJvdXRlLmNvbmNhdChzb3VyY2UpLFxuICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICAgIH1cblxuICAgICAgd2hpbGUgKHVudHJhdmVyc2VkLmxlbmd0aCA+IDApIHtcbiAgICAgICAgY29uc3QgbmV4dCA9IHVudHJhdmVyc2VkLnNoaWZ0KCk7IC8vIGJmcyFcbiAgICAgICAgaWYgKGRldGVjdEN5Y2xlKG5leHQpKSB7XG4gICAgICAgICAgY29uc3QgbWVzc2FnZSA9IChuZXh0LnJvdXRlLmxlbmd0aCA+IDBcbiAgICAgICAgICAgID8gYERlcGVuZGVuY3kgY3ljbGUgdmlhICR7cm91dGVTdHJpbmcobmV4dC5yb3V0ZSl9YFxuICAgICAgICAgICAgOiAnRGVwZW5kZW5jeSBjeWNsZSBkZXRlY3RlZC4nKTtcbiAgICAgICAgICBjb250ZXh0LnJlcG9ydChpbXBvcnRlciwgbWVzc2FnZSk7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuXG4gICAgcmV0dXJuIG1vZHVsZVZpc2l0b3IoY2hlY2tTb3VyY2VWYWx1ZSwgY29udGV4dC5vcHRpb25zWzBdKTtcbiAgfSxcbn07XG5cbmZ1bmN0aW9uIHJvdXRlU3RyaW5nKHJvdXRlKSB7XG4gIHJldHVybiByb3V0ZS5tYXAocyA9PiBgJHtzLnZhbHVlfToke3MubG9jLnN0YXJ0LmxpbmV9YCkuam9pbignPT4nKTtcbn1cbiJdfQ==