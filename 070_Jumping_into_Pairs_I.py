# -*- coding: utf-8 -*-

import sys

COIN_NULL = 0
COIN_SINGLE = 1
COIN_MAX = 2

TO_THE_LEFT = -1
TO_THE_RIGHT = 1

class Coins:
    def __init__(self, n):
        self._coins = dict([(i, COIN_SINGLE) for i in range(n)])
        return

    def move(self, ith, direction = TO_THE_RIGHT):
        sys.stderr.write("### moving %d th coin to the %d direction.\n" %(ith, direction))
        sys.stderr.write("### coins: %s.\n" %(self.get_coins()))
        try:
            self.remove_coin(ith)
            jumped_position = self.jump_n_coins(ith, direction, n = 2)
            self.add_coin(jumped_position)
        except KeyError:
            sys.stderr.write("you can't move %d coin to this direction %d\n" %(ith, direction))
        return

    def remove_coin(self, ith):
        if self._coins[ith] == COIN_NULL:
            raise ValueError, "cannot remove. no coin found in %d th position" %(ith)
        self._coins[ith] -= 1
        return
    def add_coin(self, ith):
        if self._coins[ith] == COIN_NULL:
            raise ValueError, "cannot add. no coin found in %d th position" %(ith)
        if self._coins[ith] >= COIN_MAX:
            raise ValueError, "cannot add. two coins found in %d th position" %(ith)
        self._coins[ith] += 1
        return

    # ２枚見つかったのでさらにその隣（右／左）を返す
    def jump_n_coins(self, ith, direction = TO_THE_RIGHT, n = 2):
        answer = ith
        coins_found = 0
        # coins_found が n+1 以上になったら break
        while coins_found <= n:
            answer += direction
            coins_found += self._coins[answer]
        return answer

    def get_coins(self,):
        return self._coins

    def is_final_state(self, coins = []):
        if isinstance(coins, list) == False or len(coins) == 0:
            coins = self.get_coins()
        result = True
        for c,num in coins.items():
            if num != COIN_MAX and num != COIN_NULL:
                result = False
        return result


def main():
    cs = Coins(n = 8)
    cs.move(ith = 3, direction = TO_THE_RIGHT)
    cs.move(ith = 5, direction = TO_THE_LEFT)
    cs.move(ith = 0, direction = TO_THE_RIGHT)
    cs.move(ith = 4, direction = TO_THE_RIGHT)
    print cs.get_coins()
    print cs.is_final_state(coins = cs.get_coins())

if __name__ == '__main__':
    main()
