#!/bin/shebang

\\ single line comment

"root-level string"

(define root-level-function
  Var lit -> (+ (* X X) (/ Y Y) (- Z Z)))

\* block comment *\

(package example []

  (define special-keywords ->
    (do
      (set *language* (value *custom*))
      (trap-error
        (simple-error "whoops!")
        (/. E (print (error-to-string E) (stoutput))))
      skip))

  \* multi
     line
     block
     comment *\

  (define typed-function {A --> (list A) --> boolean}
    _ [] -> (true 0 false)
    X [X | _] -> true \\ end of line comment
    X [{ | Xs] -> [0 X Xs ()])

  (defmacro syntax-magic
    [@p] -> [} +++---+012323])

  (define conditionals
    X Y Z -> (if (and X Y) (or (and Y X) Z) (not (and Y X))))

  "package-level string"

  (defcc <rule>
    <patterns> -> <action> where <guard> := [<patterns> [where <guard> <action>]];
    <patterns> -> <action> := [<patterns> <action>];
    <patterns> <- <action> where <guard>
        := [<patterns> [where <guard> [choicepoint! <action>]]];
    <patterns> <- <action> := [<patterns> [choicepoint! <action>]];)

  (define strings ->
    (do
      (output "~%Shen, copyright c#123; 2010-2015 Mark Tarver~%")
      (output "www.shenlanguage.org, ~A~%"
        (value *version*))
      (output "running under ~A, implementation: ~A"
        (value *language*)
        (value *implementation*))
      (output "~%port ~A ported by ~A~%"
        (value *port*)
        (value *porters*))))

  (defprolog mem
    X [X | _] <--;
    X [Y | Z] <-- (mem X Z);))
