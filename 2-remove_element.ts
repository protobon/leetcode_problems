function removeElement(nums: number[], val: number): number {
    let k = 0;
    while (k < nums.length) {
      if (nums[k] === val) {
        nums.splice(k, 1);
      } else {
        k++;
      }
    }
    return nums.length;
};