from typing import *

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        nums = [lower-1] + nums + [upper+1]
        
        for i in range(len(nums)-1):
            delta = nums[i+1] - nums[i]
            
            if delta == 2:
                res.append(str(nums[i]+1))
            elif delta > 2:
                res.append(str(nums[i]+1) + '->' + str(nums[i+1]-1))
        
        return res
