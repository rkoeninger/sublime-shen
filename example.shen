#!/bin/she bang -x

\\ single line comment

"root-level string"

123

(define root-level-function
  Var lit -> (+ (* X X) (/ Y Y) (- Z Z)))

\* block comment *\

(package example []

  (define special-keywords ->
    (do
      (set *language* (value *custom*))
      (trap-error
        (do (simple-error "whoops!") (error "oh, no!"))
        (lambda E (output "~S" (error-to-string E)))
        (/. E (print (error-to-string E) (stoutput))))
      skip))

  \* multi
     line
     block
     comment *\

  (define typed-function {A --> (list A) --> boolean}
    _ [] -> (true 0123 false)
    X [X | _] -> true \\ end of line comment
    X [{ | Xs] -> [0a X Xs ()])

  (datatype maybe
    H : boolean; X : A;
    ____________________
    [H | X] : (maybe A);)

  (defmacro syntax-magic
    [@p] -> [} ++--+-+012323.2434])

  "package-level string"

  (defcc <rule>
    <patterns> -> <action> where <guard> := [<patterns> [where <guard> <action>]];
    <patterns> <- <action> where <guard> := [<patterns> [where <guard> [choicepoint! <action>]]];)

  (define strings ->
    (case
      (= X (and Y Z))
        (output "~%Shen, copyright c#123; 2010-2015 Mark Tarver~%")
      (not (< Qwe Asd))
        (output "www.shenlanguage.org, ~A~%" (value *version*))
      true
        (output "~%port ~A ported by ~A~%"
          (value *port*)
          (value *porters*))))

  (defprolog mem
    X [X | _] <--;
    X [Y | Z] <-- (mem X Z);))
