from typing import *

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        sum_ = 0
        left = 0
        
        for right in range(len(nums)):
            sum_ += nums[right]
            
            if right >= k-1:
                max_avg = max(max_avg, sum_ / k)
                sum_ -= nums[left]
                left += 1
        
        return max_avg
