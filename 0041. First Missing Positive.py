from typing import *

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # cyclic-sort
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != i+1:
                j = nums[i]-1
                
                # checking pair in correct place
                if nums[j] == j+1:
                    i += 1
                    continue
                    
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        # search for number that is not in place
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        
        return len(nums)+1

