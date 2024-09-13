def findClosestNumber(nums: list[int]) -> int:
        """
        Given a list of positive and negative numbers, find the number that's closest to zero.
        Return the number with the largest value.

        Constraints:

        1 <= n <= 1000

        -10^5 <= nums[i] <= 10^5
        """
        closest = nums[0]
        for num in nums:
            if num < 0:
                if abs(num) < abs(closest):
                    closest = num
            else:
                if num <= abs(closest):
                    closest = num
        return closest
