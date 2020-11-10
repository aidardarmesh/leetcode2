from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import heapq
        heap = []
        
        for num in nums1:
            heapq.heappush(heap, num)
        
        for num in nums2:
            heapq.heappush(heap, num)
        
        n = len(nums1) + len(nums2)
        is_odd = n % 2 == 1
        res = 0
        
        for _ in range(n // 2):
            res = heapq.heappop(heap)
        
        if is_odd:
            res = heapq.heappop(heap)
        else:
            res += heapq.heappop(heap)
            res /= 2
        
        return res
