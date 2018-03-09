import unittest

from src.PokerHand import PokerCard


class TestCategory(unittest.TestCase):
    def testHappyFlow(self):
        self.assertTrue(True)

    def test_card_category(self):
        card = PokerCard("AS", "3D", "6C", "JS", "QC")
        self.assertEqual('High card', card.category)

    def test_pair_card_category(self):
        card = PokerCard("AS", "3D", "3C", "JS", "QC")
        self.assertEqual('Pair', card.category)

    def test_three_of_a_kind_card_category(self):
        card = PokerCard("AS", "3D", "3C", "3S", "QC")
        self.assertEqual('Three of a kind', card.category)

    def test_straight_category(self):
        card = PokerCard("AS", "2D", "3C", "4S", "5C")
        self.assertEqual('Straight', card.category)

    def test_flush_category(self):
        card = PokerCard("AS", "5S", "3S", "9S", "JS")
        self.assertEqual('Flush', card.category)

    def test_full_house_category(self):
        card = PokerCard("3S", "3D", "3H", "JS", "JC")
        self.assertEqual('Full House', card.category)

    def test_four_of_a_kind_category(self):
        card = PokerCard("3S", "3D", "3H", "3C", "JC")
        self.assertEqual('Four of a kind', card.category)

    def test_royal_flush_category(self):
        card = PokerCard("AS", "2S", "4S", "3S", "5S")
        self.assertEqual('Royal Flush', card.category)


class TestExtraCase(unittest.TestCase):
    def test_special_straight_case(self):
        card = PokerCard("10S", "JD", "QC", "KS", "AC")
        self.assertEqual('Straight', card.category)

    def test_min_straight_case(self):
        card = PokerCard("3S", "4D", "5C", "6S", "7C")
        self.assertEqual('Straight', card.category)

if __name__ == '__main__':
    unittest.main(verbosity=2)
