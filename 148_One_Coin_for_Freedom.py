# -*- coding: utf-8 -*-

import random
import sys

COIN_TOP = 1 # 表
COIN_TAIL = 0 # 裏

class ChessBoard:
    def __init__(self, length = 64):
        self._coins = {}
        for i in range(length):
            self._coins[i] = COIN_TOP
        return
    # ランダムにコインを裏返す
    def initialize(self,):
        randomly_selected_coins = random.sample(self._coins.keys(),
                                                random.randint(0, self.get_length() -1))
        for rsc in randomly_selected_coins:
            self._coins[rsc] = COIN_TAIL
        return
    # チェス盤の長さを取得する
    def get_length(self,):
        return len(self._coins)
    # 裏向きのコインのリストを取得する
    def get_tail_coins(self,):
        return [i for i in self._coins if self._coins[i] == COIN_TAIL]
    # 指定のコインを裏返す
    def flip(self, coin_to_flip):
        if isinstance(coin_to_flip, int) == False:
            raise TypeError, 'int expected'
        if coin_to_flip >= self.get_length():
            raise ValueError, 'coin does not exist'
        self._coins[coin_to_flip] = not self._coins[coin_to_flip]
        return

# 暗号化と復号化は同じ xor 関数
def encrypt(alist):
    return xor(alist)
def decrypt(alist):
    return xor(alist)
# リスト内の要素すべての xor を取る
def xor(alist):
    if isinstance(alist, list) == False:
        raise TypeError, "alist %s: list exprected" %alist
    if len(alist) == 0:
        return 0
    return reduce(lambda x,y: x^y, alist)

def main1():
    cb = ChessBoard(length = 64)
    cb.initialize()
    cb_length = cb.get_length()
    # debug
    sys.stderr.write("### tail coins: %s\n" %cb.get_tail_coins())

    # 看守がコインを一枚選択する
    answer_num = random.randint(0, cb_length - 1) # 本で言うところの J
    # debug
    sys.stderr.write("### answer_num: %d\n" %answer_num)

    # 囚人A は answer_num を知った上で裏返すべきコインを計算する
    T = cb.get_tail_coins()
    J = answer_num
    coin_to_flip = encrypt( T + [J] ) # 本で言うところの X
    # debug
    sys.stderr.write("### coin_to_flip: %d\n" %coin_to_flip)
    cb.flip(coin_to_flip)

    # 囚人B はチェスの盤面だけを見て看守の選んだコインを当てる
    answer_num_guessed = decrypt( cb.get_tail_coins() )
    # debug
    sys.stderr.write("### answer_num_guessed: %d\n" %answer_num_guessed)

    print answer_num_guessed == answer_num

if __name__ == '__main__':
    main1()
