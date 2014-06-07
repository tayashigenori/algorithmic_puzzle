# -*- coding: utf-8 -*-

import sys
import random

class Rumor:
    def __init__(self, i):
        self._i = i
        return

class Person:
    def __init__(self, i):
        self._i = i
        self._rumors = {i: True} # この人が知っている噂
        return
    def get_index(self,):
        return self._i
    def get_rumors(self,):
        return self._rumors
    def add_rumors(self, rumors):
        for r in rumors:
            self.add_rumor(r)
        return
    def add_rumor(self, rumor):
        self._rumors[rumor] = True
        return

class RumorSpreading1:
    def __init__(self, n):
        self._n = n
        self._people = [Person(i) for i in range(n)]
        return

    def send_mail(self, sender, sendee):
        rumors = sender.get_rumors()
        sendee.add_rumors(rumors)
        return

    def solve(self, strategy = 'greedy'):
        if strategy == 'greedy':
            self.solve_greedy()
        else:
            self.solve_naive()
    def solve_naive(self,):
        gossip_center = random.choise(self._people)
        # gossip_center にすべての情報を集める
        for p in self._people:
            if p.get_index() != gossip_center.get_index():
                self.send_mail(p, gossip_center)
        # これで gossip_center はすべての噂を知っている
        self._spread_from_gossip_center(gossip_center)
        return
    def solve_greedy(self,):
        for i in range(self._n):
            if self._people[i] == self._people[-1]:
                break
            self.send_mail(sender = self._people[i],
                           sendee = self._people[i+1])
        # これで self._poeple[-1] はすべての噂を知っている
        self._spread_from_gossip_center(gossip_center = self._people[-1])
        return
    def _spread_from_gossip_center(self, gossip_center):
        for q in self._people:
            if q.get_index() != gossip_center.get_index():
                self.send_mail(gossip_center, q)
        return

    def test(self,):
        for p in self._people:
            sys.stderr.write("%s\n" %(p.get_rumors()))
            if len(p.get_rumors()) != self._n:
                return False
        return True

def main():
    rs = RumorSpreading1(10)
    rs.solve()
    print rs.test()

if __name__ == '__main__':
    main()
