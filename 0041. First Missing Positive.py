from typing import *

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # cyclic-sort
        i, end = 0, len(nums)
        while i != end:
            val = nums[i]
            
            if val == i+1:
                i += 1
            elif val > end or val <= 0 or nums[val-1] == val:
                end -= 1
                nums[i], nums[end] = nums[end], nums[i]
            else:
                nums[i], nums[val-1] = nums[val-1], nums[i]
        
        return i+1

