from unittest import TestCase

from main import findDisappearedNumbers


class Test(TestCase):
    def test_find_disappeared_numbers(self):
        result = findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
        self.assertEqual(result, [5, 6])

        result2 = findDisappearedNumbers([0])
        self.assertEqual(result2, [0])
