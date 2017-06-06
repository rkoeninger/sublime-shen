# Sublime/Shen

[Shen language](http://www.shenlanguage.org/) support for [Sublime Text 3](https://www.sublimetext.com/).

## Features

  * Syntax Highlighting - detects files matching the pattern `*.shen`.
  * Comments - Applies Shen-style single line (`\\`) and multi-line (`\* ... *\`) comments using standard commands/shortcuts.
  * Snippets - generate skeleton forms for `define`, `defmacro`, `defcc`, `defprolog`, etc.

## Preview

![Screenshot](https://raw.githubusercontent.com/rkoeninger/sublime-shen/master/screenshot.png)

## github/linguist

This repo is also a submodule of GitHub's [Linguist](https://github.com/github/linguist) library, allowing syntax highlighting of Shen on Github:

```shen
\* multi
   line
   block
   comment *\

(define special-keywords ->
  (do
    (set *language* (value *custom*))
    (trap-error
      (do (simple-error "whoops!") (error "oh, no!"))
      (lambda E (output "~S" (error-to-string E)))
      (/. E (print (error-to-string E) (stoutput))))
    skip))

(define typed-function {A --> (list A) --> boolean}
  _ [] -> [true define 0123 false] (f true define +323)
  X [X | _] -> true \\ end of line comment
  X [{ | Xs] -> [0a X Xs ()])

(defcc <rule>
  <patterns> -> <action> where <guard> := [<patterns> [where <guard> <action>]];
  <patterns> <- <action> where <guard> := [<patterns> [where <guard> [choicepoint! <action>]]];)

(define strings ->
  (cases
    (= X (and Y Z))
      (output "~%Shen, copyright c#123; c#dfc; 2010-2015 c#; Mark Tarver~%")
    (not (< Qwe Asd))
      (output "www.shenlanguage.org, ~A~%" (value *version*))
    true
      (output "~%port ~A ported by ~A~%"
        (value *port*)
        (value *porters*))))
```

## Automatic Installation

Sublime/Shen is available from [Package Control](https://packagecontrol.io/packages/Shen) under the name `Shen`.

## Manual Installation

Download this repo as an archive or `git clone` it under the `Packages` directory under your Sublime user path.

On Windows, this is something like `C:\Users\%USER_NAME%\AppData\Roaming\Sublime Text 3\Packages`.

Once the `sublime-shen` package is in place, just restart Sublime, and it should be ready to go.

## Future Work

  * Formatting
  * Linting
  * Suggested Refactors
  * Build System

## Contributing

Use [PackageDev](https://packagecontrol.io/packages/PackageDev) for Sublime to edit syntax definitions. Make changes to `Shen.YAML-tmLanguage` and then re-generate `Shen.tmLangauge` by hitting <kbd>F7</kbd>. Edits made directly to `Shen.tmLanguage` will get overwritten.
