# -*- coding: utf-8 -*-

import sys
import random

from Coin import Coin, Coins

class Coin(Coin):
    # fake coin is heavier than authentic ones
    FAKE_COIN_WEIGHT = 11
    AUTHENTIC_COIN_WEIGHT = 10

class FakeCoins:
    def __init__(self, n = 10):
        self._n = n
        self._coinss = []
        self._fake_i = random.randint(0, n - 1)
        for i in range(n):
            is_fake = (i == self._fake_i)
            coins = self._initialize_coins(n, is_fake)
            self._coinss.append( coins )
        return
    def _initialize_coins(self, n = 10, is_fake = False):
        coins = Coins()
        for i in range(n):
            coins.append( Coin(i, is_fake) )
        return coins

    def solve(self,):
        weight_all_authentic = sum(range(1, self._n + 1) * Coin.AUTHENTIC_COIN_WEIGHT)
        weights = []
        # 0 番目の coins から 1枚のコインを、１番目の coins から 2枚のコインを・・・
        for i in range(self._n):
            coins = self._coinss[i]
            weights += [c.get_weight() for c in coins[0:i+1]]
        return sum(weights) - weight_all_authentic - 1

    """
    for validation
    """
    def test_answer(self, answer):
        weights = [[c.get_weight() for c in coins] for coins in self._coinss]
        sys.stderr.write("%s\n" %(weights))
        sys.stderr.write("%d\n" %(self._fake_i))
        return self._fake_i == answer

def main():
    fc = FakeCoins()
    guess = fc.solve()
    print guess
    print fc.test_answer(guess)

if __name__ == '__main__':
    main()
