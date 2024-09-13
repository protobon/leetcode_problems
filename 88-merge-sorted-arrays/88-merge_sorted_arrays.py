from typing import List

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, 
nums1 has a length of m + n, where the first m elements denote the 
elements that should be merged, and the last n elements are set to 0 
and should be ignored. nums2 has a length of n.
"""


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    """
    m: size of nums1
    n: size of nums2
    nums1: m values + n zeros
    nums2: n values
    description: Merges all numbers from 'nums2' into 'nums1', both lists are
    in ascended order, returns None.
    """

    # border cases
    if len(nums1) != m + n or len(nums2) != n or m < 0 or m + n > 200:
        return
    if m == 0:
        nums1[:] = nums2[:]
        return

    # logic
    for i in reversed(range(len(nums1))):
        if n == 0:
            break
        left = m - 1
        right = n - 1
        if m != 0 and nums1[left] > nums2[right]:
            nums1[i] = nums1[left]
            m -= 1
        else:
            nums1[i] = nums2[right]
            n -= 1
