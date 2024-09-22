def twoSum(nums: list[int], target: int):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    """

    indices = dict()
    for i in range(len(nums)):
        res = target - nums[i]
        if res in indices:
            return [indices[res], i]
        indices[nums[i]] = i


if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))
    print(twoSum([3,2,4], 6))
    print(twoSum([3,3], 6))
    print(twoSum([-1,-2,-3,-4,-5], -8))
    print(twoSum([-3,4,3,90], 0))
