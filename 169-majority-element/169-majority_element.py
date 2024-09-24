from collections import defaultdict


def majorityElement(nums: list[int]):
    """
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.
    """
    count = defaultdict(int)
    n = len(nums)
    for num in nums:
        count[num] += 1
        if count[num] > n//2:
            return num


if __name__ == "__main__":
    print(majorityElement([3,2,3]))
    print(majorityElement([2,2,1,1,1,2,2]))
    print(majorityElement([1,1]))
