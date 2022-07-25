import sys
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    print(nums, target)

twoSum([1, 2, 3], 4)        # [0, 2]
twoSum([2, 7, 11, 15], 9)   # [0, 1]
twoSum([3, 2, 4], 6)        # [1, 2]
twoSum([3, 3], 6)           # [0, 1]
