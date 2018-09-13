# Sublime/Shen

[Shen language](http://www.shenlanguage.org/) support for [Sublime Text 3](https://www.sublimetext.com/).

## Features

  * Syntax Highlighting - detects files matching the pattern `*.shen`.
  * Comments - Applies Shen-style single line (`\\`) and multi-line (`\* ... *\`) comments using standard commands/shortcuts.
  * Snippets - generate skeleton forms for `define`, `defmacro`, `defcc`, `defprolog`, etc.

## Preview

![Screenshot](https://raw.githubusercontent.com/rkoeninger/sublime-shen/master/screenshot.png)

## Installation

Sublime/Factor is available from [Package Control](https://packagecontrol.io/packages/Factor) under the name `Factor`.

## Future Work

  * Formatting
  * Linting
  * Suggested Refactors
  * Build System

## Contributing

Use [PackageDev](https://packagecontrol.io/packages/PackageDev) for Sublime to edit syntax definitions. Make changes to `Shen.YAML-tmLanguage` and then re-generate `Shen.tmLangauge` by hitting <kbd>F7</kbd>. Edits made directly to `Shen.tmLanguage` will get overwritten.
