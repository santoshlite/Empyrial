"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _helperPluginUtils = require("@babel/helper-plugin-utils");

var _pluginSyntaxClassStaticBlock = _interopRequireDefault(require("@babel/plugin-syntax-class-static-block"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function generateUid(scope, denyList) {
  const name = "";
  let uid;
  let i = 1;

  do {
    uid = scope._generateUid(name, i);
    i++;
  } while (denyList.has(uid));

  return uid;
}

var _default = (0, _helperPluginUtils.declare)(({
  types: t,
  template,
  assertVersion
}) => {
  assertVersion("^7.12.0");
  return {
    name: "proposal-class-static-block",
    inherits: _pluginSyntaxClassStaticBlock.default,
    visitor: {
      Class(path) {
        const {
          scope
        } = path;
        const classBody = path.get("body");
        const privateNames = new Set();
        const body = classBody.get("body");

        for (const path of body) {
          if (path.isPrivate()) {
            privateNames.add(path.get("key.id").node.name);
          }
        }

        for (const path of body) {
          if (!path.isStaticBlock()) continue;
          const staticBlockPrivateId = generateUid(scope, privateNames);
          privateNames.add(staticBlockPrivateId);
          const staticBlockRef = t.privateName(t.identifier(staticBlockPrivateId));
          path.replaceWith(t.classPrivateProperty(staticBlockRef, template.expression.ast`(() => { ${path.node.body} })()`, [], true));
        }
      }

    }
  };
});

exports.default = _default;