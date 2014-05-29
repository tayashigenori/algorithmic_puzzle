
(define (sum numlist)
  (if
    (null? numlist)
    0
    (+ (car numlist) (sum (cdr numlist)))
  )
)

(define (retrieve ls n)
    (if (zero? n)
        (car ls)
        (retrieve (cdr ls) (- n 1))))
