# -*- coding: utf-8 -*-

import sys
import random

# fake coin is lighter than authentic ones
FAKE_COIN_WEIGHT = 10
AUTHENTIC_COIN_WEIGHT = 11

class Coin:
    def __init__(self, i, is_fake = False):
        self._i = i
        self._is_fake = is_fake
        if is_fake == True:
            self._weight = FAKE_COIN_WEIGHT
        else:
            self._weight = AUTHENTIC_COIN_WEIGHT
        return
    def get_index(self):
        return self._i
    def is_fake(self):
        return self._is_fake
    def get_weight(self,):
        return self._weight

    def is_gt(self, another_coin): # is greater than
        return self.get_weight() > another_coin.get_weight()
    def is_eq(self, another_coin): # is equal
        return self.get_weight() == another_coin.get_weight()

    def is_ge(self, another_coin): # is greater than or equal
        return self.is_gt(another_coin) or self.is_eq(another_coin)

    def is_le(self, another_coin): # is less than or equal
        return not self.is_gt(another_coin)
    def is_lt(self, another_coin): # is less than
        return not self.is_ge(another_coin)

class Coins(list):
    def is_gt(self, other_coins): # is greater than
        this_weight = sum([c.get_weight() for c in self])
        other_weight = sum([c.get_weight() for c in other_coins])
        return this_weight > other_weight
    def is_eq(self, other_coins): # is equal
        this_weight = sum([c.get_weight() for c in self])
        other_weight = sum([c.get_weight() for c in other_coins])
        return this_weight == other_weight

    def is_ge(self, other_coins): # is greater than or equal
        return self.is_gt(other_coins) or self.is_eq(other_coins)

    def is_le(self, other_coins): # is less than or equal
        return not self.is_gt(other_coins)
    def is_lt(self, other_coins): # is less than
        return not self.is_ge(other_coins)


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
            coins.append( Coin(i, is_fake) )
        return coins
    def get_coins(self,):
        return self._coins

    # this works only for n = 8
    def solve(self, verbose = True):
        # １回目の分割
        (coins1, coins2, others) = self._split_coins(self._coins,
                                                     g1 = 3, g2 = 3)
        ### for debug
        if verbose == True:
            sys.stderr.write("### coins1: %s\n### coins2: %s\n### others: %s\n"
                             %(coins1, coins2, others))
            self.show_weights(coins1)
            self.show_weights(coins2)
            self.show_weights(others)
        # １回目の計測
        if coins1.is_eq(coins2):
            # 偽物は others の中にある
            if others[0].is_lt(others[1]):
                lighter_coin = others[0]
            else:
                lighter_coin = others[1]
            return lighter_coin.get_index()
        elif coins1.is_lt(coins2):
            lighter_coins = coins1
        else:
            lighter_coins = coins2

        # ２回目の分割
        (coin1, coin2, other) = self._split_coins(lighter_coins,
                                                  g1 = 1, g2 = 1)
        ### for debug
        if verbose == True:
            sys.stderr.write("### coin1: %s\n### coin2: %s\n### other: %s\n"
                             %(coin1, coin2, other))
            self.show_weights(coin1)
            self.show_weights(coin2)
            self.show_weights(other)
        # ２回目の計測
        if coin1.is_eq(coin2):
            # 偽物は other
            return other[0].get_index()
        elif coin1.is_lt(coin2):
            lighter_coin = coin1[0]
        else:
            lighter_coin = coin2[0]
        return lighter_coin.get_index()

    def solve2(self,):
        # １回目の分割
        (coins1, coins2, others) = self._split_coins(self._coins,
                                                     g1 = 3, g2 = 3)
        (a,b,c) = coins1
        (f,g,h) = coins2
        (d,e) = others
        coins3 = Coins([a,d,f])
        coins4 = Coins([c,e,h])
        # １回目の計測
        if coins1.is_eq(coins2):
            # 偽物は others (d,e) の中にある
            # ２回目の計測
            if coins3.is_lt(coins4):
                lighter_coin = d
            else:
                lighter_coin = e
        elif coins1.is_lt(coins2):
            # 偽物は coins1 (a,b,c) の中にある
            # ２回目の計測
            if coins3.is_eq(coins4):
                lighter_coin = b
            elif coins3.is_lt(coins4):
                lighter_coin = a
            else:
                lighter_coin = c
        else:
            # 偽物は coins2 (f,g,h) の中にある
            # ２回目の計測
            if coins3.is_eq(coins4):
                lighter_coin = g
            elif coins3.is_lt(coins4):
                lighter_coin = f
            else:
                lighter_coin = h
        return lighter_coin.get_index()
    """
    helper functions
    """
    # split coins into (g1, g2, others)
    def _split_coins(self, coins_to_split, g1 = 3, g2 = 3):
        sys.stderr.write("### coins_to_split: %s\n### g1: %d\n\n### g2: %d\n"
                         %(coins_to_split, g1, g2))
        coins = random.sample(coins_to_split, g1 + g2)
        coins1 = Coins( random.sample(coins, g1) )
        coins2 = Coins( [c for c in coins if c not in coins1] )
        others = Coins( [c for c in coins_to_split if c not in coins] )
        return (coins1, coins2, others)

    """
    for debug
    """
    def show_weights(self, coins):
        weights = [c.get_weight() for c in coins]
        sys.stderr.write("%s\n" %(weights))
        return
    """
    for validation
    """
    def test_answer(self, answer):
        weights = [c.get_weight() for c in self._coins]
        sys.stderr.write("%s\n" %(weights))
        return weights[answer] == FAKE_COIN_WEIGHT

def main():
    fc = FakeCoins()
    sys.stderr.write("### solve version1 ###\n")
    answer = fc.solve()
    print answer
    print fc.test_answer(answer)

    sys.stderr.write("### solve version2 ###\n")
    answer2 = fc.solve2()
    print answer2
    print fc.test_answer(answer2)

if __name__ == '__main__':
    main()
