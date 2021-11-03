'use strict';var _containsPath = require('contains-path');var _containsPath2 = _interopRequireDefault(_containsPath);
var _path = require('path');var _path2 = _interopRequireDefault(_path);

var _resolve = require('eslint-module-utils/resolve');var _resolve2 = _interopRequireDefault(_resolve);
var _moduleVisitor = require('eslint-module-utils/moduleVisitor');var _moduleVisitor2 = _interopRequireDefault(_moduleVisitor);
var _docsUrl = require('../docsUrl');var _docsUrl2 = _interopRequireDefault(_docsUrl);
var _importType = require('../core/importType');var _importType2 = _interopRequireDefault(_importType);function _interopRequireDefault(obj) {return obj && obj.__esModule ? obj : { default: obj };}

module.exports = {
  meta: {
    type: 'problem',
    docs: {
      url: (0, _docsUrl2.default)('no-restricted-paths') },


    schema: [
    {
      type: 'object',
      properties: {
        zones: {
          type: 'array',
          minItems: 1,
          items: {
            type: 'object',
            properties: {
              target: { type: 'string' },
              from: { type: 'string' },
              except: {
                type: 'array',
                items: {
                  type: 'string' },

                uniqueItems: true },

              message: { type: 'string' } },

            additionalProperties: false } },


        basePath: { type: 'string' } },

      additionalProperties: false }] },




  create: function noRestrictedPaths(context) {
    const options = context.options[0] || {};
    const restrictedPaths = options.zones || [];
    const basePath = options.basePath || process.cwd();
    const currentFilename = context.getFilename();
    const matchingZones = restrictedPaths.filter(zone => {
      const targetPath = _path2.default.resolve(basePath, zone.target);

      return (0, _containsPath2.default)(currentFilename, targetPath);
    });

    function isValidExceptionPath(absoluteFromPath, absoluteExceptionPath) {
      const relativeExceptionPath = _path2.default.relative(absoluteFromPath, absoluteExceptionPath);

      return (0, _importType2.default)(relativeExceptionPath, context) !== 'parent';
    }

    function reportInvalidExceptionPath(node) {
      context.report({
        node,
        message: 'Restricted path exceptions must be descendants of the configured `from` path for that zone.' });

    }

    const zoneExceptions = matchingZones.map(zone => {
      const exceptionPaths = zone.except || [];
      const absoluteFrom = _path2.default.resolve(basePath, zone.from);
      const absoluteExceptionPaths = exceptionPaths.map(exceptionPath => _path2.default.resolve(absoluteFrom, exceptionPath));
      const hasValidExceptionPaths = absoluteExceptionPaths.
      every(absoluteExceptionPath => isValidExceptionPath(absoluteFrom, absoluteExceptionPath));

      return {
        absoluteExceptionPaths,
        hasValidExceptionPaths };

    });

    function checkForRestrictedImportPath(importPath, node) {
      const absoluteImportPath = (0, _resolve2.default)(importPath, context);

      if (!absoluteImportPath) {
        return;
      }

      matchingZones.forEach((zone, index) => {
        const absoluteFrom = _path2.default.resolve(basePath, zone.from);

        if (!(0, _containsPath2.default)(absoluteImportPath, absoluteFrom)) {
          return;
        }var _zoneExceptions$index =

        zoneExceptions[index];const hasValidExceptionPaths = _zoneExceptions$index.hasValidExceptionPaths,absoluteExceptionPaths = _zoneExceptions$index.absoluteExceptionPaths;

        if (!hasValidExceptionPaths) {
          reportInvalidExceptionPath(node);
          return;
        }

        const pathIsExcepted = absoluteExceptionPaths.
        some(absoluteExceptionPath => (0, _containsPath2.default)(absoluteImportPath, absoluteExceptionPath));

        if (pathIsExcepted) {
          return;
        }

        context.report({
          node,
          message: `Unexpected path "{{importPath}}" imported in restricted zone.${zone.message ? ` ${zone.message}` : ''}`,
          data: { importPath } });

      });
    }

    return (0, _moduleVisitor2.default)(source => {
      checkForRestrictedImportPath(source.value, source);
    }, { commonjs: true });
  } };
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uLy4uL3NyYy9ydWxlcy9uby1yZXN0cmljdGVkLXBhdGhzLmpzIl0sIm5hbWVzIjpbIm1vZHVsZSIsImV4cG9ydHMiLCJtZXRhIiwidHlwZSIsImRvY3MiLCJ1cmwiLCJzY2hlbWEiLCJwcm9wZXJ0aWVzIiwiem9uZXMiLCJtaW5JdGVtcyIsIml0ZW1zIiwidGFyZ2V0IiwiZnJvbSIsImV4Y2VwdCIsInVuaXF1ZUl0ZW1zIiwibWVzc2FnZSIsImFkZGl0aW9uYWxQcm9wZXJ0aWVzIiwiYmFzZVBhdGgiLCJjcmVhdGUiLCJub1Jlc3RyaWN0ZWRQYXRocyIsImNvbnRleHQiLCJvcHRpb25zIiwicmVzdHJpY3RlZFBhdGhzIiwicHJvY2VzcyIsImN3ZCIsImN1cnJlbnRGaWxlbmFtZSIsImdldEZpbGVuYW1lIiwibWF0Y2hpbmdab25lcyIsImZpbHRlciIsInpvbmUiLCJ0YXJnZXRQYXRoIiwicGF0aCIsInJlc29sdmUiLCJpc1ZhbGlkRXhjZXB0aW9uUGF0aCIsImFic29sdXRlRnJvbVBhdGgiLCJhYnNvbHV0ZUV4Y2VwdGlvblBhdGgiLCJyZWxhdGl2ZUV4Y2VwdGlvblBhdGgiLCJyZWxhdGl2ZSIsInJlcG9ydEludmFsaWRFeGNlcHRpb25QYXRoIiwibm9kZSIsInJlcG9ydCIsInpvbmVFeGNlcHRpb25zIiwibWFwIiwiZXhjZXB0aW9uUGF0aHMiLCJhYnNvbHV0ZUZyb20iLCJhYnNvbHV0ZUV4Y2VwdGlvblBhdGhzIiwiZXhjZXB0aW9uUGF0aCIsImhhc1ZhbGlkRXhjZXB0aW9uUGF0aHMiLCJldmVyeSIsImNoZWNrRm9yUmVzdHJpY3RlZEltcG9ydFBhdGgiLCJpbXBvcnRQYXRoIiwiYWJzb2x1dGVJbXBvcnRQYXRoIiwiZm9yRWFjaCIsImluZGV4IiwicGF0aElzRXhjZXB0ZWQiLCJzb21lIiwiZGF0YSIsInNvdXJjZSIsInZhbHVlIiwiY29tbW9uanMiXSwibWFwcGluZ3MiOiJhQUFBLDZDO0FBQ0EsNEI7O0FBRUEsc0Q7QUFDQSxrRTtBQUNBLHFD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QUFPd0IsS0FBUCxLQUFpQjtBQUNyQyxjQUFNVCxlQUFlYixlQUFLQyxPQUFMLENBQWFmLFFBQWIsRUFBdUJZLEtBQUtqQixJQUE1QixDQUFyQjs7QUFFQSxZQUFJLENBQUMsNEJBQWF1QyxrQkFBYixFQUFpQ1AsWUFBakMsQ0FBTCxFQUFxRDtBQUNuRDtBQUNELFNBTG9DOztBQU9zQkgsdUJBQWVZLEtBQWYsQ0FQdEIsT0FPN0JOLHNCQVA2Qix5QkFPN0JBLHNCQVA2QixDQU9MRixzQkFQSyx5QkFPTEEsc0JBUEs7O0FBU3JDLFlBQUksQ0FBQ0Usc0JBQUwsRUFBNkI7QUFDM0JULHFDQUEyQkMsSUFBM0I7QUFDQTtBQUNEOztBQUVELGNBQU1lLGlCQUFpQlQ7QUFDcEJVLFlBRG9CLENBQ2RwQixxQkFBRCxJQUEyQiw0QkFBYWdCLGtCQUFiLEVBQWlDaEIscUJBQWpDLENBRFosQ0FBdkI7O0FBR0EsWUFBSW1CLGNBQUosRUFBb0I7QUFDbEI7QUFDRDs7QUFFRGxDLGdCQUFRb0IsTUFBUixDQUFlO0FBQ2JELGNBRGE7QUFFYnhCLG1CQUFVLGdFQUErRGMsS0FBS2QsT0FBTCxHQUFnQixJQUFHYyxLQUFLZCxPQUFRLEVBQWhDLEdBQW9DLEVBQUcsRUFGbkc7QUFHYnlDLGdCQUFNLEVBQUVOLFVBQUYsRUFITyxFQUFmOztBQUtELE9BMUJEO0FBMkJEOztBQUVELFdBQU8sNkJBQWVPLE1BQUQsSUFBWTtBQUMvQlIsbUNBQTZCUSxPQUFPQyxLQUFwQyxFQUEyQ0QsTUFBM0M7QUFDRCxLQUZNLEVBRUosRUFBRUUsVUFBVSxJQUFaLEVBRkksQ0FBUDtBQUdELEdBbEhjLEVBQWpCIiwiZmlsZSI6Im5vLXJlc3RyaWN0ZWQtcGF0aHMuanMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgY29udGFpbnNQYXRoIGZyb20gJ2NvbnRhaW5zLXBhdGgnO1xuaW1wb3J0IHBhdGggZnJvbSAncGF0aCc7XG5cbmltcG9ydCByZXNvbHZlIGZyb20gJ2VzbGludC1tb2R1bGUtdXRpbHMvcmVzb2x2ZSc7XG5pbXBvcnQgbW9kdWxlVmlzaXRvciBmcm9tICdlc2xpbnQtbW9kdWxlLXV0aWxzL21vZHVsZVZpc2l0b3InO1xuaW1wb3J0IGRvY3NVcmwgZnJvbSAnLi4vZG9jc1VybCc7XG5pbXBvcnQgaW1wb3J0VHlwZSBmcm9tICcuLi9jb3JlL2ltcG9ydFR5cGUnO1xuXG5tb2R1bGUuZXhwb3J0cyA9IHtcbiAgbWV0YToge1xuICAgIHR5cGU6ICdwcm9ibGVtJyxcbiAgICBkb2NzOiB7XG4gICAgICB1cmw6IGRvY3NVcmwoJ25vLXJlc3RyaWN0ZWQtcGF0aHMnKSxcbiAgICB9LFxuXG4gICAgc2NoZW1hOiBbXG4gICAgICB7XG4gICAgICAgIHR5cGU6ICdvYmplY3QnLFxuICAgICAgICBwcm9wZXJ0aWVzOiB7XG4gICAgICAgICAgem9uZXM6IHtcbiAgICAgICAgICAgIHR5cGU6ICdhcnJheScsXG4gICAgICAgICAgICBtaW5JdGVtczogMSxcbiAgICAgICAgICAgIGl0ZW1zOiB7XG4gICAgICAgICAgICAgIHR5cGU6ICdvYmplY3QnLFxuICAgICAgICAgICAgICBwcm9wZXJ0aWVzOiB7XG4gICAgICAgICAgICAgICAgdGFyZ2V0OiB7IHR5cGU6ICdzdHJpbmcnIH0sXG4gICAgICAgICAgICAgICAgZnJvbTogeyB0eXBlOiAnc3RyaW5nJyB9LFxuICAgICAgICAgICAgICAgIGV4Y2VwdDoge1xuICAgICAgICAgICAgICAgICAgdHlwZTogJ2FycmF5JyxcbiAgICAgICAgICAgICAgICAgIGl0ZW1zOiB7XG4gICAgICAgICAgICAgICAgICAgIHR5cGU6ICdzdHJpbmcnLFxuICAgICAgICAgICAgICAgICAgfSxcbiAgICAgICAgICAgICAgICAgIHVuaXF1ZUl0ZW1zOiB0cnVlLFxuICAgICAgICAgICAgICAgIH0sXG4gICAgICAgICAgICAgICAgbWVzc2FnZTogeyB0eXBlOiAnc3RyaW5nJyB9LFxuICAgICAgICAgICAgICB9LFxuICAgICAgICAgICAgICBhZGRpdGlvbmFsUHJvcGVydGllczogZmFsc2UsXG4gICAgICAgICAgICB9LFxuICAgICAgICAgIH0sXG4gICAgICAgICAgYmFzZVBhdGg6IHsgdHlwZTogJ3N0cmluZycgfSxcbiAgICAgICAgfSxcbiAgICAgICAgYWRkaXRpb25hbFByb3BlcnRpZXM6IGZhbHNlLFxuICAgICAgfSxcbiAgICBdLFxuICB9LFxuXG4gIGNyZWF0ZTogZnVuY3Rpb24gbm9SZXN0cmljdGVkUGF0aHMoY29udGV4dCkge1xuICAgIGNvbnN0IG9wdGlvbnMgPSBjb250ZXh0Lm9wdGlvbnNbMF0gfHwge307XG4gICAgY29uc3QgcmVzdHJpY3RlZFBhdGhzID0gb3B0aW9ucy56b25lcyB8fCBbXTtcbiAgICBjb25zdCBiYXNlUGF0aCA9IG9wdGlvbnMuYmFzZVBhdGggfHwgcHJvY2Vzcy5jd2QoKTtcbiAgICBjb25zdCBjdXJyZW50RmlsZW5hbWUgPSBjb250ZXh0LmdldEZpbGVuYW1lKCk7XG4gICAgY29uc3QgbWF0Y2hpbmdab25lcyA9IHJlc3RyaWN0ZWRQYXRocy5maWx0ZXIoKHpvbmUpID0+IHtcbiAgICAgIGNvbnN0IHRhcmdldFBhdGggPSBwYXRoLnJlc29sdmUoYmFzZVBhdGgsIHpvbmUudGFyZ2V0KTtcblxuICAgICAgcmV0dXJuIGNvbnRhaW5zUGF0aChjdXJyZW50RmlsZW5hbWUsIHRhcmdldFBhdGgpO1xuICAgIH0pO1xuXG4gICAgZnVuY3Rpb24gaXNWYWxpZEV4Y2VwdGlvblBhdGgoYWJzb2x1dGVGcm9tUGF0aCwgYWJzb2x1dGVFeGNlcHRpb25QYXRoKSB7XG4gICAgICBjb25zdCByZWxhdGl2ZUV4Y2VwdGlvblBhdGggPSBwYXRoLnJlbGF0aXZlKGFic29sdXRlRnJvbVBhdGgsIGFic29sdXRlRXhjZXB0aW9uUGF0aCk7XG5cbiAgICAgIHJldHVybiBpbXBvcnRUeXBlKHJlbGF0aXZlRXhjZXB0aW9uUGF0aCwgY29udGV4dCkgIT09ICdwYXJlbnQnO1xuICAgIH1cblxuICAgIGZ1bmN0aW9uIHJlcG9ydEludmFsaWRFeGNlcHRpb25QYXRoKG5vZGUpIHtcbiAgICAgIGNvbnRleHQucmVwb3J0KHtcbiAgICAgICAgbm9kZSxcbiAgICAgICAgbWVzc2FnZTogJ1Jlc3RyaWN0ZWQgcGF0aCBleGNlcHRpb25zIG11c3QgYmUgZGVzY2VuZGFudHMgb2YgdGhlIGNvbmZpZ3VyZWQgYGZyb21gIHBhdGggZm9yIHRoYXQgem9uZS4nLFxuICAgICAgfSk7XG4gICAgfVxuXG4gICAgY29uc3Qgem9uZUV4Y2VwdGlvbnMgPSBtYXRjaGluZ1pvbmVzLm1hcCgoem9uZSkgPT4ge1xuICAgICAgY29uc3QgZXhjZXB0aW9uUGF0aHMgPSB6b25lLmV4Y2VwdCB8fCBbXTtcbiAgICAgIGNvbnN0IGFic29sdXRlRnJvbSA9IHBhdGgucmVzb2x2ZShiYXNlUGF0aCwgem9uZS5mcm9tKTtcbiAgICAgIGNvbnN0IGFic29sdXRlRXhjZXB0aW9uUGF0aHMgPSBleGNlcHRpb25QYXRocy5tYXAoKGV4Y2VwdGlvblBhdGgpID0+IHBhdGgucmVzb2x2ZShhYnNvbHV0ZUZyb20sIGV4Y2VwdGlvblBhdGgpKTtcbiAgICAgIGNvbnN0IGhhc1ZhbGlkRXhjZXB0aW9uUGF0aHMgPSBhYnNvbHV0ZUV4Y2VwdGlvblBhdGhzXG4gICAgICAgIC5ldmVyeSgoYWJzb2x1dGVFeGNlcHRpb25QYXRoKSA9PiBpc1ZhbGlkRXhjZXB0aW9uUGF0aChhYnNvbHV0ZUZyb20sIGFic29sdXRlRXhjZXB0aW9uUGF0aCkpO1xuXG4gICAgICByZXR1cm4ge1xuICAgICAgICBhYnNvbHV0ZUV4Y2VwdGlvblBhdGhzLFxuICAgICAgICBoYXNWYWxpZEV4Y2VwdGlvblBhdGhzLFxuICAgICAgfTtcbiAgICB9KTtcblxuICAgIGZ1bmN0aW9uIGNoZWNrRm9yUmVzdHJpY3RlZEltcG9ydFBhdGgoaW1wb3J0UGF0aCwgbm9kZSkge1xuICAgICAgY29uc3QgYWJzb2x1dGVJbXBvcnRQYXRoID0gcmVzb2x2ZShpbXBvcnRQYXRoLCBjb250ZXh0KTtcblxuICAgICAgaWYgKCFhYnNvbHV0ZUltcG9ydFBhdGgpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuXG4gICAgICBtYXRjaGluZ1pvbmVzLmZvckVhY2goKHpvbmUsIGluZGV4KSA9PiB7XG4gICAgICAgIGNvbnN0IGFic29sdXRlRnJvbSA9IHBhdGgucmVzb2x2ZShiYXNlUGF0aCwgem9uZS5mcm9tKTtcblxuICAgICAgICBpZiAoIWNvbnRhaW5zUGF0aChhYnNvbHV0ZUltcG9ydFBhdGgsIGFic29sdXRlRnJvbSkpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cblxuICAgICAgICBjb25zdCB7IGhhc1ZhbGlkRXhjZXB0aW9uUGF0aHMsIGFic29sdXRlRXhjZXB0aW9uUGF0aHMgfSA9IHpvbmVFeGNlcHRpb25zW2luZGV4XTtcblxuICAgICAgICBpZiAoIWhhc1ZhbGlkRXhjZXB0aW9uUGF0aHMpIHtcbiAgICAgICAgICByZXBvcnRJbnZhbGlkRXhjZXB0aW9uUGF0aChub2RlKTtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cblxuICAgICAgICBjb25zdCBwYXRoSXNFeGNlcHRlZCA9IGFic29sdXRlRXhjZXB0aW9uUGF0aHNcbiAgICAgICAgICAuc29tZSgoYWJzb2x1dGVFeGNlcHRpb25QYXRoKSA9PiBjb250YWluc1BhdGgoYWJzb2x1dGVJbXBvcnRQYXRoLCBhYnNvbHV0ZUV4Y2VwdGlvblBhdGgpKTtcblxuICAgICAgICBpZiAocGF0aElzRXhjZXB0ZWQpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cblxuICAgICAgICBjb250ZXh0LnJlcG9ydCh7XG4gICAgICAgICAgbm9kZSxcbiAgICAgICAgICBtZXNzYWdlOiBgVW5leHBlY3RlZCBwYXRoIFwie3tpbXBvcnRQYXRofX1cIiBpbXBvcnRlZCBpbiByZXN0cmljdGVkIHpvbmUuJHt6b25lLm1lc3NhZ2UgPyBgICR7em9uZS5tZXNzYWdlfWAgOiAnJ31gLFxuICAgICAgICAgIGRhdGE6IHsgaW1wb3J0UGF0aCB9LFxuICAgICAgICB9KTtcbiAgICAgIH0pO1xuICAgIH1cblxuICAgIHJldHVybiBtb2R1bGVWaXNpdG9yKChzb3VyY2UpID0+IHtcbiAgICAgIGNoZWNrRm9yUmVzdHJpY3RlZEltcG9ydFBhdGgoc291cmNlLnZhbHVlLCBzb3VyY2UpO1xuICAgIH0sIHsgY29tbW9uanM6IHRydWUgfSk7XG4gIH0sXG59O1xuIl19