from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:

    unique = set()
    for i in nums:
        unique.add(i)
    result = list()

    for i in range(1, len(nums)+1):
        if i not in nums:
            result.append(i)
    return result


