// Quick Take

import { strict as assert } from "assert";
import { conv } from "../dist/color-shorthand-hex-to-six-digit.esm.js";

// converts shorthand hex color codes within strings (imagine that could be
// email template source code):
assert.equal(
  conv("aaaa #f0c zzzz\n\t\t\t#fc0"),
  "aaaa #ff00cc zzzz\n\t\t\t#ffcc00"
);

// converts shorthand hex colour codes within plain objects:
assert.deepEqual(
  conv({
    a: "#ffcc00",
    b: "#f0c",
    c: "text",
  }),
  {
    a: "#ffcc00",
    b: "#ff00cc",
    c: "text",
  }
);

// converts shorthand hex colour codes within arrays:
assert.deepEqual(conv(["#fc0", "#f0c", "text", ""]), [
  "#ffcc00",
  "#ff00cc",
  "text",
  "",
]);

// converts shorthand hex colour codes within nested spaghetti's:
assert.deepEqual(
  conv([[[[[[{ x: ["#fc0"] }]]]]], { z: "#f0c" }, ["text"], { y: "" }]),
  [[[[[[{ x: ["#ffcc00"] }]]]]], { z: "#ff00cc" }, ["text"], { y: "" }]
);

// in all other cases it silently returns the input:
assert.equal(conv(null), null);
