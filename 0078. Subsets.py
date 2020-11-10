from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def generate(subset, idx, nums, res):
            res.append(subset)
            
            for i in range(idx, len(nums)):
                generate(subset[:] + [nums[i]], i+1, nums, res)
        
        generate([], 0, nums, res)
        
        return res
