; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (if(null? (cdr s))
      nil
      (car (cdr s))
      )  
)

(define (caddr s)
  (if(null? (cddr s))
      nil
      (car (cddr s)) 
      )
)

(define (sign x)
  (cond 
    ((< x 0) 
      -1)
    ((= x 0)
      0)
    (else 1)
    )

)

(define (ordered? s)
  (if (null? s)
      true
      (cond
        ( (null? (cdr s))
          true)
        ((> (car s) (cadr s))
            false) 
        (else (ordered? (cdr s)))
      )
  )
)


(define (nodots s)
  (cond 
    ((null? s) 
      nil)

    ((and (pair? s) (null? (cdr s))) 
        s);(cons (car s) nil))
     ((not (pair? s)) 
        (cons s nil))
     ((and (pair? s) (pair? (car s))) 
      (cons (cons (car(car s))  (nodots (cdr(car s))))  (nodots (cdr s))) 
      )

    (else (cons (car s) (nodots (cdr s)) ) ) 
    )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((= v (car s)) True)
          (else (contains? (cdr s) v) ; replace this line
          )
          )
    )

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((contains? s v) s)
          ( (and (not (contains? s v)) (< v (car s) )) 
            (cons v s))
          (else (cons (car s) (add (cdr s) v))) ; replace this line
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) 
            (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s)  t))

          (else (intersect s (cdr t) )) 
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)

          ((= (car s) (car t)) 
            (cons (car s) (union (cdr s) (cdr t) )))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t ) ) ) 
          (else (cons (car t) (union s (cdr t) ))) ; replace this line
          ))

; Tail-Calls in Scheme

(define (exp-recursive b n)
  (if (= n 0)
      1
      (* b (exp-recursive b (- n 1)))))

(define (exp b n)
  (define (exp-optimized b n total)
    (if (= n 0)
      total 
      (exp-optimized b (- n 1) (* total b)))
  )
  (exp-optimized b n 1)
)

(define (filter pred lst)
  (define (filter-helper pred lst count new_lst)
    (cond 
      ((= count 0) new_lst)
      ((and (pred (car lst)) (null? new_lst))  
        (filter-helper pred (cdr lst) (- count 1)  (list (car lst))))
      ( (and (pred (car lst)) (not (null? new_lst)))
        (filter-helper pred (cdr lst) (- count 1)  (append new_lst (list (car lst)) ))) 
      (else (filter-helper pred (cdr lst) (- count 1) new_lst))
      )
    )
  (filter-helper pred lst (length lst) '())
)