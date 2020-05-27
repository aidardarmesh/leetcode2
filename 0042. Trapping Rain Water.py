from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        dp_left = [0] * n
        max_left = 0
        
        for i in range(n):
            max_left = max(max_left, height[i])
            dp_left[i] = max_left
        
        dp_right = [0] * n
        max_right = 0
        
        for i in range(n-1, -1, -1):
            max_right = max(max_right, height[i])
            dp_right[i] = max_right
        
        volume = 0
        
        for i in range(n):
            volume += min(dp_left[i], dp_right[i]) - height[i]
        
        return volume
