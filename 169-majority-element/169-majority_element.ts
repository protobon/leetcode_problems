/*
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.


*/
function majorityElement(nums: number[]): number {
    const n = nums.length

    let count = {}
    for (let i = 0; i < n; i++) {
        if (!(nums[i] in count)) {
            count[nums[i]] = 1
        } else {
            count[nums[i]]++
        }
        if (count[nums[i]] > n / 2) {
            return nums[i]
        }
    }

    return -1
};