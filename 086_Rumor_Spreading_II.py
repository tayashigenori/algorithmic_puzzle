# -*- coding: utf-8 -*-

import sys
import random

import importlib
Rumor_Spreading_I_module = importlib.import_module("085_Rumor_Spreading_I")

class RumorSpreading2(Rumor_Spreading_I_module.RumorSpreading1):
    def phone_call(self, person1, person2):
        rumors1 = person1.get_rumors()
        person2.add_rumors(rumors1)
        rumors2 = person2.get_rumors()
        person1.add_rumors(rumors2)
        return

    def solve(self,):
        if self._n == 1:
            return
        if self._n == 2:
            self._phone_call(person1 = self._people[0],
                             person2 = self._people[-1])
            return
        if self._n == 3:
            self._solve_3(person1 = self._people[0],
                          person2 = self._people[1],
                          person3 = self._people[2])
            return
        self._solve_all()
    def _solve_all(self,):
        gossip_group = random.sample(self._people, 4)
        gossip_center = random.choice(gossip_group)
        others = [person for person in self._people if person not in gossip_group]

        # gossip_center calls others
        for o in others:
            self.phone_call(gossip_center, o)
        # share rumor in gossip_group
        self._solve_4(gossip_group[0], gossip_group[1],
                      gossip_group[2], gossip_group[3])
        # gossip_center calls others again
        for o in others:
            self.phone_call(gossip_center, o)
        return
    def _solve_3(self, person1, person2, person3):
        self.phone_call(person1, person2)
        self.phone_call(person2, person3)
        self.phone_call(person3, person1)
        return
    def _solve_4(self, person1, person2, person3, person4):
        # share inside (1,2)
        self.phone_call(person1, person2)
        # share inside (3,4)
        self.phone_call(person3, person4)
        # share betweeen (1,2) & (3,4)
        self.phone_call(person1, person4)
        self.phone_call(person2, person3)
        return

def main():
    rs = RumorSpreading2(10)
    rs.solve()
    print rs.test()

    rs = RumorSpreading2(4)
    rs.solve()
    print rs.test()


if __name__ == '__main__':
    main()
