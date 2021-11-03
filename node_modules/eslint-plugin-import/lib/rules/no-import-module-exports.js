'use strict';var _minimatch = require('minimatch');var _minimatch2 = _interopRequireDefault(_minimatch);
var _path = require('path');var _path2 = _interopRequireDefault(_path);
var _pkgUp = require('pkg-up');var _pkgUp2 = _interopRequireDefault(_pkgUp);function _interopRequireDefault(obj) {return obj && obj.__esModule ? obj : { default: obj };}

function getEntryPoint(context) {
  const pkgPath = _pkgUp2.default.sync(context.getFilename());
  return require.resolve(_path2.default.dirname(pkgPath));
}

module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow import statements with module.exports',
      category: 'Best Practices',
      recommended: true },

    fixable: 'code',
    schema: [
    {
      'type': 'object',
      'properties': {
        'exceptions': { 'type': 'array' } },

      'additionalProperties': false }] },



  create(context) {
    const importDeclarations = [];
    const entryPoint = getEntryPoint(context);
    const options = context.options[0] || {};
    let alreadyReported = false;

    function report(node) {
      const fileName = context.getFilename();
      const isEntryPoint = entryPoint === fileName;
      const isIdentifier = node.object.type === 'Identifier';
      const hasKeywords = /^(module|exports)$/.test(node.object.name);
      const isException = options.exceptions &&
      options.exceptions.some(glob => (0, _minimatch2.default)(fileName, glob));

      if (isIdentifier && hasKeywords && !isEntryPoint && !isException) {
        importDeclarations.forEach(importDeclaration => {
          context.report({
            node: importDeclaration,
            message: `Cannot use import declarations in modules that export using ` +
            `CommonJS (module.exports = 'foo' or exports.bar = 'hi')` });

        });
        alreadyReported = true;
      }
    }

    return {
      ImportDeclaration(node) {
        importDeclarations.push(node);
      },
      MemberExpression(node) {
        if (!alreadyReported) {
          report(node);
        }
      } };

  } };
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi4uLy4uL3NyYy9ydWxlcy9uby1pbXBvcnQtbW9kdWxlLWV4cG9ydHMuanMiXSwibmFtZXMiOlsiZ2V0RW50cnlQb2ludCIsImNvbnRleHQiLCJwa2dQYXRoIiwicGtnVXAiLCJzeW5jIiwiZ2V0RmlsZW5hbWUiLCJyZXF1aXJlIiwicmVzb2x2ZSIsInBhdGgiLCJkaXJuYW1lIiwibW9kdWxlIiwiZXhwb3J0cyIsIm1ldGEiLCJ0eXBlIiwiZG9jcyIsImRlc2NyaXB0aW9uIiwiY2F0ZWdvcnkiLCJyZWNvbW1lbmRlZCIsImZpeGFibGUiLCJzY2hlbWEiLCJjcmVhdGUiLCJpbXBvcnREZWNsYXJhdGlvbnMiLCJlbnRyeVBvaW50Iiwib3B0aW9ucyIsImFscmVhZHlSZXBvcnRlZCIsInJlcG9ydCIsIm5vZGUiLCJmaWxlTmFtZSIsImlzRW50cnlQb2ludCIsImlzSWRlbnRpZmllciIsIm9iamVjdCIsImhhc0tleXdvcmRzIiwidGVzdCIsIm5hbWUiLCJpc0V4Y2VwdGlvbiIsImV4Y2VwdGlvbnMiLCJzb21lIiwiZ2xvYiIsImZvckVhY2giLCJpbXBvcnREZWNsYXJhdGlvbiIsIm1lc3NhZ2UiLCJJbXBvcnREZWNsYXJhdGlvbiIsInB1c2giLCJNZW1iZXJFeHByZXNzaW9uIl0sIm1hcHBpbmdzIjoiYUFBQSxzQztBQUNBLDRCO0FBQ0EsK0I7O0FBRUEsU0FBU0EsYUFBVCxDQUF1QkMsT0FBdkIsRUFBZ0M7QUFDOUIsUUFBTUMsVUFBVUMsZ0JBQU1DLElBQU4sQ0FBV0gsUUFBUUksV0FBUixFQUFYLENBQWhCO0FBQ0EsU0FBT0MsUUFBUUMsT0FBUixDQUFnQkMsZUFBS0MsT0FBTCxDQUFhUCxPQUFiLENBQWhCLENBQVA7QUFDRDs7QUFFRFEsT0FBT0MsT0FBUCxHQUFpQjtBQUNmQyxRQUFNO0FBQ0pDLFVBQU0sU0FERjtBQUVKQyxVQUFNO0FBQ0pDLG1CQUFhLGdEQURUO0FBRUpDLGdCQUFVLGdCQUZOO0FBR0pDLG1CQUFhLElBSFQsRUFGRjs7QUFPSkMsYUFBUyxNQVBMO0FBUUpDLFlBQVE7QUFDTjtBQUNFLGNBQVEsUUFEVjtBQUVFLG9CQUFjO0FBQ1osc0JBQWMsRUFBRSxRQUFRLE9BQVYsRUFERixFQUZoQjs7QUFLRSw4QkFBd0IsS0FMMUIsRUFETSxDQVJKLEVBRFM7Ozs7QUFtQmZDLFNBQU9uQixPQUFQLEVBQWdCO0FBQ2QsVUFBTW9CLHFCQUFxQixFQUEzQjtBQUNBLFVBQU1DLGFBQWF0QixjQUFjQyxPQUFkLENBQW5CO0FBQ0EsVUFBTXNCLFVBQVV0QixRQUFRc0IsT0FBUixDQUFnQixDQUFoQixLQUFzQixFQUF0QztBQUNBLFFBQUlDLGtCQUFrQixLQUF0Qjs7QUFFQSxhQUFTQyxNQUFULENBQWdCQyxJQUFoQixFQUFzQjtBQUNwQixZQUFNQyxXQUFXMUIsUUFBUUksV0FBUixFQUFqQjtBQUNBLFlBQU11QixlQUFlTixlQUFlSyxRQUFwQztBQUNBLFlBQU1FLGVBQWVILEtBQUtJLE1BQUwsQ0FBWWpCLElBQVosS0FBcUIsWUFBMUM7QUFDQSxZQUFNa0IsY0FBZSxvQkFBRCxDQUF1QkMsSUFBdkIsQ0FBNEJOLEtBQUtJLE1BQUwsQ0FBWUcsSUFBeEMsQ0FBcEI7QUFDQSxZQUFNQyxjQUFjWCxRQUFRWSxVQUFSO0FBQ2xCWixjQUFRWSxVQUFSLENBQW1CQyxJQUFuQixDQUF3QkMsUUFBUSx5QkFBVVYsUUFBVixFQUFvQlUsSUFBcEIsQ0FBaEMsQ0FERjs7QUFHQSxVQUFJUixnQkFBZ0JFLFdBQWhCLElBQStCLENBQUNILFlBQWhDLElBQWdELENBQUNNLFdBQXJELEVBQWtFO0FBQ2hFYiwyQkFBbUJpQixPQUFuQixDQUEyQkMscUJBQXFCO0FBQzlDdEMsa0JBQVF3QixNQUFSLENBQWU7QUFDYkMsa0JBQU1hLGlCQURPO0FBRWJDLHFCQUFVLDhEQUFEO0FBQ04scUVBSFUsRUFBZjs7QUFLRCxTQU5EO0FBT0FoQiwwQkFBa0IsSUFBbEI7QUFDRDtBQUNGOztBQUVELFdBQU87QUFDTGlCLHdCQUFrQmYsSUFBbEIsRUFBd0I7QUFDdEJMLDJCQUFtQnFCLElBQW5CLENBQXdCaEIsSUFBeEI7QUFDRCxPQUhJO0FBSUxpQix1QkFBaUJqQixJQUFqQixFQUF1QjtBQUNyQixZQUFJLENBQUNGLGVBQUwsRUFBc0I7QUFDcEJDLGlCQUFPQyxJQUFQO0FBQ0Q7QUFDRixPQVJJLEVBQVA7O0FBVUQsR0F2RGMsRUFBakIiLCJmaWxlIjoibm8taW1wb3J0LW1vZHVsZS1leHBvcnRzLmpzIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IG1pbmltYXRjaCBmcm9tICdtaW5pbWF0Y2gnO1xuaW1wb3J0IHBhdGggZnJvbSAncGF0aCc7XG5pbXBvcnQgcGtnVXAgZnJvbSAncGtnLXVwJztcblxuZnVuY3Rpb24gZ2V0RW50cnlQb2ludChjb250ZXh0KSB7XG4gIGNvbnN0IHBrZ1BhdGggPSBwa2dVcC5zeW5jKGNvbnRleHQuZ2V0RmlsZW5hbWUoKSk7XG4gIHJldHVybiByZXF1aXJlLnJlc29sdmUocGF0aC5kaXJuYW1lKHBrZ1BhdGgpKTtcbn1cblxubW9kdWxlLmV4cG9ydHMgPSB7XG4gIG1ldGE6IHtcbiAgICB0eXBlOiAncHJvYmxlbScsXG4gICAgZG9jczoge1xuICAgICAgZGVzY3JpcHRpb246ICdEaXNhbGxvdyBpbXBvcnQgc3RhdGVtZW50cyB3aXRoIG1vZHVsZS5leHBvcnRzJyxcbiAgICAgIGNhdGVnb3J5OiAnQmVzdCBQcmFjdGljZXMnLFxuICAgICAgcmVjb21tZW5kZWQ6IHRydWUsXG4gICAgfSxcbiAgICBmaXhhYmxlOiAnY29kZScsXG4gICAgc2NoZW1hOiBbXG4gICAgICB7XG4gICAgICAgICd0eXBlJzogJ29iamVjdCcsXG4gICAgICAgICdwcm9wZXJ0aWVzJzoge1xuICAgICAgICAgICdleGNlcHRpb25zJzogeyAndHlwZSc6ICdhcnJheScgfSxcbiAgICAgICAgfSxcbiAgICAgICAgJ2FkZGl0aW9uYWxQcm9wZXJ0aWVzJzogZmFsc2UsXG4gICAgICB9LFxuICAgIF0sXG4gIH0sXG4gIGNyZWF0ZShjb250ZXh0KSB7XG4gICAgY29uc3QgaW1wb3J0RGVjbGFyYXRpb25zID0gW107XG4gICAgY29uc3QgZW50cnlQb2ludCA9IGdldEVudHJ5UG9pbnQoY29udGV4dCk7XG4gICAgY29uc3Qgb3B0aW9ucyA9IGNvbnRleHQub3B0aW9uc1swXSB8fCB7fTtcbiAgICBsZXQgYWxyZWFkeVJlcG9ydGVkID0gZmFsc2U7XG5cbiAgICBmdW5jdGlvbiByZXBvcnQobm9kZSkge1xuICAgICAgY29uc3QgZmlsZU5hbWUgPSBjb250ZXh0LmdldEZpbGVuYW1lKCk7XG4gICAgICBjb25zdCBpc0VudHJ5UG9pbnQgPSBlbnRyeVBvaW50ID09PSBmaWxlTmFtZTtcbiAgICAgIGNvbnN0IGlzSWRlbnRpZmllciA9IG5vZGUub2JqZWN0LnR5cGUgPT09ICdJZGVudGlmaWVyJztcbiAgICAgIGNvbnN0IGhhc0tleXdvcmRzID0gKC9eKG1vZHVsZXxleHBvcnRzKSQvKS50ZXN0KG5vZGUub2JqZWN0Lm5hbWUpO1xuICAgICAgY29uc3QgaXNFeGNlcHRpb24gPSBvcHRpb25zLmV4Y2VwdGlvbnMgJiZcbiAgICAgICAgb3B0aW9ucy5leGNlcHRpb25zLnNvbWUoZ2xvYiA9PiBtaW5pbWF0Y2goZmlsZU5hbWUsIGdsb2IpKTtcblxuICAgICAgaWYgKGlzSWRlbnRpZmllciAmJiBoYXNLZXl3b3JkcyAmJiAhaXNFbnRyeVBvaW50ICYmICFpc0V4Y2VwdGlvbikge1xuICAgICAgICBpbXBvcnREZWNsYXJhdGlvbnMuZm9yRWFjaChpbXBvcnREZWNsYXJhdGlvbiA9PiB7XG4gICAgICAgICAgY29udGV4dC5yZXBvcnQoe1xuICAgICAgICAgICAgbm9kZTogaW1wb3J0RGVjbGFyYXRpb24sXG4gICAgICAgICAgICBtZXNzYWdlOiBgQ2Fubm90IHVzZSBpbXBvcnQgZGVjbGFyYXRpb25zIGluIG1vZHVsZXMgdGhhdCBleHBvcnQgdXNpbmcgYCArXG4gICAgICAgICAgICAgIGBDb21tb25KUyAobW9kdWxlLmV4cG9ydHMgPSAnZm9vJyBvciBleHBvcnRzLmJhciA9ICdoaScpYCxcbiAgICAgICAgICB9KTtcbiAgICAgICAgfSk7XG4gICAgICAgIGFscmVhZHlSZXBvcnRlZCA9IHRydWU7XG4gICAgICB9XG4gICAgfVxuXG4gICAgcmV0dXJuIHtcbiAgICAgIEltcG9ydERlY2xhcmF0aW9uKG5vZGUpIHtcbiAgICAgICAgaW1wb3J0RGVjbGFyYXRpb25zLnB1c2gobm9kZSk7XG4gICAgICB9LFxuICAgICAgTWVtYmVyRXhwcmVzc2lvbihub2RlKSB7XG4gICAgICAgIGlmICghYWxyZWFkeVJlcG9ydGVkKSB7XG4gICAgICAgICAgcmVwb3J0KG5vZGUpO1xuICAgICAgICB9XG4gICAgICB9LFxuICAgIH07XG4gIH0sXG59O1xuIl19