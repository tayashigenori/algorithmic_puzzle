# -*- coding: utf-8 -*-

import sys
import random

class Coin:
    # fake coin is lighter than authentic ones
    FAKE_COIN_WEIGHT = 10
    AUTHENTIC_COIN_WEIGHT = 11

    def __init__(self, i, is_fake = False):
        self._i = i
        self._is_fake = is_fake
        if is_fake == True:
            self._weight = self.FAKE_COIN_WEIGHT
        else:
            self._weight = self.AUTHENTIC_COIN_WEIGHT
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

    """
    helper functions
    """
    # split coins into (g1, g2, others)
    def _split_coins(self, g1 = 3, g2 = 3):
        sys.stderr.write("### coins_to_split: %s\n### g1: %d\n\n### g2: %d\n"
                         %(self, g1, g2))
        coins = random.sample(self, g1 + g2)
        coins1 = Coins( random.sample(coins, g1) )
        coins2 = Coins( [c for c in coins if c not in coins1] )
        others = Coins( [c for c in self if c not in coins] )
        return (coins1, coins2, others)

    """
    for debug
    """
    def show_weights(self,):
        weights = [c.get_weight() for c in self]
        sys.stderr.write("%s\n" %(weights))
        return
