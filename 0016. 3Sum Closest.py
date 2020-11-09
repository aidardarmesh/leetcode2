from typing import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res = -1
        abs_diff = float('inf')
        for i in range(len(nums)):
            left, right = i + 1, len(nums)-1
            two_sum = target - nums[i]
            
            while left < right:
                new_sum = nums[left] + nums[right]
                new_abs_diff = abs(new_sum - two_sum)
                
                if abs_diff > new_abs_diff:
                    abs_diff = new_abs_diff
                    res = new_sum + nums[i]
                
                if new_sum <= two_sum:
                    left += 1
                else:
                    right -= 1
        
        return res
