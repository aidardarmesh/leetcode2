/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hash = {};
    
    for(let i = 0; i < nums.length; i++) {
        let pair = target - nums[i];
        if(hash[pair] !== undefined) {
            return [hash[pair], i];
        } else {
            hash[nums[i]] = i;
        }
    }
    
    return [];
};
