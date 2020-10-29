from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    s = set()
    if len(nums) == 1:
        return False
    for item in nums:
        if item in s:
            return True
        else:
            s.add(item)
    return False


def missing_number(nums: List[int]) -> int:
    s = set()
    for i in nums:
        s.add(i)

    n = range(len(nums) + 1)
    for i in n:
        if i not in s:
            return i


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    #Look at abs solution
    #Look at implementing without extra space
    unique = set()
    result = []

    for i in nums:
        unique.add(i)

    for i in range(1, len(nums) + 1):
        if i not in unique:
            result.append(i)
    return result
