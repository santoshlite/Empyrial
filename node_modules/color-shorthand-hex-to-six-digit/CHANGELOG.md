# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

## 3.0.1 (2021-01-28)

### Bug Fixes

- add testStats to npmignore ([f3c84e9](https://github.com/codsen/codsen/commit/f3c84e95afc5514214312f913692d85b2e12eb29))

## 3.0.0 (2021-01-23)

### Features

- rewrite in TS, start using named exports ([df180c5](https://github.com/codsen/codsen/commit/df180c5d3f1413ea826e8f771ea57492d3378189))

### BREAKING CHANGES

- previously: `import conv from ...` - now `import { conv } from ...`

## 2.11.0 (2020-11-28)

Accidental version bump during migration to sourcehut. Sorry about that.

## 2.10.0 (2019-01-20)

- ✨ Various documentation and setup tweaks after we migrated to monorepo
- ✨ Setup refresh: updated dependencies and all config files using automated tools

## 2.4.0 (2018-10-15)

- ✨ Updated all dependencies and restored coverage tracking both via terminal when testing and through coveralls.io

## 2.3.0 (2018-06-27)

- ✨ Set up Rollup to remove any comments from build files
- ✨ Attempt to fix reported issues with UMD builds `undefined$3` variable not found

## 2.2.0 (2018-06-08)

### Added

- ✨ Fixed false positive cases of HTML entities, for example `&#124;`. Thanks James Kupczak!
- ✨ Rebased a little
- ✨ Migrated to BitBucket...
- ✨ ...which means we dropped Travis. But we kept Coveralls.
- ✨ RIP BitHound

## 2.1.0 (2018-05-03)

### Added

- ✨ Set up [Prettier](https://prettier.io)
- ✨ Removed `package.lock` and `.editorconfig`
- ✨ Wired Rollup to remove comments from non-dev builds. This means we can now leave the `console.log`s in the source code — Rollup will remove from production code.

## 2.0.0 (2017-12-06)

### Changed

- ✨ Rebased in ES Modules
- ✨ Set up Rollup (nice rhyming), now generating transpiled CommonJS, UMD and native ES Module builds.

Bumping major just in case it breaks somebody's API. It shouldn't though.

## 1.5.0 (2017-05-25)

### Updated

- Dependencies to request the latest `_.clonedeep`
- Readme, added more examples

## 1.4.0 (2017-03-06)

### Added

- More unit tests to cover XHTML code.

## 1.3.0 (2017-03-02)

### Tweaked

- Now any input args are not mutated. Ever.

## 1.2.0 (2017-02-17)

### Added

- Table of Contents in README

### Tweaked

- Set up blanket deps ranges because it's tedious to update them and these deps never breaking-change
- Updated company name in README and LICENSE

## 1.1.0 (2017-01-09)

### Added

- All hex codes, three and six digits long, are converted to lowercase. This is to prevent case mismatches.
- Test 05.01 to prove this works as intended.

## 1.0.0 (2017-01-06)

Initial release. 100% test coverage.
