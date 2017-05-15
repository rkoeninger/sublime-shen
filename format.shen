
(define dict->'
  D K V -> (do (dict-> D K V) D))

(define @d-macro-h
  N [] -> [dict N]
  N [K V | KVs] -> [dict->' (@d-macro-h N KVs) K V])

(defmacro @d-macro
  [@d | KVs] ->
    (if (= 0 (shen.mod (length KVs) 2))
      (@d-macro-h (/ (length KVs) 2) KVs)
      (error "@d macro requires even number of arguments")))

\\ {number --> list A --> list A}
(define take
  0 _ -> []
  _ [] -> []
  N [X | Xs] -> [X | (take (- N 1) Xs)])

(define take-until-h
  _ Ys [] -> [(reverse Ys) | []]
  F Ys [X | Xs] -> [(reverse Ys) | [X | Xs]] where (F X)
  F Ys [X | Xs] -> (take-until-h [X | Ys] Xs))

\\ {(A --> boolean) --> list A --> list A --> list (list A)}
(define take-until
  F Xs -> (take-until-h F [] Xs))

(define take-until+-h
  _ Ys [] -> [(reverse Ys) | []]
  F Ys [X | Xs] -> [(reverse [X | Ys]) | Xs] where (F X)
  F Ys [X | Xs] -> (take-until+-h [X | Ys] Xs))

\\ {(A --> boolean) --> list A --> list A --> list (list A)}
(define take-until+
  F Xs -> (take-until+-h F [] Xs))

\\ {list A --> number}
(define clause-arity
  Xs -> (length (take-until (= ->) Xs)))

(define take-clause
  ArgCount Xs -> )

(define group-clauses
  _ [] -> []
  N Clauses -> (append  (group-clauses N )))

(define strlen-h
  N "" -> N
  N (@s _ S) -> (strlen-h (+ 1 N) S))

\\ {string --> number}
(define strlen
  Str -> (strlen-h 0 Str))

(define parse-expression
  [define Name { | Body] ->
    (let Split (take-until+ (= }) [] [{ | Body])
      (@d name Name typesig (hd Split) clauses (tl Body)))
  [define Name | Body] -> (@d name Name clauses Body))

(define format-expression
  [define Name | Body] -> []
  [defmacro Name | Body] -> []
  [defprolog Name | Body] -> []
  [defcc Name | Body] -> []
  [datatype | Body] -> []
  [package Name Exports | Body] -> []
  Expr -> Expr)
