(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (if (null? items) nil
    (cons (proc (car items)) (map proc (cdr items)))
  )
) 
(define (cons-all first rests)
  (define (insert rest)
    (cons first rest))
    (map insert rests)) 

(define (zip pairs)
  'replace-this-line)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
    (define (helper s i new_lst)
      ( if (null? s)
            new_lst
            ;(cons i (car s))))
            (helper (cdr s) (+ i 1) (append new_lst (cons(cons i (cons (car s) nil)) nil   ) ))))

    (helper s 0 ())
)
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (cond 
    ((null? denoms) nil)
    ((= total 0) '(nil))
    ; take out coins that are too big
    ((> (car denoms) total) (list-change total (cdr denoms)))
    ;counting partitions in a way that I couldn't really explain to you well, but have learned to trust anyways
    (else (append 
      (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
      (list-change total (cdr denoms)))
    )
    ) 
)
  
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )))
