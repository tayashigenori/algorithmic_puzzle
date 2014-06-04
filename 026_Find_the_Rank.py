# -*- coding: utf-8 -*-

import math
import sys

class String(str):
    def __init__(self, s = "", alphabet_dict = {}):
        self._s = s
        self._alphabets = self.get_alphabets()
        return

    def get_alphabets(self,):
        alphabets = [c for c in self._s]
        return sorted(alphabets)

    def find_the_rank(self,):
        ######################################
        # for TURING, count the followings:
        #  - G***** ... 5!
        #  - I***** ... 5!
        #  - N***** ... 5!
        #  - R***** ... 5!
        #  - TG**** ... 4!
        #  - TI**** ... 4!
        #  - TN**** ... 4!
        #  - TR**** ... 4!
        #  - TUG*** ... 3!
        #  - TUI*** ... 3!
        #  - TUN*** ... 3!
        #  - TURG** ... 2!
        #  - TURIG* ... 1!
        #
        # 5! * 4 (G,I,N,R) + 4! * 4 (G,I,N,R) + 3! * 3 (G,I,N) * 2! * 1 (G) + 1! * 1 (N)
        # = 597
        # so "TURING" is the 598th
        ######################################
        rank = 0
        keta = len(self._s)
        for i in range(len(self._s)): # i: 0 ~ 5
            i_mojime = i+1
            c = self._s[i]
            cs_rank_in_alphabet = self._alphabets.index(c)
            sys.stderr.write("### adding math.factorial(%d) * %d\n"
                             %(keta - i_mojime, cs_rank_in_alphabet ))
            rank += math.factorial(keta - i_mojime) * cs_rank_in_alphabet
            # alphabet から使用済みの文字 c を削除
            self._alphabets.remove(c)
        # self._s の前に rank 個の要素がある
        return rank + 1

def main():
    s = String("TURING")
    print s.find_the_rank()

if __name__ == '__main__':
    main()
