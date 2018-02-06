import unittest
from src.entrance import BowlingScorer

class Test(unittest.TestCase):
    def testHappyFlow(self):
        self.assertTrue(True)

    def test_ten_times_sum_up_should_as_expected(self):
        bs1 = BowlingScorer()
        bs1.addRecord(1, 2)
        bs1.addRecord(3, 4)
        bs1.addRecord(5, 1)
        bs1.addRecord(2, 3)
        bs1.addRecord(4, 5)
        bs1.addRecord(1, 2)
        bs1.addRecord(3, 4)
        bs1.addRecord(5, 1)
        bs1.addRecord(2, 3)
        bs1.addRecord(4, 5)
        self.assertEqual(bs1.getScore(), 60)

    def test_9_and_no_pins_should_as_expected(self):
        bs = BowlingScorer()
        bs.addRecord(9, "-")
        bs.addRecord(9, "-")
        bs.addRecord(9, "-")
        bs.addRecord(9, "-")
        bs.addRecord(9, "-")
        bs.addRecord(9, "-")
        bs.addRecord(9, "-")
        bs.addRecord(9, "-")
        bs.addRecord(9, "-")
        bs.addRecord(9, "-")
        self.assertEqual(bs.getScore(), 90)



if __name__ == '__main__':
 +    unittest.main(verbosity=2)