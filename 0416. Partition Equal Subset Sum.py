from typing import *

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s % 2 == 1:
            return False
        
        dp = [[-1 for __ in range(s//2+1)] for _ in range(len(nums))]

        def partition_recursive(dp, nums, idx, curr_s):
            if curr_s == 0:
                return 1
            
            if idx >= len(nums):
                return 0
            
            if dp[idx][curr_s] != -1:
                return dp[idx][curr_s]
            
            if nums[idx] <= curr_s:
                if partition_recursive(dp, nums, idx+1, curr_s - nums[idx]) == 1:
                    dp[idx][curr_s] = 1
                    return 1
                    
            dp[idx][curr_s] = partition_recursive(dp, nums, idx+1, curr_s)
            
            return dp[idx][curr_s]
        
        return partition_recursive(dp, nums, 0, s//2) == 1
