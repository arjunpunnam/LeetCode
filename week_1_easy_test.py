from unittest import TestCase
from LeetCode.week_1_easy import contains_duplicate, missing_number, findDisappearedNumbers


class TestSolution(TestCase):
    def test_contains_duplicate(self):
        self.assertEquals(contains_duplicate([0]), False)
        self.assertEqual(contains_duplicate([3, 1]), False)

    def test_missing_numbers(self):
        self.assertEqual(missing_number([3, 0, 1]), 2)
        self.assertEqual(missing_number([9,6,4,2,3,5,7,0,1]), 8)
        self.assertEqual(missing_number([0]), 1)

    def test_findDisappearedNumbers(self):
        print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
        self.assertEqual(findDisappearedNumbers([4,3,2,7,8,2,3,1]) , [5,6])

