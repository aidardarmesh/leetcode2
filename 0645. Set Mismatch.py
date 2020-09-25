from typing import *

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # cyclic-sort
        i = 0
        while i < len(nums):
            val = nums[i]
            
            if val == i+1 or nums[val-1] == val:
                i += 1
            else:
                nums[i], nums[val-1] = nums[val-1], nums[i]
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return [nums[i], i+1]
        
        return [-1, -1]
