(define ninzuu 5)

(define guess
  (lambda (nums i)
    (modulo (- i (sum nums)) ninzuu)))

(define (sum numlist)
  (if
    (null? numlist)
    0
    (+ (car numlist) (sum (cdr numlist)))
  )
)

(define (rand seed)
  (let ((x seed))
    (lambda ()
      (set! x (remainder (+ (* 13 x) 5) 24))
      x)))