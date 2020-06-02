from typing import *

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left, right = [0] * n, [0] * n
        left[0] = n-1
        right[n-1] = n-1
        
        for i in range(n):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1
        
        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < n-1:
                right[i] = right[i+1] + 1
        
        return max(min(left[i], right[i]) for i in range(n))
