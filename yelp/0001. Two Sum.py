from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        val_idx = {}
        
        for i in range(n):
            complement = target - nums[i]
            
            if complement in val_idx:
                return [val_idx[complement], i]
            
            val_idx[nums[i]] = i
        
        return [-1, -1]
