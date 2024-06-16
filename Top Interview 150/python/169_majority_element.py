# 169. Majority Element - Easy
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""  # noqa

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track = count = 0
        for i in nums:
            if count == 0:
                track = i
            if i != track:
                count -= 1
            else:
                count += 1
        return track


if __name__ == "__main__":
    solution = Solution()
    input_list = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
        [9, 4, 9, 2, 9, 5, 7, 8, 9, 1],
    ]  # noqa
    expected_output = [3, 2, 9]  # noqa
    actual_output = []
    for input in input_list:
        max_repeat_num = solution.majorityElement(input)
        actual_output.append(max_repeat_num)

    for expected, actual in zip(expected_output, actual_output):
        assert expected == actual
