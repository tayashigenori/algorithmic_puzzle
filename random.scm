
(define (rand seed upper)
  (let ((x seed))
    (lambda ()
      (set! x (remainder (+ (* 13 x) 5) upper))
      x)))

(define create_random_list
  (lambda (length)
    (cond
      ((eqv? length 0) `())
      (else
       (cons (r) (create_random_list (- length 1)))))))
