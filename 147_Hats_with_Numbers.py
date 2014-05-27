# -*- coding: utf-8 -*-

import random
import sys

class Hat:
    def __init__(self, num):
        self._num = num
        return
    def get(self,):
        return self._num

class Hats:
    def __init__(self, length): # nは人数
        self._hats = {}
        self._length = length
        return

    def set_hats(self, nums = []):
        if len(nums) == self._length:
            for i in range(self._length):
                self._hats[i] = Hat(nums[i])
            return
        # ランダムに生成
        for i in range(self._length):
            this_n = random.randint(0, self._length - 1)
            self._hats[i] = Hat(this_n)
        return

    def get_hats_num(self,):
        return [hat.get() for i,hat in self._hats.items()]
    def get_hats_num_except_me(self, me):
        return [hat.get() for i,hat in self._hats.items() if i != me]

def guess(alist, n, i):
    # alist: 自分以外の数字のリスト # n人中自分は i番目
    # x + sum(alist) % n = i となるような x を求める
    return (i - sum(alist)) % n

def judge(guesses, answers):
    if len(guesses) != len(answers):
        raise ValueError, 'len(guesses) has to be equal to len(answers)' %(len(guesses),
                                                                           len(answers))
    sys.stderr.write("""### answers: %s
### guesses: %s\n""" %(answers, guesses))
    for i in range(len(guesses)):
        if guesses[i] == answers[i]:
            sys.stderr.write("### Found.\n### %dth elements are %s\n"
                             %(i, guesses[i]))
            return True
    sys.stderr.write("### Not found.\n")
    return False

def main(n = 5):
    # 人数分の帽子
    hats = Hats(length = n)
    # ランダムに帽子に数字を書く
    hats.set_hats()
    # 各人が他人の帽子を見て自分の帽子の数字を推測
    guesses = []
    for i in range(n):
        hats_num_except_me = hats.get_hats_num_except_me(me = i)
        guesses.append( guess(hats_num_except_me, n, i) )
    # 1人でも正解していれば勝ち
    print judge(guesses, hats.get_hats_num())
    return

if __name__ == '__main__':
    main()
