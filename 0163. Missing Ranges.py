from typing import *

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        curr = lower
        nums.append(upper+1)
        
        for i in range(len(nums)):
            delta = nums[i] - curr
            
            if delta <= 0:
                curr = nums[i] + 1
            elif delta == 1:
                res.append(str(curr))
                curr = nums[i] + 1
            else:
                res.append(str(curr) + '->' + str(nums[i]-1))
                curr = nums[i]+1
        
        return res
