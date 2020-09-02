from typing import *

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(nums):
            if len(nums) <= 1:
                return 0
            
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            
            total = 0
            total += merge_sort(left)
            total += merge_sort(right)
            
            # counting reverse pairs
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] > 2*right[j]:
                    # all values after left[i] are larger than right[j]
                    # because left and right are already sorted
                    total += len(left)-i
                    j += 1
                else:
                    i += 1
            
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i, k = i+1, k+1
                else:
                    nums[k] = right[j]
                    j, k = j+1, k+1
            
            while i < len(left):
                nums[k] = left[i]
                i, k = i+1, k+1
            
            while j < len(right):
                nums[k] = right[j]
                j, k = j+1, k+1
            
            return total
        
        return merge_sort(nums)
