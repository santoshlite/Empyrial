var assert = require('assert');
var cssUrl = require('..');

describe('css-url-regex', function() {

  it('should find a css url with no quotes', function() {
    assert.equal(cssUrl().test('url(foo.css)'), true);
  });

  it('should find a css url with quotes', function() {
    assert.equal(cssUrl().test("url('foo.css')"), true);
  });

  it('should not find a css url if it is not there', function() {
    assert.equal(cssUrl().test("('foo.css')"), false);
  });

  it('should match multiple urls', function() {
    assert.deepEqual(
      "url(foo.css); url(bar.css);".match(cssUrl()),
      ["url(foo.css)", "url(bar.css)"]);
  });
});
