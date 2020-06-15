from typing import *

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import functools
        
        def comparator(p1, p2):
            return (p1[0]**2 + p1[1]**2) - (p2[0]**2 + p2[1]**2)
        
        return sorted(points, key=functools.cmp_to_key(comparator))[:K]
