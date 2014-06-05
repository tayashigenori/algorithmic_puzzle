# -*- coding: utf-8 -*-

######################
## does not work yet
######################

import sys

COIN_NULL = 0
COIN_SINGLE = 1
COIN_DOUBLE = 2

TO_THE_LEFT = -1
TO_THE_RIGHT = 1

class Coins:
    def __init__(self, n):
        self._coins = dict([(i, COIN_SINGLE) for i in range(n)])
        return

    def move(self, ith, direction = TO_THE_RIGHT):
        try:
            self.remove_coin(ith)
            jumped_position = self.jump_n_coins(ith, direction, n = 2)
            self.add_coin(ith)
        except KeyError:
            sys.stderr.write("you can't move %d coin to this direction %d\n" %(ith, direction))
        return

    def remove_coin(self, ith):
        self._coins[ith] += 1
        return
    def add_coin(self, ith):
        self._coins[ith] += 1
        return

    def jump_n_coins(self, ith, direction = TO_THE_RIGHT, n = 2):
        answer = ith
        coins_found = 0
        while True:
            answer += direction
            coins_found += self._coins[answer]
            if coins_found == n:
                break
            if coins_found >= n + 1:
                raise ValueError, "%d + 1 coins found in this direction %d" %(n, direction)
        return answer

    def get_coins(self,):
        return self._coins


def main():
    cs = Coins(n = 8)
    cs.move(ith = 3, direction = TO_THE_RIGHT)
    cs.move(ith = 5, direction = TO_THE_LEFT)
    cs.move(ith = 0, direction = TO_THE_RIGHT)
    cs.move(ith = 4, direction = TO_THE_RIGHT)
    print cs.get_coins()

if __name__ == '__main__':
    main()
