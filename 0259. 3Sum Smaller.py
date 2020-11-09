from typing import *

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res = 0
        for i in range(len(nums)):
            two_sum = target - nums[i]
            left, right = i+1, len(nums)-1
            
            while left < right:
                new_two_sum = nums[left] + nums[right]
                
                if new_two_sum < two_sum:
                    res += right-left
                    left += 1
                else:
                    right -= 1
        
        return res
