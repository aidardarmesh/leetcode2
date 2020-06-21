from typing import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        if len(nums) == 1:
            return [nums]
        
        res = []
        
        for i in range(len(nums)):
            for perm in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + perm)
        
        return res
