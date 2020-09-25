from typing import *

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # cyclic-sort
        i = 0
        while i < len(nums):
            val = nums[i]
            
            if val == i+1 or nums[val-1] == val:
                i += 1
            else:
                nums[i], nums[val-1] = nums[val-1], nums[i]
        
        # gathering answer
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)
        
        return res
