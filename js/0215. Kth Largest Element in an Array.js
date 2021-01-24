/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    let sorted = nums.sort((a, b) => b - a);
    return sorted[k-1];
};
