import sys
from collections import defaultdict
from typing import List


# Returns the indices of two numbers that add up to the target
def two_sums(nums, target):

    lookup = defaultdict(list)
    for i, num in enumerate(nums):
        needed = target - num
        if needed in lookup:
            return [lookup[needed][0], i]
        lookup[num].append(i)

    return None


print(two_sums([1, 2, 3], 4))  # [0, 2]
print(two_sums([2, 7, 11, 15], 9))  # [0, 1]


def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if target - nums[i] in d:
            return [d[target - nums[i]], i]
        else:
            d[nums[i]] = i


print(twoSum([3, 2, 4], 6))  # [1, 2]


class Solution(object):
    def TooSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i


input_list = [3, 3]
ob1 = Solution()
print(ob1.TooSum(input_list, 6))  # [0, 1]


