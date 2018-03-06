#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import Counter

map_dict = {"2": 2, "A": 1, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3}


def is_straight(sorted_keys):
    return map_dict[sorted_keys[4]] == map_dict[sorted_keys[3]] + 1 == map_dict[sorted_keys[2]] + 2 == map_dict[
        sorted_keys[1]] + 3 == map_dict[sorted_keys[0]] + 4


def get_category(card1, card2, card3, card4, card5):
    all_card_points = (
        card1[0:len(card1) - 1],
        card2[0:len(card2) - 1],
        card3[0:len(card3) - 1],
        card4[0:len(card4) - 1],
        card5[0:len(card5) - 1]
    )
    point_count = Counter(all_card_points)
    max_times_of_point = max(list(point_count.values()))
    sorted_keys = sorted(point_count.keys(), key=lambda point: map_dict[point])
    if is_all_card_in_same_suit(card1, card2, card3, card4, card5):
        if is_straight(sorted_keys):
            return 'Royal Flush'
        return 'Flush'
    if max_times_of_point == 1:
        if is_straight(sorted_keys):
            return 'Straight'
        return 'High card'
    if max_times_of_point == 2:
        return 'Pair'
    if max_times_of_point == 3:
        if len(list(point_count.values())) == 2:
            return 'Full House'
        return 'Three of a kind'
    if max_times_of_point == 4:
        return 'Four of a kind'


def is_all_card_in_same_suit(card1, card2, card3, card4, card5):
    all_card_suits = (card1[1], card2[1], card3[1], card4[1], card5[1])
    suit_max_value = max(list(Counter(all_card_suits).values()))
    return suit_max_value == 5


class PokerCard:
    category = 0

    def __init__(self, card1, card2, card3, card4, card5):
        self.category = get_category(card1, card2, card3, card4, card5)

    def getcategory(self):
        return self.category
