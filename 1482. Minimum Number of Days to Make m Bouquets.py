from typing import *

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(days):
            bouquets = ready_flowers = 0
            
            for bday in bloomDay:
                if bday > days:
                    bouquets += ready_flowers // k
                    ready_flowers = 0
                else:
                    ready_flowers += 1
            
            bouquets += ready_flowers // k
            
            return bouquets >= m
        
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right-left) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if possible(left) else -1
