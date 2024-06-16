# 26. Remove Duplicates from Sorted Array - Easy
"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, 
to get accepted, you need to do the following things:
 - Change the array nums such that the first k elements of nums contain 
 the unique elements in the order they were present in nums initially. 
 The remaining elements of nums are not important as well as the size of nums.
 - Return k.
"""  # noqa

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i in nums:
            if idx == 0 or nums[idx - 1] != i:
                nums[idx] = i
                idx += 1
        return idx


if __name__ == "__main__":
    solution = Solution()
    input_list = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1],
    ]  # noqa
    expected_output = [[1, 2], [0, 1, 2, 3, 4], [1]]  # noqa
    actual_output = []
    for input in input_list:
        idx = solution.removeDuplicates(input)
        actual_output.append(input[:idx])

    for expected, actual in zip(expected_output, actual_output):
        assert expected == actual
