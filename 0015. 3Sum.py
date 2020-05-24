from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        three_sum = 0
        
        for i in range(len(nums)):
            two_sum = three_sum - nums[i]
            left, right = i+1, len(nums)-1
            
            while left < right:
                new_sum = nums[left] + nums[right]
                
                if new_sum == two_sum:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif new_sum < two_sum:
                    left += 1
                else:
                    right -= 1
        
        return res
