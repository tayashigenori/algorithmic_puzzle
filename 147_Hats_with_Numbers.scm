;;;;;;;;;;;;;;;;;;;;
; helper functions ;
;;;;;;;;;;;;;;;;;;;;
; sum
(define (sum numlist)
  (if
    (null? numlist)
    0
    (+ (car numlist) (sum (cdr numlist)))
  )
)

; random
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

; list manipulation
(define (retrieve ls n)
    (if (zero? n)
        (car ls)
        (retrieve (cdr ls) (- n 1))))

;;;;;;;;;;;;;;;;;;
; main functions ;
;;;;;;;;;;;;;;;;;;
; function to guess
(define guess
  (lambda (nums i) ; nums: all numbers
    (modulo (- i
               (- (sum nums) (retrieve nums i)))
            ninzuu)))

; main
(define ninzuu 5)
(define r (rand 1 ninzuu)) ; TODO change seed randomly
(define hats (create_random_list ninzuu))
hats

(define guess_all
  (lambda (hats length)
    (cond
      ((eqv? length 0) `())
      (else
       (cons (guess hats (- ninzuu length))
             (guess_all hats (- length 1)))))))

(define guesses (guess_all hats ninzuu))
guesses
