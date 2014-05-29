
(load "random.scm")
(load "list.scm")

(define guess
  (lambda (nums i) ; nums: all numbers including me
    (modulo (- i
               (- (sum nums) (retrieve nums i)))
            ninzuu)))

(define guess_all
  (lambda (hats length)
    (cond
      ((eqv? length 0) `())
      (else
       (cons (guess hats ; all hat numbers
                    (- ninzuu length)) ; this is (- ninzuu length)th member
             (guess_all hats (- length 1)))))))

; print
(define display_output
  (lambda (header list)
    (display header)
    (display list)
    (display "\n")))

; main
(define ninzuu 10)
(define r (rand 1 ninzuu)) ; TODO change seed randomly

(define hats (create_random_list ninzuu))
(display_output "hats:\t\t" hats)

(define guesses (guess_all hats ninzuu))
(display_output "guesses:\t" guesses)
