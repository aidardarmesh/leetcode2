from typing import *

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def feasible(capacity):
            days = 1
            shipped = 0
            
            for weight in weights:
                shipped += weight
                if shipped > capacity:
                    days += 1
                    shipped = weight
                    if days > D:
                        return False
            
            return True
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
