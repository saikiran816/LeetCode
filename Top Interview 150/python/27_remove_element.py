# 27. Remove Element - Easy
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:
 - Change the array nums such that the first k elements of nums contain 
 the elements which are not equal to val. The remaining elements of nums are 
 not important as well as the size of nums.
 - Return k.
"""  # noqa

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    input_list = [
        ([3, 2, 2, 3], 3),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
        ([], 3),
        ([3, 2, 2, 3], 5),
        ([2, 2, 2, 2], 2),
        ([2, 2, 3], 2),
    ]  # noqa
    expected_output = [[2, 2], [0, 1, 3, 0, 4], [], [3, 2, 2, 3], [], [3]]  # noqa
    actual_output = []
    for input in input_list:
        nums = input[0]
        idx = solution.removeElement(*input)
        actual_output.append(nums[:idx])

    for expected, actual in zip(expected_output, actual_output):
        assert expected == actual
