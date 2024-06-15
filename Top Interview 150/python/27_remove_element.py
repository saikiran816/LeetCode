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
        if val not in nums:
            return len(nums)
        if (len(set(nums)) == 1 and val in nums) or (len(nums) == 0):
            return 0
        i, j = 0, len(nums) - 1
        idx_count = 0
        while i <= j:
            if nums[j] == val:
                j -= 1
                idx_count += 1
                continue
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                idx_count += 1
            i += 1
        return len(nums) - idx_count


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
    expected_output = [[2, 2], [0, 1, 4, 0, 3], [], [3, 2, 2, 3], [], [3]]  # noqa
    actual_output = []
    for input in input_list:
        nums = input[0]
        idx = solution.removeElement(*input)
        actual_output.append(nums[:idx])

    for expected, actual in zip(expected_output, actual_output):
        assert expected == actual
