#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import Counter

map_dict = {"2": 2, "A": 1, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3}
def is_straight(sorted_keys):
    return map_dict[sorted_keys[4]] == map_dict[sorted_keys[3]] + 1 == map_dict[sorted_keys[2]] + 2 == map_dict[sorted_keys[1]] + 3 == map_dict[sorted_keys[0]] + 4

def get_category(card1, card2, card3, card4, card5):
    all_card_points = card1[0] + card2[0] + card3[0] + card4[0] + card5[0]
    count = Counter(all_card_points)
    count_list = list(count.values())
    max_value = max(count_list)
    # print(sorted(count.keys(), my_cmp))
    # print(sorted(count.keys(), key=lambda point: map_dict[point]))
    sorted_keys = sorted(count.keys(), key=lambda point: map_dict[point])
    print(sorted_keys)
    if max_value == 1:
        if is_straight(sorted_keys):
            return 'Straight'
        else:
            return 'High card'
    if max_value == 2:
        return 'Pair'
    if max_value == 3:
        return 'Three of a kind'
    if max_value == 4:
        return 'Four of a kind'


class PokerCard:
    category = 0

    def __init__(self, card1, card2, card3, card4, card5):
        self.category = get_category(card1, card2, card3, card4, card5)

    def getcategory(self):
        return self.category