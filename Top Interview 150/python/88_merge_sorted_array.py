# 88. Merge Sorted Array - Easy
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""  # noqa

from typing import List


class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, len(a) - 1
        while i >= 0 and j >= 0:
            if a[i] > b[j]:
                a[k] = a[i]
                i -= 1
            else:
                a[k] = b[j]
                j -= 1
            k -= 1

        while i >= 0:
            a[k] = a[i]
            i -= 1
            k -= 1

        while j >= 0:
            a[k] = b[j]
            j -= 1
            k -= 1


if __name__ == "__main__":
    solution = Solution()
    sample_input = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        ([1], 1, [], 0),
        ([0], 0, [1], 1),
        ([1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0], 5, [-5, -2, 0, 1, 2, 6], 6),
    ]
    expected_output = [
        [1, 2, 2, 3, 5, 6],
        [1],
        [1],
        [-5, -2, 0, 1, 1, 2, 2, 3, 4, 5, 6],
    ]  # noqa

    actual_output = []
    for input in sample_input:
        x = input[0]
        solution.merge(*input)
        actual_output.append(x)

    for expected, actual in zip(expected_output, actual_output):
        assert expected == actual
