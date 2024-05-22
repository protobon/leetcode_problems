/*
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
*/
function rotate(nums: number[], k: number): void {
    const n = nums.length
    let shift = "right"  // Default: shift to the right
    if (k > n) {
        k = k - n  // Case: k > n shifts k-n places to the right
    }
    else if (k > n / 2) {
        shift = "left"
        k = n - k  // Case: k > n/2 shifts n-k places to the left
    }

    if (shift === "left") {
        while (k > 0) {
            const firstElem = nums.shift()!
            nums.push(firstElem)
            k--
        }
    } else {
        while (k > 0) {
            const lastElem = nums.pop()!
            nums.unshift(lastElem)
            k--
        }
    }
};