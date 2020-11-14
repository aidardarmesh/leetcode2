from typing import *

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        while i < n:
            num = nums[i]
            
            if num < n and num != i:
                nums[i], nums[num] = nums[num], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i:
                return i
        
        return n
