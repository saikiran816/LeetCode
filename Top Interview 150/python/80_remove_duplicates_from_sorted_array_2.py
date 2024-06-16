# 26. Remove Duplicates from Sorted Array II - Medium
"""
Given an integer array nums sorted in non-decreasing order, remove some 
duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.
"""  # noqa

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i in nums:
            if idx == 0 or idx == 1 or nums[idx - 2] != i:
                nums[idx] = i
                idx += 1
        return idx


if __name__ == "__main__":
    solution = Solution()
    input_list = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1],
        [1, 1, 1, 2, 2, 3],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
    ]  # noqa
    expected_output = [
        [1, 1, 2],
        [0, 0, 1, 1, 2, 2, 3, 3, 4],
        [1],
        [1, 1, 2, 2, 3],
        [0, 0, 1, 1, 2, 3, 3],
    ]  # noqa
    actual_output = []
    for input in input_list:
        idx = solution.removeDuplicates(input)
        actual_output.append(input[:idx])

    for expected, actual in zip(expected_output, actual_output):
        assert expected == actual
