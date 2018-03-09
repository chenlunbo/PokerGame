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

MAP_DICT = {"2": 15, "A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3}


def is_straight(point_count):
    sorted_keys = sorted(point_count.keys(), key=lambda point: MAP_DICT[point])
    if sorted_keys == ['3', '4', '5', 'A', '2']:
        return True
    return MAP_DICT[sorted_keys[4]] == MAP_DICT[sorted_keys[3]] + 1 == MAP_DICT[sorted_keys[2]] + 2 == MAP_DICT[
        sorted_keys[1]] + 3 == MAP_DICT[sorted_keys[0]] + 4


def is_all_card_in_same_suit(suit_count):
    return max(list(suit_count.values())) == 5


def is_only_two_suits(point_count):
    return len(list(point_count.values())) == 2


def get_point_category(point_count):
    return max(list(point_count.values()))


def is_category_royal_flush(point_count, suit_count):
    return is_all_card_in_same_suit(suit_count) and is_straight(point_count)


def is_category_flush(point_count, suit_count):
    return is_all_card_in_same_suit(suit_count) and not is_straight(point_count)


def is_category_straight(point_count):
    return get_point_category(point_count) == SINGLE_CARD_POINT and is_straight(point_count)


def is_category_high_card(point_count):
    return get_point_category(point_count) == SINGLE_CARD_POINT and not is_straight(point_count)


def is_category_pair(point_count):
    return get_point_category(point_count) == PAIR_CARD_POINT


def is_category_full_house(point_count):
    return get_point_category(point_count) == THREE_CARD_POINT and is_only_two_suits(point_count)


def is_category_three_of_a_kind(point_count):
    return get_point_category(point_count) == THREE_CARD_POINT and not is_only_two_suits(point_count)


def is_category_four_of_a_kind(point_count):
    return get_point_category(point_count) == FOUR_CARD_POINT


def get_category(card1, card2, card3, card4, card5):
    point_count = Counter((card1[:-1], card2[:-1], card3[:-1], card4[:-1], card5[:-1]))
    suit_count = Counter((card1[1], card2[1], card3[1], card4[1], card5[1]))
    if is_category_royal_flush(point_count, suit_count):
        return ROYAL_FLUSH
    if is_category_flush(point_count, suit_count):
        return FLUSH
    if is_category_high_card(point_count):
        return HIGH_CARD
    if is_category_pair(point_count):
        return PAIR
    if is_category_straight(point_count):
        return STRAIGHT
    if is_category_three_of_a_kind(point_count):
        return THREE_OF_A_KIND
    if is_category_full_house(point_count):
        return FULL_HOUSE
    if is_category_four_of_a_kind(point_count):
        return FOUR_OF_A_KIND
    return HIGH_CARD


class PokerCard:
    category = 0

    def __init__(self, card1, card2, card3, card4, card5):
        self.category = get_category(card1, card2, card3, card4, card5)

    def getcategory(self):
        return self.category
