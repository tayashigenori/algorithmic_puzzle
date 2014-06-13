# -*- coding: utf-8 -*-

import sys
import random

from Coin import Coin, Coins

fake_is_lighter = random.randint(0, 1)
if fake_is_lighter == 1:
    class UnknownCoin(Coin):
        # fake coin is lighter than authentic ones
        FAKE_COIN_WEIGHT = 10
        AUTHENTIC_COIN_WEIGHT = 11
else:
    class UnknownCoin(Coin):
        # fake coin is heavier than authentic ones
        FAKE_COIN_WEIGHT = 11
        AUTHENTIC_COIN_WEIGHT = 10

class FakeCoins:
    def __init__(self, n = 8):
        self._n = n
        self._coins = self._initialize_coins(n)
        return
    def _initialize_coins(self, n):
        coins = Coins()
        fake_i = random.randint(0, n - 1)
        for i in range(n):
            is_fake = (i == fake_i)
            coins.append( UnknownCoin(i, is_fake) )
        return coins
    def get_coins(self,):
        return self._coins

    def solve(self, verbose = True):
        if self._n % 2 == 0:
            others_len = 2
        else:
            others_len = 1
        (g1, g2) = ((self._n - others_len) / 2,
                    (self._n - others_len) / 2)
        # １回目の分割
        (coins1, coins2, others) = self._coins._split_coins(g1, g2)
        ### for debug
        if verbose == True:
            coins1.show_weights()
            coins2.show_weights()
            others.show_weights()
        # １回目の計測
        if coins1.is_eq(coins2):
            sys.stderr.write("### coins1 equal to coins2.\n")
            # 偽物は others の中にある
            # ２回目の計測
            authentic_coins = Coins( random.sample(coins1, others_len) )
            if others.is_lt(authentic_coins):
                sys.stderr.write("### others are fake and lighter.\n")
                fake_is_lighter = True
            else:
                sys.stderr.write("### others are fake and heavier.\n")
                fake_is_lighter = False
            return fake_is_lighter
        elif coins1.is_lt(coins2):
            sys.stderr.write("### coins1 is lighter.\n")
            lighter_coins = coins1
        else:
            sys.stderr.write("### coins2 is lighter.\n")
            lighter_coins = coins2
        # ２回目の分割
        if len(lighter_coins) % 2 == 0:
            pass
        else:
            authentic_coin = random.sample(others, 1)
            lighter_coins += authentic_coin
        l = len(lighter_coins) / 2
        (lighter_coins1, lighter_coins2, others) = lighter_coins._split_coins(l, l)
        ### for debug
        if verbose == True:
            lighter_coins1.show_weights()
            lighter_coins2.show_weights()
            others.show_weights()
        if lighter_coins1.is_eq(lighter_coins2):
            sys.stderr.write("### lighter_coins1 equals to lighter_coins2.\n")
            sys.stderr.write("### lighter_coins are authentic.\n")
            fake_is_lighter = False
        else:
            sys.stderr.write("### lighter_coins1 does not eequal to lighter_coins2.\n")
            sys.stderr.write("### lighter_coins are fake.\n")
            fake_is_lighter = True
        return fake_is_lighter

    """
    for validation
    """
    def test_answer(self, guess):
        self._coins.show_weights()
        sys.stderr.write("### authentic coin weight: %d\n"
                         %(UnknownCoin.AUTHENTIC_COIN_WEIGHT))
        sys.stderr.write("### fake coin weight: %d\n"
                         %(UnknownCoin.FAKE_COIN_WEIGHT))
        return guess == (UnknownCoin.AUTHENTIC_COIN_WEIGHT > UnknownCoin.FAKE_COIN_WEIGHT)

def main():
    fc = FakeCoins()
    guess = fc.solve()
    print "fake is lighter? guess ->", guess
    print "is the guess correct? ->", fc.test_answer(guess)

if __name__ == '__main__':
    main()
