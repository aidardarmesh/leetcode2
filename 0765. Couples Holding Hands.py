from typing import *

class Solution:
    def minSwapsCouples(self, nums: List[int]) -> int:
        num_idx = {num:i for i, num in enumerate(nums)}
        swaps = 0
        
        for i in range(0, len(nums)-1, 2):
            if nums[i] % 2 == 0:
                pair = nums[i]+1
            else:
                pair = nums[i]-1
            
            if nums[i+1] != pair:
                pair_idx = num_idx[pair]
                correct_idx = i+1
                
                temp = nums[correct_idx]
                
                nums[correct_idx], nums[pair_idx] = pair, temp
                num_idx[temp], num_idx[pair] = num_idx[pair], num_idx[temp]
                swaps += 1
        
        return swaps
