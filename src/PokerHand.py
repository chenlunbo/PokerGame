#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import Counter

HIGH_CARD = 'High card'
PAIR = 'Pair'
THREE_OF_A_KIND = 'Three of a kind'
STRAIGHT = 'Straight'
FLUSH = 'Flush'
FULL_HOUSE = 'Full House'
FOUR_OF_A_KIND = 'Four of a kind'
ROYAL_FLUSH = 'Royal Flush'

SINGLE_CARD_POINT = 1
PAIR_CARD_POINT = 2
THREE_CARD_POINT = 3
FOUR_CARD_POINT = 4

MAP_DICT = {"2": 15, "A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4,
            "3": 3}


def is_straight(point_count):
    sorted_keys = sorted(point_count.keys(), key=lambda point: MAP_DICT[point])
    if sorted_keys == ['3', '4', '5', 'A', '2']:
        return True
    return MAP_DICT[sorted_keys[4]] == MAP_DICT[sorted_keys[3]] + 1 == MAP_DICT[sorted_keys[2]] + 2 == MAP_DICT[
        sorted_keys[1]] + 3 == MAP_DICT[sorted_keys[0]] + 4


def is_all_card_in_same_suit(card1, card2, card3, card4, card5):
    all_card_suits = (card1[1], card2[1], card3[1], card4[1], card5[1])
    suit_max_value = max(list(Counter(all_card_suits).values()))
    return suit_max_value == 5


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
    if is_all_card_in_same_suit(card1, card2, card3, card4, card5):
        if is_straight(point_count):
            return ROYAL_FLUSH
        return FLUSH
    if max_times_of_point == SINGLE_CARD_POINT:
        if is_straight(point_count):
            return STRAIGHT
        return HIGH_CARD
    if max_times_of_point == PAIR_CARD_POINT:
        return PAIR
    if max_times_of_point == THREE_CARD_POINT:
        if len(list(point_count.values())) == 2:
            return FULL_HOUSE
        return THREE_OF_A_KIND
    if max_times_of_point == FOUR_CARD_POINT:
        return FOUR_OF_A_KIND


class PokerCard:
    category = 0

    def __init__(self, card1, card2, card3, card4, card5):
        self.category = get_category(card1, card2, card3, card4, card5)

    def getcategory(self):
        return self.category
